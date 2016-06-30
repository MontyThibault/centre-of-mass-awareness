# Put me as a button on the shelf

import sys

# Replace your absolute path here

sys.path.append('C:/Users/Monty/Desktop/COMAwareness/forcePlates/MayaIntegration')


# For pytest dependency

sys.path.append('C:/Miniconda2/Lib/site-packages')


# Enable stacktrace error catching in Python scripts

import maya.cmds
import maya.utils

cmds.stackTrace(state = True)




# Clean up all imported modules in case the script was ran before
# (The Maya python environment is persistent)

# Important!!!


if 'existing' in vars():


	for key in sys.modules.keys():

		if key not in existing:

			del sys.modules[key]



existing = sys.modules.keys()



# Main

try:

	from tests_integration.main import main

	main()

except Exception, e:

	import traceback
	traceback.print_exc()