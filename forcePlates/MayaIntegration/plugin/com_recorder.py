
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Sep 02, 2016

## ------------------------------------------------------------------------



from collections import deque
from threading import Lock
import time


class COMRecorder(object):
	"""

	Records a series of centre of mass positions.

	"""

	def __init__(self, sensor, record_permanent = False):

		self.samples = []
		self.drawable_samples = deque([], 200)

		self.sample_lock = Lock()

		self.sensor = sensor
		self.record_permanent = record_permanent


	def bind_listeners(self):

		self.sensor.centre_of_pressure.add_listener(self.on_update)


	def on_update(self, cop):

		cop_tup = (cop[0], cop[1])
		tup = (cop_tup, self.sensor.total_force, time.time())


		# Protects against mutation during iteration errors with the PyGame thread

		with self.sample_lock:

			if self.record_permanent:
				self.samples.append(tup)
				
			self.drawable_samples.append(tup)