#include "Character.h"
#include <Utils/Utils.h>
#include <stdio.h>


/**
	the constructor
*/
Character::Character() : ArticulatedFigure() {
	this->COMController = CentreOfMass((ArticulatedFigure*) this);
}

/**
	the destructor
*/
Character::~Character(void) {
	//nothing to do. We'll let whoever created the world deal with freeing it up
}

/**
	This method is used to populate the relative orientation of the parent and child bodies of joint i.
*/
void Character::getRelativeOrientation(int i, Quaternion* qRel){
	//rotation from child frame to world, and then from world to parent == rotation from child to parent
	joints[i]->computeRelativeOrientation(*qRel);
}

/**
	This method is used to get the relative angular velocities of the parent and child bodies of joint i,
	expressed in parent's local coordinates. 
	We'll assume that i is in the range 0 - joints.size()-1!!!
*/
void Character::getRelativeAngularVelocity(int i, Vector3d* wRel){
	*wRel = joints[i]->child->state.angularVelocity - joints[i]->parent->state.angularVelocity;
	//we will store wRel in the parent's coordinates, to get an orientation invariant expression for it
	*wRel = joints[i]->parent->getLocalCoordinates(*wRel);
}


/**
	This method populates the dynamic array passed in with the state of the character.
	For the state, we consider the 13-dimensional state of the root, and then only
	the relative orientation and angular velocity (as measured from the parent) for
	every other link. The velocities of the CM are derived from this information,
	using the velocity propagation technique (if that's what it is called).		
	The only thing we will not be storing explicitly is the positions of the CMs of the rigid bodies. 
	The order in which the bodies appear is given by the array of joints. 
	This works under the assumption that in the joint 
	sequence, the parent of any rigid body appears before its children (assuming that for each joint
	we read the parent first and then the child). 
*/
void Character::getState(ReducedCharacterStateArray* state){
	updateJointOrdering();
	//we'll push the root's state information - ugly code....
	state->push_back(root->state.position.x);
	state->push_back(root->state.position.y);
	state->push_back(root->state.position.z);

	state->push_back(root->state.orientation.s);
	state->push_back(root->state.orientation.v.x);
	state->push_back(root->state.orientation.v.y);
	state->push_back(root->state.orientation.v.z);

	state->push_back(root->state.velocity.x);
	state->push_back(root->state.velocity.y);
	state->push_back(root->state.velocity.z);

	state->push_back(root->state.angularVelocity.x);
	state->push_back(root->state.angularVelocity.y);
	state->push_back(root->state.angularVelocity.z);

	//now each joint introduces one more rigid body, so we'll only record its state relative to its parent.
	//we are assuming here that each joint is revolute!!!
	Quaternion qRel;
	Vector3d wRel;

	for (uint i=0;i<joints.size();i++){
		getRelativeOrientation(jointOrder[i], &qRel);
	
		state->push_back(qRel.s);
		state->push_back(qRel.v.x);
		state->push_back(qRel.v.y);
		state->push_back(qRel.v.z);

		getRelativeAngularVelocity(jointOrder[i], &wRel);
		state->push_back(wRel.x);
		state->push_back(wRel.y);
		state->push_back(wRel.z);
	}
}

/**
	This method populates the state of the current character with the values that are passed
	in the dynamic array. The same conventions as for the getState() method are assumed.
*/
void Character::setState(ReducedCharacterStateArray* state, int start, bool hackFlag){
	updateJointOrdering();
	ReducedCharacterState rs(state, start);

	//kinda ugly code....
	root->state.position = rs.getPosition();
	root->state.orientation = rs.getOrientation();
	root->state.velocity = rs.getVelocity();
	root->state.angularVelocity = rs.getAngularVelocity();

	//now each joint introduces one more rigid body, so we'll only record its state relative to its parent.
	//we are assuming here that each joint is revolute!!!
	Quaternion qRel;
	Vector3d wRel;

	Vector3d r;
	Vector3d d;
	Vector3d vRel;

//	root->updateToWorldTransformation();
	for (uint j=0;j<joints.size();j++){
		qRel = rs.getJointRelativeOrientation(j);
		wRel = rs.getJointRelativeAngVelocity(j);
		//transform the relative angular velocity to world coordinates
		wRel = joints[j]->parent->getWorldCoordinates(wRel);

		//now that we have this information, we need to restore the state of the rigid body.

		//set the proper orientation
		int orderedJ = j;
		if( hackFlag )
			orderedJ = jointOrder[j];


		joints[orderedJ]->child->state.orientation = joints[orderedJ]->parent->state.orientation * qRel;
		//and the proper angular velocity
		joints[orderedJ]->child->state.angularVelocity = joints[orderedJ]->parent->state.angularVelocity + wRel;
		//and now set the linear position and velocity
		joints[orderedJ]->fixJointConstraints(false, true, false);
//		joints[j]->child->updateToWorldTransformation();
	}
}

