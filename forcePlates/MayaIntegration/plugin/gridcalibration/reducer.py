
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 23, 2016

## ------------------------------------------------------------------------



class Reducer(object):
	"""

	This class takes large collections of samples and reduces them to a more manageable
	size for realtime error correction.

	"""

	def partitionBySource(self, samples):
		""" 

		Breaks the given samples up into equivalence classes of the first element of the 
		tuple (the source point). This is the list of partitions.

		Ex.
		>>> samples = [
				((0, 0), (0, 0), 1),
				((1, 1), (0, 0), 1),
				((1, 1), (0, 1), 1)
			]

		>>> partitioned = self.r.partition(samples)

		[
			[((0, 0), (0, 0), 1)],
			[((1, 1), (0, 0), 1), ((1, 1), (0, 1), 1)]
		]

		"""
		
		partitions = dict()

		for sample in samples:


			source = sample[0]

			if source not in partitions.keys():
				partitions[source] = []

			partitions[source].append(sample)

		return partitions.values()


	def merge(self, partitions):
		"""

		Merges the list of partitions into a single-level-deep list of samples. Effectively
		the inverse of Reducer.partitionBy_().

		"""
		
		samples = []

		for partition in partitions:
			for sample in partition:
				samples.append(sample)

		return samples

	
	def _partitionByForce(self, samples, interval):
		""" 

		Breaks the given list of samples up into partitions of equal spacing as dictated
		by the interval argument. The partitions are dictated by intervals [min, max).

		Ex.

		>>> samples = [
				((0, 0), (0, 0), 0),
				((1, 1), (0, 0), 1)
			]

		>>> self.r._partitionByForce(samples, 1)
		
		[
			[((0, 0), (0, 0), 0)],
			[((1, 1), (0, 0), 1)]
		]

		"""

		partitions = dict()

		for sample in samples:

			force = sample[2]

			# Scale the force such that integral values correspond to boundary points
			scaled = force / interval
			int_ = int(scaled)

			# We then use int_ as an index into the dict
			if int_ not in partitions.keys():
				partitions[int_] = []


			partitions[int_].append(sample)


		return partitions.values()


	def reduce(self, samples, interval):
		""" 

		This method takes a single paritition and merges the samples (taking the average) 
		such that there is only one per interval. The dimension in question is the force
		axis of each sample (third component of the tuple). The force axis is split up such 
		that no two samples of the returned partition are within `interval` of each other.

		"""

		partitions = self._partitionByForce(samples, interval)

		return [
			self._averageSamples(partition)
			for partition in partitions
		]



	def filter_min_max(self, samples, min_, max_):
		"""

		Filters samples such that the force axis lies on [min, max].

		"""
		
		return filter(lambda s: s[2] <= max_ and s[2] >= min_, samples)





	# TODO: eliminate redundancy with this class and sampler.py
	# These methods are untested as they are already done in sampler.py

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