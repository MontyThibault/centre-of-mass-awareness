#include "CentreOfMass.h"

CentreOfMass::CentreOfMass() {
}

CentreOfMass::CentreOfMass(ArticulatedFigure *af) {
	this->af = af;
}

CentreOfMass::~CentreOfMass(void) {
}

Vector3d CentreOfMass::getRealCOM(void) {
	
	ArticulatedRigidBody *root = this->af->root;
	DynamicArray<Joint*> joints = this->af->joints;

	Vector3d COM = Vector3d(root->getCMPosition()) * root->getMass();
	double curMass = root->getMass();
	double totalMass = curMass;
	for (uint i=0; i <joints.size(); i++){
		curMass = joints[i]->child->getMass();
		totalMass += curMass;
		COM.addScaledVector(joints[i]->child->getCMPosition() , curMass);
	}

	COM /= totalMass;

	return COM;

}

Vector3d CentreOfMass::getRealCOMVelocity(void) {
	
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

Vector3d CentreOfMass::getPerceivedCOM(void) {

	// if(this->currentCOM.length() == 0.0)
	//	this->currentCOM = this->getRealCOM();

	this->currentCOM -= this->gGrad(this->currentCOM) * 0.001;

	return this->currentCOM;

}

double CentreOfMass::g(Vector3d p) {
	Vector3d real = this->getRealCOM();

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