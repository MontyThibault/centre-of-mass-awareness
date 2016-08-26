
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 26, 2016

## ------------------------------------------------------------------------



from plugin.gridcalibration.processor import Processor
import unittest


def instance(cls):
	return cls()


class ProcessorTest(unittest.TestCase):


	# Mimic sampler interface

	@instance
	class sampler(object):

		def identity(*args):

			# Identity sample

			return ((0, 0), (0, 0), 1)


		def off_by_one(*args):

			# Offset by (1, 1)

			return ((0, 0), (1, 1), 1)

		def square_identities(self, point, force, radius):

			# Identities for each point on a unit square

			return {
				(0, 0): ((0, 0), (0, 0), 1),
				(1, 0): ((1, 0), (1, 0), 1),
				(0, 1): ((0, 1), (0, 1), 1),
				(1, 1): ((1, 1), (1, 1), 1)
			}[point]

		def square_off_by_one(self, point, force, radius):

			# Offset by (1, 1) for each point on a unit square

			return {
				(0, 0): ((0, 0), (1, 1), 1),
				(1, 0): ((1, 0), (2, 1), 1),
				(0, 1): ((0, 1), (1, 2), 1),
				(1, 1): ((1, 1), (2, 2), 1)
			}[point]

		def square_mixture(self, point, force, radius):

			# Offset by (1, 1) for the (0, 0) point; the rest are identities

			return {
				(0, 0): ((0, 0), (1, 1), 1),
				(1, 0): ((1, 0), (1, 0), 1),
				(0, 1): ((0, 1), (0, 1), 1),
				(1, 1): ((1, 1), (1, 1), 1)
			}[point]



	# Mimic grid interface

	@instance
	class grid(object):
		def weightedSquare(*args):

			# This is a unit square where the point lies in the exact centre.

			return [((0, 0), 0.25), ((1, 0), 0.25), ((0, 1), 0.25), ((1, 1), 0.25)]




	# Tests begin

	def test_simple_sample_process(self):

		sample =  ((10, -3), (5, 3), 40)

		assert Processor._processPointWithSample((5, 3), sample) == (10, -3)

	def test_equal_weighted_sum(self):

		points = [
			((0, 0), 1),
			((0, 1), 1),
			((1, 0), 1),
			((1, 1), 1)
		]

		assert Processor._weightedSum(points) == (0.5, 0.5)


	def test_lopsided_weighted_sum(self):

		points = [
			((0, 0), 1),
			((0, 1), 0),
			((1, 0), 0),
			((1, 1), 0)
		]

		assert Processor._weightedSum(points) == (0, 0)


	def test_single_point_identity(self):

		x = Processor(self.sampler.identity, self.grid)

		assert x.process((0, 0), 1) == (0, 0)
		assert x.process((32, -3), 0.1) == (32, -3)


	def test_single_point_offset(self):

		x = Processor(self.sampler.off_by_one, self.grid)

		assert x.process((0, 0), 1) == (-1, -1)
		assert x.process((32, -3), 0.1) == (31, -4)


	def test_square_identity(self):

		x = Processor(self.sampler.square_identities, self.grid)

		assert x.process((0.5, 0.5), 1) == (0.5, 0.5)


	def test_square_offset(self):

		x = Processor(self.sampler.square_off_by_one, self.grid)

		assert x.process((0.5, 0.5), 1) == (-0.5, -0.5)