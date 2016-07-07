import code
import threading

class ConsoleThread(threading.Thread):
	"""

	Runs a console on top of the original executing program.

	"""

	def __init__(self, local_vars):
		
		threading.Thread.__init__(self)

		self.local_vars = local_vars


	def run(self):

		ic = code.InteractiveConsole(self.local_vars)
		ic.interact()