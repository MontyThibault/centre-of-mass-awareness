from plugin.sixaxis.sixaxis_calibration import SixAxisCalibrationMatrix
import unittest

class TestSixAxisCalibration(unittest.TestCase):

	def test_insert_factory_six_axis_calibrations(self):
		SixAxisCalibrationMatrix.insert_factory_six_axis_calibrations()