import time


class COMRecorder(object):
	"""

	Records a series of centre of mass positions.

	"""

	def __init__(self, cop):

		self.samples = []
		self.cop = cop


	def bind_listeners(self, fp):

		fp.forces_after_calibration.add_listener(self.on_update)


	def on_update(self, fac):

		cop = (self.cop.center[0], self.cop.center[1])

		self.samples.append((cop, time.time()))