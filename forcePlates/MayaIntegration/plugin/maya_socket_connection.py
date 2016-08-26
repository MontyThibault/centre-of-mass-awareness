
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 26, 2016

## ------------------------------------------------------------------------



"""

This module established a socket command port session with a running Maya program, and
provides a way to interface very naturally with Maya from within an external Python program.

Note: We must activate a command port before this script will work. Use the MEL command

	commandPort -name ":99" -sourceType "python" -pickleOutput;

"""

import socket
import pickle
import inspect
import textwrap

_PORT = 99


maya = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
maya.connect(("127.0.0.1", _PORT))


def recv_pickled(*args):

	val = maya.recv(*args)

	return pickle.loads(val)


def send_and_recv(str_):

	maya.send(str_)

	recv = recv_pickled(1024)


	# If there was an error, raise it.

	if isinstance(recv, Exception):
		raise recv


	return recv	



def call_func(f, *locals_):
	"""

	Calls a simple function by sending over the source code. A simple function 
	consititutes anything that will run that does not have outside dependencies.

	"""

	# Send the locals over the socket in pickled form, which is then unpickled when
	# the code is executed.

	body = textwrap.dedent("""

	import pickle

	locals_ = %s
	globals()["unpickled"] = pickle.loads(locals_)

	""" % repr(pickle.dumps(locals_)))
	

	# Add the function definition
	
	body += textwrap.dedent(inspect.getsource(f))


	# Bind the function to the global namespace

	body += '\nglobals()["func"] = %s\n' % f.__name__


	send_and_recv(body)


	# Call the function with the unpickled args

	return send_and_recv('globals()["func"](*globals()["unpickled"])')

