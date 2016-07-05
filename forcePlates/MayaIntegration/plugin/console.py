import code
import threading

class Console(threading.Thread):

	def __init__(self, local_vars):
		
		threading.Thread.__init__(self)

		self.local_vars = local_vars


	def run(self):

		ic = code.InteractiveConsole(self.local_vars)
		ic.interact()