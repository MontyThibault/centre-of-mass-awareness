
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 26, 2016

## ------------------------------------------------------------------------



# from plugin.sixaxis.sixaxis import SixAxis
# import ctypes
# import unittest


# class TestSixAxis(unittest.TestCase):

# 	class FauxDevice(object):
# 		def Init():
# 			pass

# 		def AioSetAiRangeAll(range):
# 			pass

# 		def AioSingleAiEx(deviceID, c_channel, slot):

# 			from random import random
# 			slot.contents = ctypes.c_float(random() + c_channel.value)

# 	def setUp(self):

# 		self.device = self.FauxDevice()
# 		self.channels = [6, 7, 8, 9, 10, 11]
		

# 	def test_create_and_process_six_axis(self):

# 		rock = SixAxis(self.device, self.channels)
# 		rock.updateMeasurements()
		
# 		assert rock.forces == rock.measurements[:3]

# 	