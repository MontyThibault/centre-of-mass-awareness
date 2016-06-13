#include "CentreOfMass.h"

RigidBodyError::RigidBodyError(void) {
	this->arb = 0;
}

RigidBodyError::RigidBodyError(ArticulatedRigidBody *arb) {
	this->arb = arb;
}

double RigidBodyError::getMassE() {
	return this->arb->getMass();
}

Vector3d RigidBodyError::getCMPositionE() {
	return this->arb->getCMPosition();
}

CentreOfMass::CentreOfMass() {
}

CentreOfMass::CentreOfMass(ArticulatedFigure *af) {
	this->af = af;
}

CentreOfMass::~CentreOfMass(void) {
}

/*
 * This method sets the array of RigidBodyErrors corresponding to the array of ArticulatedRigidBodies
 * and same for the root. The section after the if-statements should run only once.
 */
void CentreOfMass::setRBE(void) {
	// If root pointer is already set
	if(this->root.arb) 
		return;

	// If the articulated figure's root pointer is not yet set
	if(this->af->root == 0)
		return;


	for(unsigned i = 0; i < this->af->arbs.size(); i++) {
		ArticulatedRigidBody *arb = this->af->arbs[i];

		this->rbe.push_back(RigidBodyError(arb));
	}

	this->root = RigidBodyError(this->af->root);

	this->currentCOM = this->getCOM();
}

/*
 * This method computes the true centre of mass of the character.
 */
Vector3d CentreOfMass::getCOM(void) {
	this->setRBE();

	ArticulatedRigidBody *root = this->root.arb;

	Vector3d COM = Vector3d(root->getCMPosition()) * root->getMass();
	double curMass = root->getMass();
	double totalMass = curMass;

	DynamicArray<ArticulatedRigidBody*> arbs = this->af->arbs;

	for (uint i=0; i < arbs.size(); i++){
		curMass = arbs[i]->getMass();
		totalMass += curMass;
		COM.addScaledVector(arbs[i]->getCMPosition() , curMass);
	}

	COM /= totalMass;

	return COM;
}

/*
 * This is called internally by the animation system. It is not called in 
 * consistent intervals and probably should not be changed. (See ::step)
 */
Vector3d CentreOfMass::getCOME(void) {
	return this->currentCOM;
}

/*
 * This method computes the true centre of velocity of the character.
 */
Vector3d CentreOfMass::getCOMVelocity(void) {
	
	ArticulatedRigidBody *root = this->af->root;
	DynamicArray<Joint*> joints = this->af->joints;

	Vector3d COMVel = Vector3d(root->getCMVelocity()) * root->getMass();
	double curMass = root->getMass();
	double totalMass = curMass;
	for (uint i=0; i <joints.size(); i++){
		curMass = joints[i]->child->getMass();
		totalMass += curMass;
		COMVel.addScaledVector(joints[i]->child->getCMVelocity() , curMass);
	}

	COMVel /= totalMass;

	return COMVel;
}

Vector3d CentreOfMass::getCOMVelocityE(void) {
	return this->getCOMVelocity();
}


// Each joint <-> rigid body needs an uncertainty measure on its CM position and velocity (not angular)

// Returns a random number between -1 and 1
double fRand() {
	double r = (double) rand() / RAND_MAX;
	return r * 2 - 1;
}


/*
 * This method is called by the Python program on every frame draw. This is 
 * where we should do updates.
 */
void CentreOfMass::step(void) {

	// 30 fps
	double timeDiff = 1.0 / 30.0;

	Vector3d grad = this->gGrad(this->currentCOM);
	
	// NOT isotropic!
	// Only an approximation of randomness for now
	Vector3d randVec = Vector3d(fRand(), (fRand() + 1) / 2, fRand());

	grad += randVec;

	this->currentCOM -= grad * 0.01;

	////////////////////////////////

	// Number of samples
	int n = 5;

	Vector3d accumulator = Vector3d();
	for(int i = 0; i < n; i++) {
		// accumulator += 
	}

	/*
	this->setRBE();

	ArticulatedRigidBody *root = this->root.arb;

	Vector3d COM = Vector3d(root->getCMPosition()) * root->getMass();
	double curMass = root->getMass();
	double totalMass = curMass;

	DynamicArray<ArticulatedRigidBody*> arbs = this->af->arbs;

	for (uint i=0; i < arbs.size(); i++){
		curMass = arbs[i]->getMass();
		totalMass += curMass;
		COM.addScaledVector(arbs[i]->getCMPosition() , curMass);
	}

	COM /= totalMass;

	return COM;
	*/
}

double CentreOfMass::g(Vector3d p) {
	Vector3d real = this->getCOM();

	return (real - p).length();
}

Vector3d CentreOfMass::gGrad(Vector3d p) {
	// We implement a simple gradient approximation using very small differences.
	double epsilon = pow(10.0, -10.0);

	Vector3d v;
	double gp = this->g(p);

	v.x = this->g(p + Vector3d(epsilon, 0, 0)) - gp;
	v.y = this->g(p + Vector3d(0, epsilon, 0)) - gp;
	v.z = this->g(p + Vector3d(0, 0, epsilon)) - gp;

	v /= epsilon;

	return v;
}