/**
	this method is used to return the current heading of the character, specified as an angle measured in radians
*/
double Character::getHeadingAngle(){
	//first we need to get the current heading of the character. Also, note that q and -q represent the same rotation
	Quaternion q = getHeading();
	if (q.s<0){
		q.s = -q.s;
		q.v = -q.v;
	}
	double currentHeading = 2 * safeACOS(q.s);
	if (q.v.dotProductWith(PhysicsGlobals::up) < 0)
		currentHeading = -currentHeading;
	return currentHeading;
}


/**
	This method returns the dimension of the state. Note that we will consider
	each joint as having 3-DOFs (represented by the 4 values of the quaternion)
	without taking into account what type of joint it is (i.e. a hinge joint
	has only one degree of freedom, but we will still consider the relative orientation
	of the child relative to the parent as a quaternion.
*/
int Character::getStateDimension(){
	//13 for the root, and 7 for every other body (and each body is introduced by a joint).
	return 13 + 7 * joints.size();
}


/**
	This method is used to mirror the given orientation. It is assumed that rotations in the sagittal plane
	(about parent frame x-axis) are to stay the same, while the rotations about the other axes need to be reversed.
*/
Quaternion mirrorOrientation(const Quaternion& q){
	//get the rotation about the parent's x-axis
	Quaternion qSagittal = q.getComplexConjugate().decomposeRotation(Vector3d(1, 0, 0)).getComplexConjugate();
	//this is what is left, if we removed that component of the rotation
	Quaternion qOther = q * qSagittal.getComplexConjugate();
	//and now negate the non-sagittal part of the rotation, but keep the rotation in the sagittal plane
	return qOther.getComplexConjugate() * qSagittal;
}

/**
	This method is used to multiply, element-wise, the two vectors that are passed in  
*/
Vector3d elemWiseMultiply(const Vector3d& a, const Vector3d& b){
	return Vector3d(a.x * b.x, a.y * b.y, a.z * b.z);
}

/**
	this method takes the state of the character, passed in as an array of doubles, and reverses it inplace
*/
void Character::reverseStanceOfStateArray(ReducedCharacterStateArray* state, int start){
	ReducedCharacterState chS(state, start);

	char name[100];

	//now we're ready to start swapping left and right body parts
	for (uint i=0;i<joints.size();i++){
		//get the name of the joint, and if it's a right joint, and can be matched with one on the left, swap them
		strcpy(name, joints[jointOrder[i]]->name);
		if (name[0] == 'r'){
			int rJointIndex = i;
			name[0] = 'l';
			int lJointIndex = reverseJointOrder[this->getJointIndex(name)];
			if (lJointIndex > 0){
				//ok, swap the angular velocities and the orientations
				Quaternion qr = chS.getJointRelativeOrientation(rJointIndex);
				Quaternion ql = chS.getJointRelativeOrientation(lJointIndex);
				chS.setJointRelativeOrientation(ql, rJointIndex);
				chS.setJointRelativeOrientation(qr, lJointIndex);
				Vector3d wr = chS.getJointRelativeAngVelocity(rJointIndex);
				Vector3d wl = chS.getJointRelativeAngVelocity(lJointIndex);
				chS.setJointRelativeAngVelocity(wl, rJointIndex);
				chS.setJointRelativeAngVelocity(wr, lJointIndex);
			}
		}
	}

	//now reflect/mirror all the orientations and angular velocities,
	//now we're ready to start swapping left and right body parts
	for (uint i=0;i<joints.size();i++){
		//orientations
		chS.setJointRelativeOrientation(mirrorOrientation(chS.getJointRelativeOrientation(i)), i);
		//angular velocities - assume that ang velocity about the x axis results in rotation in the sagittal plane, so it shouldn't be changed
		chS.setJointRelativeAngVelocity(elemWiseMultiply(chS.getJointRelativeAngVelocity(i), Vector3d(1, -1, -1)), i);
	}

	//and now take care of the root information
	chS.setOrientation(mirrorOrientation(chS.getOrientation()));
	chS.setAngularVelocity(elemWiseMultiply(chS.getAngularVelocity(), Vector3d(1, -1, -1)));
	//for the velocity, we only want the x-component reversed (i.e. movement in the sagittal plane should stay the same)
	chS.setVelocity(elemWiseMultiply(chS.getVelocity(), Vector3d(-1, 1, 1)));	
}

/**
	this method is used to retrieve the reduced state of the character, but with the stance reversed.
*/
void Character::getReverseStanceState(ReducedCharacterStateArray* state){
	//this is the index where we will start populating the data in the state array
	int start = state->size();
	getState(state);
	reverseStanceOfStateArray(state, start);
}


