from plugin.gridcalibration.generator import Generator
import unittest


class TestGenerator(unittest.TestCase):

	def setUp(self):

		self.mg = MockGrid()
		self.mfp = MockForcePlate()

		self.u = Generator(self.mg, self.mfp)


	def test_weighted_average_single(self):

		l = [((0, 0), 1)]

		assert self.u._weightedAverage(l) == (0, 0)


	def test_weighted_average_multiple(self):

		l = [
			((0, 0), 1),
			((1, 1), 1)
		]

		assert self.u._weightedAverage(l) == (0.5, 0.5)

	def test_weighted_average_lopsided(self):

		l = [
			((0, 0), 0),
			((1, 1), 1)
		]

		assert self.u._weightedAverage(l) == (1, 1)


	def test_take_sample(self):

		self.mfp._center = (12, 34)
		self.u.take_sample()

		assert self.u.samples[0] == ((-10, -10), (12, 34), 4)


class MockGrid(object):
	
	def __init__(self, *args):
		
		self.currentPoint = (-10, -10)



class MockForcePlate(object):
	
	def __init__(self):

		self._center = (0, 0)
		self.forces = [1, 1, 1, 1]


	def center(self):

		return self._center