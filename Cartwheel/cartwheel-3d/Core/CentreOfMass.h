#pragma once

#include "Physics/ArticulatedFigure.h"

class RigidBodyError {

public:
	RigidBodyError();
	RigidBodyError(ArticulatedRigidBody *arb);

	ArticulatedRigidBody *arb;

	/* 
	 * The naming convention methodNameE signifies that measurement with artificial 
	 * applied. This error can depend on randomness, so may be sampled multiple times.
	 */
	double getMassE();
	Vector3d getCMPositionE();
};


class CentreOfMass {

public:

	CentreOfMass();
	CentreOfMass(ArticulatedFigure *af);

	~CentreOfMass(void);

	Vector3d getRealCOM(void);
	Vector3d getRealCOMVelocity(void);

	Vector3d getPerceivedCOM(void);

	void step(void);	

private:
	/*
	 * Reference to the articulated figure of the character.
	 */
	ArticulatedFigure *af;

	/*
	 * All articulated rigid bodies of the figure are wrapped in an error class
	 * in which we add our modifications.
	 *
	 * TODO: Extend this to joints
	 */
	DynamicArray<RigidBodyError> rbe;

	/*
	 * The RigidBodyError wrapper of this->af->root.
	 */
	RigidBodyError root;

	/*
	 * Current centre of mass; stays persistent between calls to getPerceivedCOM().
	 */
	Vector3d currentCOM;

	/*
	 * Updates this->rbe to wrap around the rigid bodies already present in the articulated figure.
	 */
	void setRBE(void);

	/*
	 * A centre-of-mass correction function that determines the path of a random walk 
	 */
	double g(Vector3d p);
	
	/*
	 * Returns the gradient of g.
	 */
	Vector3d gGrad(Vector3d p);

};