/**
	This method is used to compute the center of mass of the articulated figure.
*/
Vector3d Character::getCOM(){

	// We must reverse the error in the perceived vs. the real centre of mass,
	// otherwise the character corrects in the wrong direction.

	// An more straight-foreward implementation just for understanding sake would be
	// return this->COMController.getCOME();

	Vector3d real = this->COMController.getCOM();
	Vector3d diff = this->COMController.getCOME() - real;
	return real - diff;
}

/**
	This method is used to compute the velocity of the center of mass of the articulated figure.
*/
Vector3d Character::getCOMVelocity(){
	return this->COMController.getCOMVelocity();
}

void Character::drawRealCOM(int flags) {
	if(!(flags & SHOW_CENTER_OF_MASS))
		return;

	Vector3d COM = this->COMController.getCOM();

	glPushMatrix();

	glDisable(GL_DEPTH_TEST);
	glColor3ub(255, 0, 0);

	GLUtils::drawSphere(COM, 0.04, 11);

	glEnable(GL_DEPTH_TEST);
	
	glPopMatrix();
}

void Character::drawPerceivedCOM(int flags) {
	if(!(flags & SHOW_CENTER_OF_MASS)) 
		return;

	Vector3d COM = this->COMController.getCOME();

	glPushMatrix();

	glDisable(GL_DEPTH_TEST);
	glColor3ub(128, 0, 0);

	GLUtils::drawSphere(COM, 0.025, 11);

	glEnable(GL_DEPTH_TEST);
	
	glPopMatrix();
}

/**
	this method is used to rotate the character about the vertical axis, so that it's default heading has the value that is given as a parameter
*/
void Character::setHeading(Quaternion heading){
	ReducedCharacterStateArray state;
	getState(&state);
	setHeading(heading, &state);
	setState(&state);
}


/**
	this method is used to rotate the character (well, the character whose state is passed in as a parameter) 
	about the vertical axis, so that it's default heading has the value that is given as a parameter
*/
void Character::setHeading(Quaternion heading, ReducedCharacterStateArray* state, int start){
	ReducedCharacterState chS(state, start);
	Quaternion oldHeading, newHeading, qRoot;
	//get the current root orientation, that contains information regarding the current heading
	qRoot = chS.getOrientation();
	//get the twist about the vertical axis...
	oldHeading = computeHeading(qRoot);
	//now we cancel the initial twist and add a new one of our own choosing
	newHeading = heading * oldHeading.getComplexConjugate();
	//add this component to the root.
	chS.setOrientation(newHeading * qRoot);
	//and also update the root velocity and angular velocity
	chS.setVelocity(newHeading.rotate(chS.getVelocity()));
	chS.setAngularVelocity(newHeading.rotate(chS.getAngularVelocity()));
}

/**
	this method is used to rotate the character (well, the character whose state is passed in as a parameter) 
	about the vertical axis, so that it's default heading has the value that is given as a parameter
*/
void Character::setHeading(double val, ReducedCharacterStateArray* state, int start){
	setHeading(Quaternion::getRotationQuaternion(val, Vector3d(0,1,0)), state, start);
}

/**
	this method is used to rotate the character about the vertical axis, so that it's default heading has the value that is given as a parameter
*/
void Character::setHeading(double val){
	ReducedCharacterStateArray state;
	getState(&state);
	setHeading(Quaternion::getRotationQuaternion(val, Vector3d(0,1,0)), &state);
	setState(&state);
}

/**
	this method is used to rotate the character about the vertical axis, so that it's default heading has the value that is given as a parameter
*/
void Character::recenter(){
	ReducedCharacterStateArray state;
	getState(&state);
	ReducedCharacterState chS(&state);
	Point3d currPos = chS.getPosition();
	currPos.x = currPos.z = 0;
	chS.setPosition(currPos);
	setState(&state);
}

/**
	this method is used to return the current heading of the character
*/
Quaternion Character::getHeading(){
	//get the current root orientation, that contains information regarding the current heading and retrieve the twist about the vertical axis
	return computeHeading(root->getOrientation());
}

/**
	this method is used to read the reduced state of the character from the file
*/
void Character::loadReducedStateFromFile(char* fName){
	ReducedCharacterStateArray state;
	readReducedStateFromFile(fName, &state);
	setState(&state);
}

