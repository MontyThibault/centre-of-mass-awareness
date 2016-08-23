
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 23, 2016

## ------------------------------------------------------------------------



from plugin.gridcalibration.grid import Grid
import unittest

class GridTest(unittest.TestCase):

	def test_iterate_simple_grid(self):

		x = Grid(10, 10, 10, 10)

		assert x.currentPoint == (-10, -10)
		assert x.hasMorePoints == True

		for _ in range(9):
			x.next()

		assert x.currentPoint == (-10, 10)
		assert x.hasMorePoints == True

		for _ in range(1000):
			x.next()

		assert x.currentPoint == (10, 10)
		assert x.hasMorePoints == False

		x.reset()

		assert x.currentPoint == (-10, -10)
		assert x.hasMorePoints == True

	def test_simple_contains(self):

		x = Grid(10, 5, 20, 10)

		assert x.contains((10, 5))
		assert x.contains((-3, -2))
		assert not x.contains((0.3, 3))
		assert not x.contains((11, 0))


	def test_simple_square(self):

		# Unit divisions
		x = Grid(10, 10, 20, 20)

		p = (0.5, 0.5)

		assert (1, 1) in x.square(p)
		assert (0, 0) in x.square(p)
		assert (0, 1) in x.square(p)
		assert (0, 1) in x.square(p)


		p = (6.321, -7.466)

		assert (6, -8) in x.square(p)
		assert (7, -8) in x.square(p)
		assert (6, -7) in x.square(p)
		assert (7, -7) in x.square(p)

	def test_weighted_square(self):

		x = Grid(10, 10, 1, 1)

		p = (0, 0)

		assert x.weightedSquare(p)[0][1] == 0.25

		p = (10, 10)

		assert ((10, 10), 1) in x.weightedSquare(p)

		p = (4.4324, -8.54323)
		ws = x.weightedSquare(p)

		assert sum([w for (p, w) in ws]) == 1


	def test_points(self):

		x = Grid(1, 1, 2, 2)

		p = x.points()

		assert (-1, -1) in p
		assert (1, -1) in p
		assert (1, 1) in p

		assert not (0, 0) in p

		assert len(p) == 4