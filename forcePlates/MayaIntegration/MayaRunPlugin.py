# Put me as a button on the shelf

import sys


# Replace your absolute path here

sys.path.append('C:/Users/Monty/Desktop/COMAwareness/forcePlates/MayaIntegration')


# Enable stacktrace error catching in Python scripts

import maya.cmds
cmds.stackTrace(state = True)



# Force refresh on all imported modules in case the script was ran before
# (The Maya python environment is persistent)

# Important!!!

for mod in sys.modules.keys():

	if mod.startswith('plugin'):
		del sys.modules[mod]


# Main

from plugin.main import main
main()