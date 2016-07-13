import code
import threading

class ConsoleThread(threading.Thread):
	"""

	Runs a console on top of the original executing program.

	"""

	def __init__(self, local_vars):
		
		threading.Thread.__init__(self)

		self.local_vars = local_vars

		self.console_started_lock = threading.Lock()
		self.console_started_lock.acquire()


	def run(self):

		self.ic = code.InteractiveConsole(self.local_vars)

		self.console_started_lock.release()

		self.ic.interact()


	def kill(self):

		with self.console_started_lock:

			try:	

				# This will raise SystemExit, which will propegate to the
				# current thread as well unless we catch it!

				self.ic.push('quit()')

			except:
				pass