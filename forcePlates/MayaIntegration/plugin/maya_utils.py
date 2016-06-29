"""

Useful abstractions for common operations with the Maya API.

"""


def createLocatorTransformPair(cmds, name):

	if not cmds.objExists(name):
		cmds.createNode( "transform", name = name )
		cmds.createNode( "locator", parent = name )


def moveObject(cmds, p, name):

	cmds.move(p[0], p[1], p[2], name)


def objectLocation(cmds, name):

	cmds.xform(name, ws = True, t = 1, q = 1)