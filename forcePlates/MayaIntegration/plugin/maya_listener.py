# Should not be used

import threading
import maya_socket_connection as msc

class ListenerThread(threading.Thread):

	def run(self):

		while True:

			print msc.recv_pickled(1024)