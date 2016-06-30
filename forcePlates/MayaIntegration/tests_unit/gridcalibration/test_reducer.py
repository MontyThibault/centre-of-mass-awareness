from plugin.gridcalibration.reducer import Reducer
import unittest

class TestReducer(unittest.TestCase):

	def setUp(self):
		self.r = Reducer()

	def test_partitions_of_one_sample(self):

		samples = [
			((0, 0), (0, 0), 1)
		]

		filtered = self.r.partitionBySource(samples)

		assert filtered == [
			[((0, 0), (0, 0), 1)]
		]



	# This is duplicated in the docstring (bad?)

	def test_partitions_of_two_samples(self):

		samples = [
			((0, 0), (0, 0), 1),
			((1, 1), (0, 0), 1),
			((1, 1), (0, 1), 1)
		]

		partitioned = self.r.partitionBySource(samples)

		assert partitioned == [
			[((0, 0), (0, 0), 1)],
			[((1, 1), (0, 0), 1), ((1, 1), (0, 1), 1)]
		]

	def test_merging_of_partitions(self):

		partitions = [
			[((0, 0), (0, 0), 1)],
			[((1, 1), (0, 0), 1)]
		]

		samples = self.r.merge(partitions)

		assert samples == [
			((0, 0), (0, 0), 1),
			((1, 1), (0, 0), 1)
		]

	def test_partition_by_force_of_two_samples(self):

		samples = [
			((0, 0), (0, 0), 0),
			((1, 1), (0, 0), 1)
		]

		p = self.r._partitionByForce(samples, 1)

		assert p == [
			[((0, 0), (0, 0), 0)],
			[((1, 1), (0, 0), 1)]
		]

	def test_reduction_of_one_sample(self):

		partition = [
			((0, 0), (0, 0), 1)
		]

		p = self.r.reduce(partition, 1)

		assert p == partition

	def test_reduction_of_two_of_the_same_samples(self):

		partition = [
			((0, 0), (0, 0), 1),
			((0, 0), (0, 0), 1)
		]

		p = self.r.reduce(partition, 1)

		assert p == [
			((0, 0), (0, 0), 1)
		]

	def test_reduction_of_two_different_samples(self):


		partition = [
			((0, 0), (0, 0), 0),
			((0, 0), (0, 0), 1)
		]

		
		# As the radius is smaller than the distance between samples,
		# we expect them not to be merged.

		p = self.r.reduce(partition, 0.9)

		assert p == partition


	def test_reduction_averages_two_samples_on_same_point(self):

		partition = [
			((0, 0), (32, 0), 1),
			((0, 0), (0, -32), 1)
		]

		p = self.r.reduce(partition, 1)

		assert p == [
			((0, 0), (16, -16), 1)
		]

	def test_filter_min_max(self):

		partition = [
			((0, 0), (0, 0), 1),
			((0, 3), (0, 0), 3),
			((0, -2), (0, 0), -2)
		]

		p = self.r.filter_min_max(partition, 0, 2)

		assert p == [((0, 0), (0, 0), 1)]