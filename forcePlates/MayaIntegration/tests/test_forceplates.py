from plugin.forceplates import ForcePlates
import unittest

class TestForcePlates(unittest.TestCase):


	class Affine(object):

		def process(self, x):
			return x

		def setZero(self, x):
			pass

		def setOne(self, x):
			pass


	class LabProUSB(object):
		pass


	def setUp(self):
		pass




	def tearDown(self):
		pass





	def test_inject_dependencies(self):

		f = ForcePlates
		# f.inject(self.calibration, self.labprousb)

		# assert self.calibrations == 4
		# assert self.started == True


	def test(self):
		pass