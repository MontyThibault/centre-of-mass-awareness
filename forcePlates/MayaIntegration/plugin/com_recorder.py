from collections import deque
from threading import Lock
import time


class COMRecorder(object):
	"""

	Records a series of centre of mass positions.

	"""

	def __init__(self, sensor):

		self.samples = []
		self.drawable_samples = deque([], 200)

		self.sample_lock = Lock()

		self.sensor = sensor


	def bind_listeners(self):

		self.sensor.centre_of_pressure.add_listener(self.on_update)


	def on_update(self, cop):

		cop_tup = (cop[0], cop[1])
		tup = (cop_tup, self.sensor.total_force ,time.time())


		# Protects against mutation during iteration errors with the PyGame thread

		with self.sample_lock:

			self.samples.append(tup)
			self.drawable_samples.append(tup)