# MEL
# commandPort -name 12345 -sourceType Python -pickleOutput;

# commandPort -name ":99" -sourceType "python" -pickleOutput;


import socket
import pickle
import inspect

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



def call_func(f):

	# Send the function definition
	
	body = inspect.getsource(f)


	# Bind the function to the global namespace

	body += '\nglobals()["func"] = %s\n' % f.__name__


	send_and_recv(body)


	# Call the function

	return send_and_recv('globals()["func"]()')