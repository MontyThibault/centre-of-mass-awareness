#pragma once

#include "Physics/ArticulatedFigure.h"

class CentreOfMass {

public:
	CentreOfMass();
	CentreOfMass(ArticulatedFigure *af);

	~CentreOfMass(void);

	Vector3d getRealCOM(void);
	Vector3d getRealCOMVelocity(void);

	Vector3d getPerceivedCOM(void);

private:
	ArticulatedFigure *af;

	Vector3d currentCOM;
	

	/*
	 * A centre-of-mass correction function that determines the path of a random walk 
	 */
	double g(Vector3d p);
	
	/*
	 * Returns the gradient of g.
	 */
	Vector3d gGrad(Vector3d p);

};