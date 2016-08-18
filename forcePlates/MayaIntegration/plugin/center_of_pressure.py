
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 18, 2016

## ------------------------------------------------------------------------



MIN = -1000
MAX = 1000


class CenterOfPressure(object):
	"""

	Interpolates between grid corners by weighted forces.

	"""

	def __init__(self, grid):
		self.grid = grid
		self.center = [0, 0]


	def bind_listeners(self, fp):

		fp.forces_after_calibration.add_listener(self.on_update)


	def on_update(self, forces_after_calibration):

		fac = forces_after_calibration

		zipped = zip(self.grid.corners(), fac)

		center = self._weightedSum(zipped)

		self.center[0] = center[0]
		self.center[1] = center[1]

		self.limits()


	def limits(self):

		if self.center[0] < MIN:
			self.center[0] = MIN

		elif self.center[0] > MAX:
			self.center[0] = MAX


		if self.center[1] < MIN:
			self.center[1] = MIN

		elif self.center[1] > MAX:
			self.center[1] = MAX



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