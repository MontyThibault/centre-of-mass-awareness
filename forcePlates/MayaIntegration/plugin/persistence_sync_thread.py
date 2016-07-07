from killable_thread import KillableThread
import shelve


class PersistenceSyncThread(KillableThread):
	"""

	Automatic object persistence using Python's shelve library. Objects are saved
	once every loop.

	"""

	def __init__(self, path):

		# Save once every three seconds

		self.fps = 1.0 / 3

		self.objs = shelve.open(path)


	def loop(self):

		self.objs.sync()