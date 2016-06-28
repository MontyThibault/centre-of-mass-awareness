from plugin.calibration.affine import Affine
import unittest

class TestAffine(unittest.TestCase):
	def test_calibrate_single_number(self):

		x = Affine()

		assert x.process(5) == 5

		x.setZero()
		x.setOne(10)

		assert x.process(15) == 2

	def test_save_single_calibration(self):

		x = Affine()
		x.offset = 10

		x.name = 'test'
		x.save()
		x.offset = 15
		x.load()

		assert x.offset == 10

		x.delete()