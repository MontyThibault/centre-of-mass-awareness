
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 23, 2016

## ------------------------------------------------------------------------



class Sampler(object):
	""" Given a constant grid point, this class controls the choice and manipulation of 
	samples from calibration data. Note all sample methods shares a common interface. """

	def __init__(self, samples):
		self.samples = samples

	def closest(self, point, force, radius = 0):
		""" Returns the closest sample on the given point. """
		
		best = None
		diff = -1

		for sample in self.samples:

			if sample[0] != point:
				continue

			currentDiff = abs(force - sample[2])

			if diff == -1 or currentDiff < diff:
				best = sample
				diff = currentDiff

		if best:
			return best
		else:

			# Assume identity for grid points with no samples
			return (point, point, force)


	def simpleComposite(self, point, force, radius):
		""" Average all samples within radius. """
		
		samples = self._samplesWithinRadius(point, force, radius)
		return self._averageSamples(samples)

	def distanceComposite(self, point, force, radius):
		""" Weighted average of all samples within radius, by distance from epicentre. """

		weightedSamples = self._weightedSamplesWithinRadius(point, force, radius)
		return self._averageWeightedSamples(weightedSamples)


	def _samplesWithinRadius(self, point, force, radius):
		""" Returns a list of samples for the specified point within the radius
		of the given force. """
		
		samples = []

		for sample in self.samples:

			if sample[0] != point:
				continue

			diff = abs(force - sample[2])
			if diff <= radius:

				samples.append(sample)

		return samples

	def _weightedSamplesWithinRadius(self, point, force, radius):
		""" The distance metric in this instance is defined to be a linear curve with
		spot-on sample corresponding to a value of one, sample exactly on the radius
		corresponding to a value of zero. This way we can easily take a weighted
		average. """

		samples = []

		for sample in self.samples:

			if sample[0] != point:
				continue

			diff = abs(force - sample[2])
			if diff <= radius:

				# Normalized linear function
				weight = (radius - diff) / radius

				samples.append((sample, weight))

		return samples


	@staticmethod
	def _averageSamples(samples):

		if len(samples) == 0:

			return ((0, 0), (0, 0), 0)


		acc = [0, 0, 0, 0, 0]

		for sample in samples:

			acc[0] += sample[0][0]
			acc[1] += sample[0][1]
			acc[2] += sample[1][0]
			acc[3] += sample[1][1]
			acc[4] += sample[2]

		acc = [x / len(samples) for x in acc]

		return ((acc[0], acc[1]), (acc[2], acc[3]), acc[4])


	@staticmethod
	def _averageWeightedSamples(weightedSamples):
		
		if len(weightedSamples) == 0:

			return ((0, 0), (0, 0), 0)



		acc = [0, 0, 0, 0, 0]
		totalWeight = 0

		for sample, weight in weightedSamples:

			acc[0] += sample[0][0] * weight
			acc[1] += sample[0][1] * weight
			acc[2] += sample[1][0] * weight
			acc[3] += sample[1][1] * weight
			acc[4] += sample[2] * weight

			totalWeight += weight

		acc = [x / totalWeight for x in acc]

		return ((acc[0], acc[1]), (acc[2], acc[3]), acc[4])