
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 19, 2016

## ------------------------------------------------------------------------



from plugin.calibration.affine import Affine
import unittest

class TestAffine(unittest.TestCase):

	def test_identity(self):

		x = Affine()

		assert x.process(-13) == -13

	def test_simple_calibration(self):

		x = Affine()

		assert x.process(5) == 5

		x.setZero(5)
		x.setOne(10)

		assert x.process(15) == 2

	def test_persistence(self):

		x = Affine()

		x.process(10)
		x.setZeroLast()

		assert x.process(10) == 0

		x.process(20)
		x.setOneLast()

		assert x.process(20) == 1