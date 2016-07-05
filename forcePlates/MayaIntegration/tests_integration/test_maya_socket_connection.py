from plugin.maya_socket_connection import maya


def test_send():

	# Will raise error if, for instance, Maya is not loaded.

	maya.send('print "Test"')


def test_recieve():

	maya.send('file -q -sn')
	maya.recv(1024)