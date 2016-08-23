
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 23, 2016

## ------------------------------------------------------------------------



from plugin.gridcalibration.generator import Generator
import unittest


class TestGenerator(unittest.TestCase):

	def setUp(self):

		self.mg = MockGrid()
		self.mfp = MockForcePlate()

		self.g = Generator(self.mg)


	def test_weighted_average_single(self):

		l = [((0, 0), 1)]

		assert self.g._weightedAverage(l) == (0, 0)


	def test_weighted_average_multiple(self):

		l = [
			((0, 0), 1),
			((1, 1), 1)
		]

		assert self.g._weightedAverage(l) == (0.5, 0.5)

	def test_weighted_average_lopsided(self):

		l = [
			((0, 0), 0),
			((1, 1), 1)
		]

		assert self.g._weightedAverage(l) == (1, 1)


	def test_center(self):

		f = [1, 1, 1, 1]

		assert self.g._center(f) == (0, 0)


	def test_take_sample(self):

		self.g.take_sample(self.mfp.forces_after_calibration.get())

		assert self.g.samples[0] == ((-10, -10), (0, 0), 4)


class MockGrid(object):
	
	def __init__(self, *args):
		
		self.currentPoint = (-10, -10)

	def corners(self):

		return [
			(-10, -10),
			(-10, 10),
			(10, 10),
			(10, -10)
		]



def _instance(cls):
	return cls()

class MockForcePlate(object):
	
	def __init__(self):

		self._center = (0, 0)

	@_instance
	class forces_after_calibration(object):

		def get(self):
			return [1, 1, 1, 1]

	def center(self):

		return self._center