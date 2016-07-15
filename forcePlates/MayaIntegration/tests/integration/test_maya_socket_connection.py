import plugin.maya_socket_connection as msc
import pytest

def test_send_and_recv():

	# Will raise error if, for instance, Maya is not loaded and the connection
	# could not be established.

	assert msc.send_and_recv('5') == 5


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


def test_function_with_args():

	complex_object = {
		'x': [5, 'Hello', {
			'y': set(['world', True, 9.99])
		}]
	}

	def f(*args):
		return args

	assert msc.call_func(f, complex_object, 42) == (complex_object, 42)


def test_import_maya_environment():

	def f():

		import maya.cmds
		import maya.utils
		import maya.OpenMaya

		import plugin

	msc.call_func(f)


def test_call_maya_function():

	def f():

		import maya.cmds

		return maya.cmds.about(version = True)

	assert msc.call_func(f) >= 2016


def test_maya_correct_scene_loaded():

	def f():

		import maya.cmds as c

		assert c.file(q = True, ns = True) == "SensorScene"

	msc.call_func(f)