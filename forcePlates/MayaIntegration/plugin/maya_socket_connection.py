# MEL
# commandPort -name 12345 -sourceType Python -pickleOutput;


import socket
import pickle

_PORT = 12345


maya = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
maya.connect(("127.0.0.1", _PORT))


def recv_pickled(*args):

	val = maya.recv(*args)

	# something to do with pickler

	return val