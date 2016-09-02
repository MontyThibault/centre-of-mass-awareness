
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Sep 02, 2016

## ------------------------------------------------------------------------



from plugin.threads.killable_thread import KillableThread


class Generator(object):
	"""

	Generates calibration data.

	"""

	def __init__(self, grid):

		self.grid = grid

		self.samples = []


	# TODO: Take all of these weighted sums/averages/samples/etc. and derivations thereof
	# and make into a module.

	@staticmethod
	def _weightedAverage(list_):
		"""

		Averages weighted lists of the form [(point, weight), (point, weight)] ...

		"""

		accum = [0, 0]

		for point, weight in list_:

			accum[0] += point[0] * weight
			accum[1] += point[1] * weight

		totalWeight = sum([weight for point, weight in list_])


		if totalWeight == 0:
			
			return (0, 0)


		accum[0] /= float(totalWeight)
		accum[1] /= float(totalWeight)

		return (accum[0], accum[1])


	def _center(self, forces):
		"""
		Ex.

		>>> corners = [(0, 0), (0, 1)]
		>>> forces = [1, 1]

		>>> _center(points, forces)
		(0, 0.5)

		"""
		
		zipped = zip(self.grid.corners(), forces)
		return self._weightedAverage(zipped)


	def take_sample(self, forces_after_calibration):
		"""

		Takes and stores a single sample from the force plate.

		"""

		f = forces_after_calibration

		# Note
		# Sample = (source_point, measured_point, total_forces)
		sample = (self.grid.currentPoint, self._center(f), sum(f))

		self.samples.append(sample)



# class SamplingThread(KillableThread):
# 	"""

# 	Periodically take samples with a generator.

# 	"""

# 	def __init__(self, gen):
# 		KillableThread.__init__(self)

# 		self.fps = 5
# 		self.gen = gen


# 	def loop(self):
		
# 		self.gen.take_sample()