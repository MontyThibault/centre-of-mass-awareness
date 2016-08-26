
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 26, 2016

## ------------------------------------------------------------------------



# from plugin.sixaxis.sixaxis_calibration import SixAxisCalibrationMatrix
# import unittest

# class TestSixAxisCalibration(unittest.TestCase):

# 	def test_calibrate_matrix_test_and_save(self):

# 		x = SixAxisCalibrationMatrix()

# 		assert x.process([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

# 		x.matrix[2][3] = 1
# 		assert x.process([0, 0, 0, 1, 0, 0]) == [0, 0, 1, 1, 0, 0]

# 		x.name = 'test'
# 		x.save()

# 		x.matrix[2][3] = 0

# 		x.load()
# 		assert x.process([0, 0, 0, 1, 0, 0]) == [0, 0, 1, 1, 0, 0]

# 		x.delete()

# 	def test_insert_factory_six_axis_calibrations(self):
# 		SixAxisCalibrationMatrix.insert_factory_six_axis_calibrations()