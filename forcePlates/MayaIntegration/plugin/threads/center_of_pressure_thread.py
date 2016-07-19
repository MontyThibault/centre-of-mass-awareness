# Depreciated


from killable_thread import KillableThread


class CenterOfPressureThread(KillableThread):
	""" 

	Keep forces syncronized.

	"""
	
	def __init__(self, fp, grid):
		KillableThread.__init__(self)

		self.fps = 60

		self.fp = fp
		self.grid = grid

		self.center_of_pressure = [0, 0]


	@staticmethod
	def _weightedSum(points):
		""" Weighted sum with a list of points of the form [(point, weight), (point, weight)]..."""

		accumulator = [0, 0]

		for point, weight in points:
			accumulator[0] += point[0] * weight
			accumulator[1] += point[1] * weight

		totalWeight = sum([weight for _, weight in points])

		if totalWeight == 0:
			return (0, 0)

		accumulator[0] /= float(totalWeight)
		accumulator[1] /= float(totalWeight)

		return (accumulator[0], accumulator[1])


	def loop(self):

		fac = self.fp.forces_after_calibration.get()
		
		zipped = zip(self.grid.corners(), fac)

		center = self._weightedSum(zipped)

		self.center_of_pressure[0] = center[0]
		self.center_of_pressure[1] = center[1]