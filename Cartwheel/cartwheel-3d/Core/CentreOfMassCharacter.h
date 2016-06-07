#pragma once

#include "Character.h"

/*
 * Computes character's centre of mass from a weighted random walk algorithm.
*/
class CentreOfMassCharacter : public Character {

public:
	CentreOfMassCharacter();
	virtual ~CentreOfMassCharacter(void);

private:
	Vector3d _COM;
	Vector3d _COMVelocity;
};