from killable_thread import KillableThread
import shelve


class PersistenceSyncThread(KillableThread):
	"""

	Automatic object persistence using Python's shelve library. Objects are saved
	once every loop.

	You have to use caution when 

	"""

	def __init__(self, path):
		KillableThread.__init__(self)

		# Save once every three seconds

		self.fps = 1.0 / 3

		self.objs = shelve.open(path, writeback = True)


	def loop(self):

		self.objs.sync()


	def kill(self):
		KillableThread.kill(self)

		self.objs.close()