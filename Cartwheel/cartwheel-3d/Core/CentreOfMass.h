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

	Vector3d COMOffset;

private:
	ArticulatedFigure *af;

};