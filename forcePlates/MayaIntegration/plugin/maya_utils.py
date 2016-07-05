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

	import maya.cmds

	print forces