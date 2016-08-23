
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 23, 2016

## ------------------------------------------------------------------------



class Processor(object):
	""" Processes points & applies corrections. Used in conjunction with a sampler. """

	def __init__(self, sampler, grid):
		self.sampler = sampler
		self.grid = grid


	@staticmethod
	def _processPointWithSample(point, sample):
		""" Returns the point-to-be-processed with simple offset applied by the sample. """

		(actual, measured, force) = sample

		measuredToActual = (actual[0] - measured[0], actual[1] - measured[1])

		return (point[0] + measuredToActual[0], point[1] + measuredToActual[1])

	@staticmethod
	def _weightedSum(points):
		""" Weighted sum with a list of points of the form [(point, weight), (point, weight)]..."""

		accumulator = [0, 0]

		for point, weight in points:
			accumulator[0] += point[0] * weight
			accumulator[1] += point[1] * weight

		totalWeight = sum([weight for _, weight in points])

		accumulator[0] /= float(totalWeight)
		accumulator[1] /= float(totalWeight)

		return (accumulator[0], accumulator[1])


	def process(self, point, force):
		""" Processes a given point & force and applies correction based on the library
		of samples. """


		ws = self.grid.weightedSquare(point)

		weightedArray = []

		for vert, weight in ws:

			sample = self.sampler(vert, force, 10)
			afterCorrection = self._processPointWithSample(point, sample)

			weightedArray.append((afterCorrection, weight))


		return self._weightedSum(weightedArray)