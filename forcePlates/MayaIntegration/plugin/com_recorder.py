from collections import deque
from threading import Lock
import time


class COMRecorder(object):
	"""

	Records a series of centre of mass positions.

	"""

	def __init__(self, cop):

		self.samples = []
		self.drawable_samples = deque([], 200)

		self.sample_lock = Lock()

		self.cop = cop


	def bind_listeners(self):

		self.cop.add_listener(self.on_update)


	def on_update(self, cop):

		cop_tup = (cop[0], cop[1])
		tup = (cop_tup, time.time())


		# Protects against mutation during iteration errors with the PyGame thread

		with self.sample_lock:

			self.samples.append(tup)
			self.drawable_samples.append(tup)