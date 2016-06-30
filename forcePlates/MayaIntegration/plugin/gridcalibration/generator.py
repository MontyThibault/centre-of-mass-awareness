class Generator(object):
	"""

	Generates calibration data.

	"""

	def __init__(self, grid, forceplates):

		self.grid = grid
		self.fp = forceplates

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

			accum[0] += point[0]
			accum[1] += point[1]

		totalWeight = sum([weight for point, weight in list_])


		accum[0] /= float(totalWeight)
		accum[1] /= float(totalWeight)

		return (accum[0], accum[1])


	def take_sample(self):
		"""
	
		Takes and stores a single sample from the force plate.

		"""

		# Note
		# Sample = (source_point, measured_point, total_forces)
		sample = (self.grid.currentPoint, self.fp.center(), sum(self.fp.forces))

		self.samples.append(sample)