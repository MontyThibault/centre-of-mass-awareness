import os
import subprocess


def test_maya_environment():
	""" 

	If this fails, the tests are not running from within the Maya environment. You
	should use the MayaRunIntegrationTests.py script, and/or exclude the integration
	tests directroy for unit tests.

	"""

	import maya.cmds
	import maya.utils
	import maya.OpenMaya



def test_find_project_path_environment():
	"""

	If this fails, the project path is not set on the system and thus the Maya script 
	does not know where to look for the plugin.

	"""

	import plugin


def test_import_pytest():
	"""

	This should never fail, since we need pytest to run this test, but it may be useful
	in case the user attempts to run the test via cmd without pytest on the PATH.

	"""

	import pytest