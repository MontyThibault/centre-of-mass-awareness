
def safe_module_wrapper(f):

	def g(*args, **kwargs):

		"""

		This decorator will wrap the given function in a pseudo-non-persistent environment 
		such that any imported modules will be reloaded when the script is recalled.

		"""


		import sys


		# Enable stacktrace error catching in Python scripts

		import maya.cmds as cmds

		cmds.stackTrace(state = True)



		# Clean up all imported modules in case the script was ran before
		# (The Maya python environment is persistent)

		# Important!!!

		glob = globals()

		if 'EXISTING_MODULES' in glob:


			for key in sys.modules.keys():

				if key not in glob['EXISTING_MODULES']:

					del sys.modules[key]

		else:

			glob['EXISTING_MODULES'] = sys.modules.keys()



		# Main

		try:

			return f(*args, **kwargs)

		except Exception, e:

			import traceback
			traceback.print_exc()



	return g