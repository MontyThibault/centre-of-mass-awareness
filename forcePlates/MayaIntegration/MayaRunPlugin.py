# Put me as a button on the shelf

import sys


# Replace your absolute path here

sys.path.append('C:/Users/Monty/Desktop/COMAwareness/forcePlates/MayaIntegration')


# Enable stacktrace error catching in Python scripts

import maya.cmds
cmds.stackTrace(state = True)



existing = sys.modules.keys()



# Main

try:

	from plugin.main import main

	main()

except Exception, e:

	import traceback
	traceback.print_exc()




# Clean up all imported modules in case the script was ran before
# (The Maya python environment is persistent)

# Important!!!

for key in sys.modules.keys():

	if key not in existing:

		del sys.modules[key]