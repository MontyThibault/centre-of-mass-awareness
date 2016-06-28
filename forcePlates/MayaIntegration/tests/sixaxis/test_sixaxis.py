from plugin.sixaxis.sixaxis import SixAxis
import unittest


class TestSixAxis(unittest.TestCase):

	class FauxDevice(object):
		def Init():
			pass

		def AioSetAiRangeAll(range):
			pass

		def AioSingleAiEx(deviceID, c_channel, slot):

			from random import random
			slot.contents = c_float(random() + c_channel.value)

	def setUp(self):

		self.device = self.FauxDevice()
		self.channels = [6, 7, 8, 9, 10, 11]
		

	def test_create_and_process_six_axis(self):

		rock = SixAxis(self.device, self.channels, "test", False)
		rock.updateMeasurements()
		
		assert rock.forces == rock.measurements[:3]

	