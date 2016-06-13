#include "CentreOfMass.h"
#include <math.h>

// Returns a random number in [0, 1)
double fRand() {
	double r = (double) rand() / RAND_MAX;
}

// Box-muller transform
double gaussian(double mu, double sigma) {
	const double epsilon = 0.00000000001;
	
	double u1, u2;
	do {
		u1 = fRand();
		u2 = fRand();
	} while(u1 <= epsilon);

	double z0 = sqrt(-2 * log(u1)) * cos(2.0 * 3.14159265 * u2);

	return mu + (z0 * sigma);
}

RigidBodyError::RigidBodyError(void) {
	this->arb = 0;
}

RigidBodyError::RigidBodyError(ArticulatedRigidBody *arb) {
	this->arb = arb;
}

/* 
 * This method returns the mass of the rigid body with a small degree of error.
 */
double RigidBodyError::getMassE() {

	double mass = this->arb->getMass();
	double error = 0.3;
	
	return gaussian(mass, error);
}

/* 
 * This method returns the position of the rigid body with error proportional to its speed
 */
Vector3d RigidBodyError::getCMPositionE() {
	Vector3d cm = this->arb->getCMPosition(),
		v = this->arb->getCMVelocity();

	double error = 0.5; // +- 50% of body velocity

	return cm + (v * gaussian(0, error));
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
 * consistent intervals and probably should not be changed. (See CentreOfMass::step)
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

Vector3d CentreOfMass::getCOMESample() {
	this->setRBE();

	RigidBodyError root = this->root;

	double curMass = root.getMassE();
	Vector3d COM = Vector3d(root.getCMPositionE()) * curMass;
	
	double totalMass = curMass;

	DynamicArray<RigidBodyError> rbe = this->rbe;

	for (uint i=0; i < rbe.size(); i++){
		curMass = rbe[i].getMassE();
		totalMass += curMass;
		COM.addScaledVector(rbe[i].getCMPositionE() , curMass);
	}

	COM /= totalMass;

	return COM;
}


/*
 * This method is called by the Python program on every frame draw. This is 
 * where we should do updates.
 */
void CentreOfMass::step(void) {

	/*

	// 30 fps
	double timeDiff = 1.0 / 30.0;

	Vector3d grad = this->gGrad(this->currentCOM);
	
	// NOT isotropic!
	// Only an approximation of randomness for now
	Vector3d randVec = Vector3d(fRand(), (fRand() + 1) / 2, fRand());

	grad += randVec;

	this->currentCOM -= grad * 0.01;

	*/

	////////////////////////////////

	// Simple monte-carlo integration
	const int samples = 10;
	Vector3d accumulator;
	
	for(uint i = 0; i < samples; i++) {
		accumulator += this->getCOMESample();
	}

	accumulator /= (double) samples;

	this->currentCOM = accumulator;


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