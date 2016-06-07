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

Vector3d CentreOfMass::getPerceivedCOM(void) {
	return this->getRealCOM();
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