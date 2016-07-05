import plugin.maya_socket_connection as msc
import pytest

def test_send_and_recv():

	# Will raise error if, for instance, Maya is not loaded and the connection
	# could not be established.

	msc.maya.send('print "Test"')
	msc.maya.recv(1024)


def test_error_raise():

	with pytest.raises(NameError):
		msc.send_and_recv('fhgkld')


def test_send_function():

	def f():

		# This is now called from within Maya

		return 42


	assert msc.call_func(f) == 42


def test_function_raise():

	def f():
		fggfdsfd

	with pytest.raises(NameError):
		msc.call_func(f)


def test_import_maya_environment():

	def f():

		import maya.cmds
		import maya.utils
		import maya.OpenMaya

	msc.call_func(f)


def test_call_maya_function():

	def f():

		import maya.cmds

		return maya.cmds.about(version = True)

	assert msc.call_func(f) >= 2016