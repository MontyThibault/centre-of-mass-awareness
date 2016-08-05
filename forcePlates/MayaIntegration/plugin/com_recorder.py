from collections import deque
from threading import Lock
import time


class COMRecorder(object):
	"""

	Records a series of centre of mass positions.

	"""

	def __init__(self, cop):

		self.samples = []
		self.drawable_samples = deque([], 120)

		self.sample_lock = Lock()

		self.cop = cop


	def bind_listeners(self, fp):

		fp.forces_after_calibration.add_listener(self.on_update)


	def on_update(self, fac):

		cop = (self.cop[0], self.cop[1])
		t = (cop, time.time())


		# Protects against mutation during iteration errors with the PyGame thread
		
		with self.sample_lock:

			self.samples.append(t)
			self.drawable_samples.appendleft(t)