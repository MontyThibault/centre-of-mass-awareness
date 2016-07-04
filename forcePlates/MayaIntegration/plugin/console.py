import threading
import multiprocessing
import sys
import io


class StreamRedirect(io.IOBase):

	maya_out = sys.stdout
	shell_out = ExternalStream()

	def __init__(self, thread_state_object):
		pass

	def write(self, message):

		threading.currentThread()




class ExternalStream(io.IOBase):

	def write(self):
		
		# Send to interpreter process



def spawn_interactive_console():

	multiprocessing.Process(target = f)


	import code

	console = code.InteractiveConsole()
	console.interact()




threading.currentThread()



################

