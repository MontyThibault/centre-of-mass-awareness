# Put me as a button on the shelf

import sys


# Replace your absolute path here

sys.path.append('C:/Users/Monty/Desktop/COMAwareness/forcePlates/MayaIntegration')


def f():

	# Import inside of a function to prevent polluting the global namespace

	import plugin
	
	plugin.main()


f()