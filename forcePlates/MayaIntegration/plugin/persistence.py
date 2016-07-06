import atexit
import pickle
import os

_filepath = os.path.dirname(os.path.realpath(__file__)) + "/.persistence.pickle"


# Startup

try:
	with open(_filepath, 'rb') as f:
		old_vals = pickle.load(f)
except:
	old_vals = dict()


used_val_pairs = []


def define_persistent(domain, varname):
	"""

	Defines a variable to be persistent.

	Usage:

	>>> define_persisent('x', locals())
	>>> x
	None

	>>> x = 10

	(Reload console)

	>>> define_persisent('x', locals())
	>>> assert x == 10

	"""


	if varname in old_vals:

		v = old_vals[varname]

	else:

		v = 0


	# Set value

	domain[varname] = v


	# Keep the (domain, name) pair so that we can still access and save
	# the values on exit.

	used_val_pairs.append((domain, varname))


def _exit():

	new_vals = dict()

	print used_val_pairs


	# Get the current values for all of the persistent variables

	for domain, varname in used_val_pairs:
		new_vals[varname] = domain[varname]


	old_vals.update(new_vals)

	print _filepath, old_vals
	
	with open(_filepath, 'wb') as f:
		pickle.dump(f, old_vals)


atexit.register(_exit)