/**
	this method is used to read the reduced state of the character from the file, into the array passed in as a parameter. The
	state of the character is not modified
*/
void Character::readReducedStateFromFile(char* fName, ReducedCharacterStateArray* state){
	// Update joint order
	if (fName == NULL)
		throwError("cannot write to a file whose name is NULL!");

	int start = state->size();

	FILE* fp = fopen(fName, "r");
	if (fp == NULL)
		throwError("cannot open the file \'%s\' for reading...", fName);

	double temp1, temp2, temp3, temp4;

	char line[100];

	//read the heading first...
	double heading;
	readValidLine(line, fp);
	sscanf(line, "%lf", &heading);
	
	readValidLine(line, fp);
	sscanf(line, "%lf %lf %lf", &temp1, &temp2, &temp3);
	state->push_back(temp1);
	state->push_back(temp2);
	state->push_back(temp3);
	readValidLine(line, fp);
	sscanf(line, "%lf %lf %lf %lf", &temp1, &temp2, &temp3, &temp4);
	state->push_back(temp1);
	state->push_back(temp2);
	state->push_back(temp3);
	state->push_back(temp4);
	readValidLine(line, fp);
	sscanf(line, "%lf %lf %lf", &temp1, &temp2, &temp3);
	state->push_back(temp1);
	state->push_back(temp2);
	state->push_back(temp3);
	readValidLine(line, fp);
	sscanf(line, "%lf %lf %lf", &temp1, &temp2, &temp3);
	state->push_back(temp1);
	state->push_back(temp2);
	state->push_back(temp3);

	for (uint i=0;i<joints.size();i++){
		readValidLine(line, fp);
		sscanf(line, "%lf %lf %lf %lf", &temp1, &temp2, &temp3, &temp4);
		state->push_back(temp1);
		state->push_back(temp2);
		state->push_back(temp3);
		state->push_back(temp4);
		readValidLine(line, fp);
		sscanf(line, "%lf %lf %lf", &temp1, &temp2, &temp3);
		state->push_back(temp1);
		state->push_back(temp2);
		state->push_back(temp3);
	}

	//now set the heading...
	setHeading(Quaternion::getRotationQuaternion(heading, PhysicsGlobals::up), state, start);

	fclose(fp);
}

/**
	this method is used to write the reduced state of the character to a file
*/
void Character::saveReducedStateToFile(char* fName, ReducedCharacterStateArray& state){
	// Update joint order
	updateJointOrdering();

	if (fName == NULL)
		throwError("cannot write to a file whose name is NULL!");

	FILE* fp = fopen(fName, "w");
	if (fp == NULL)
		throwError("cannot open the file \'%s\' for writing...", fName);

	//retrieve the current heading, write it to file, and then set a zero heading for the state
	double heading = getHeadingAngle();
	setHeading(Quaternion::getRotationQuaternion(0, PhysicsGlobals::up), &state);

	fprintf(fp, "# order is:\n# Heading\n# Position\n# Orientation\n# Velocity\n# AngularVelocity\n\n# Relative Orientation\n# Relative Angular Velocity\n#----------------\n\n# Heading\n%lf\n\n# Root(%s)\n", heading, root->name);
	fprintf(fp, "%lf %lf %lf\n", state[0], state[1], state[2]);
	fprintf(fp, "%lf %lf %lf %lf\n", state[3], state[4], state[5],state[6]);
	fprintf(fp, "%lf %lf %lf\n", state[7], state[8], state[9]);
	fprintf(fp, "%lf %lf %lf\n\n", state[10], state[11], state[12]);

	for (uint i=0;i<joints.size();i++){
		fprintf(fp, "# %s\n", joints[jointOrder[i]]->name);
		fprintf(fp, "%lf %lf %lf %lf\n", state[13+7*i+0], state[13+7*i+1], state[13+7*i+2],state[13+7*i+3]);
		fprintf(fp, "%lf %lf %lf\n", state[13+7*i+4], state[13+7*i+5], state[13+7*i+6]);
		fprintf(fp, "\n");
	}
	fclose(fp);
}

/**
	this method is used to write the reduced state of the character to the file
*/
void Character::saveReducedStateToFile(char* fName){
	ReducedCharacterStateArray state;
	getState(&state);

	saveReducedStateToFile(fName, state);
}
	
/**
	HACK!
*/
void Character::updateJointOrdering(){
	if( jointOrder.size() == joints.size() ) 
		return; // HACK assume ordering is ok
	jointOrder.clear();

	if (!root)
		return;
	DynamicArray<ArticulatedRigidBody*> bodies;
	bodies.push_back(root);

	int currentBody = 0;

	while ((uint)currentBody<bodies.size()){
		//add all the children joints to the list
		for (int i=0;i<bodies[currentBody]->getChildJointCount();i++){
			Joint *j = bodies[currentBody]->getChildJoint(i);
			jointOrder.push_back( getJointIndex(j->getName()) );
			bodies.push_back(bodies[currentBody]->getChildJoint(i)->getChild());
		}
		currentBody++;
	}

	reverseJointOrder.resize( jointOrder.size() );
	for( uint i=0; i < jointOrder.size(); ++i )
		reverseJointOrder[jointOrder[i]] = i;

}