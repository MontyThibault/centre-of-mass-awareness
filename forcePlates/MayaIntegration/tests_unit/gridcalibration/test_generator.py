from plugin.gridcalibration.generator import Generator
import unittest


class TestGenerator(unittest.TestCase):

	def setUp(self):

		self.mg = MockGrid()
		self.mfp = MockForcePlate()

		self.g = Generator(self.mg, self.mfp)


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

		self.g.take_sample()

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


class MockForcePlate(object):
	
	def __init__(self):

		self._center = (0, 0)
		self.forces = [1, 1, 1, 1]


	def center(self):

		return self._center