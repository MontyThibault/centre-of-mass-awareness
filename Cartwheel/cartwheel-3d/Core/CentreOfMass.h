#pragma once

#include "Physics/ArticulatedFigure.h"

class RigidBodyError {

public:
	RigidBodyError();
	RigidBodyError(ArticulatedRigidBody *arb);

	ArticulatedRigidBody *arb;

	/* 
	 * The naming convention methodNameE signifies that measurement with artificial error
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

	Vector3d getCOM(void);
	Vector3d getCOMVelocity(void);

	/* 
	 * The naming convention methodNameE signifies that measurement with artificial error
	 * applied. This error can depend on randomness, so may be sampled multiple times.
	 */
	Vector3d getCOME(void);
	Vector3d getCOMVelocityE(void);

	void step(void);	
	void stepDraw(const int samples);

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
	 * Returns a single random sample of the centre of mass.
	 */
	Vector3d getCOMESample();

	/*
	 * A centre-of-mass correction function that determines the path of a random walk 
	 */
	double g(Vector3d p);
	
	/*
	 * Returns the gradient of g.
	 */
	Vector3d gGrad(Vector3d p);

};