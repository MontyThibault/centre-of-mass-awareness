from killable_thread import KillableThread
from plugin.observable import Observable


class CalibrationProgramThread(KillableThread):
	"""

	This thread is a calibration utility that takes many samples per second,
	and automatically switches through the grid points.

	"""

	def __init__(self, generator):
		KillableThread.__init__(self)

		self.fps = 10
		self.generator = generator

		self.seconds_per_point = 10
		self.seconds_between_points = 5

		self._current_time = 0

		self._currently_sampling = Observable()
		self._currently_sampling.set(False)

		self._time_when_sampling_started = 0
		self._time_when_sampling_stopped = 0

		self.verbose = False

	def loop(self):

		if not self.dead:

			self._current_time += 1.0 / self.fps



		if self._currently_sampling.get():

			self.generator.take_sample()

			
			# Stop sampling after a certain time

			twss = self._time_when_sampling_started

			if self._current_time - twss > self.seconds_per_point:

				if not self.generator.grid.hasMorePoints:

					self.kill()

				self.generator.grid.next()

				self._time_when_sampling_stopped = self._current_time
				self._currently_sampling.set(False)

		else:

			# Start sampling after certain time

			twss = self._time_when_sampling_stopped

			if self._current_time - twss > self.seconds_between_points:

				self._time_when_sampling_started = self._current_time
				self._currently_sampling.set(True)