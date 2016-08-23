
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 23, 2016

## ------------------------------------------------------------------------



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