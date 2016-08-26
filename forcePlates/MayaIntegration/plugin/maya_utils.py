
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 26, 2016

## ------------------------------------------------------------------------



"""

Useful abstractions for common operations with the Maya API.

"""


def createLocatorTransformPair(name):

	import maya.cmds

	if not cmds.objExists(name):
		cmds.createNode( "transform", name = name )
		cmds.createNode( "locator", parent = name )


def moveObject(p, name):

	import maya.cmds

	cmds.move(p[0], p[1], p[2], name)


def objectLocation(name):

	import maya.cmds

	cmds.xform(name, ws = True, t = 1, q = 1)


def move_markers(forces):

	import maya.cmds as c

	# print forces

	c.xform("plate1", s = [forces[0] * 18 for i in range(3)])
	c.xform("plate2", s = [forces[1] * 18 for i in range(3)])
	c.xform("plate3", s = [forces[2] * 18 for i in range(3)])
	c.xform("plate4", s = [forces[3] * 18 for i in range(3)])


	vecs = []

	for i in range(4):
		vecs.append((
			forces[i], 

			# Get the translation of the current plate in world space
			cmds.xform('plate%s' % (i + 1), ws = True, t = 1, q = 1)
		))

			
	# Interpolate between vectors

	center = [0, 0, 0]
	totalWeight = 0.0

	for (weight, vec) in vecs:

		center = [a + (b * weight) for a, b in zip(center, vec)]
		totalWeight += weight

	if totalWeight == 0:
		return

	center = [ce / totalWeight for ce in center]
	center[1] = 0

	cmds.move(center[0], center[1], center[2], 'center')
	cmds.refresh()