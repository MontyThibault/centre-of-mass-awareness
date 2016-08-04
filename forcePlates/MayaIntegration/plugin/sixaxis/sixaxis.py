### Decomissioned

from ctypes import *

class SixAxis(object):
	def __init__(self, device, channels):
		""" 

		Maps a single six-axis sensor to a Maya transform 

		Device: An instance of PAIO.AIODevice()
		Channels: The channel indicies for the sensor in the following order:
			[forceX, forceY, forceZ, torqueX, torqueY, torqueZ] 

		"""

		self.device = device
		self.channels = channels

		# Dirty ctypes list
		self._measurements_c = (c_float * 6)()

		# Good Python list for public interface
		self.measurements = [0, 0, 0, 0, 0, 0]


	def update(self):

		ptr = cast(self._measurements_c, c_voidp).value
		for (i, channel) in enumerate(self.channels):
			
			slot = cast(ptr + (4 * i), POINTER(c_float))
			self.device.AioSingleAiEx(c_short(channel), slot)


		for i in range(6):
			self.measurements[i] = self._measurements_c[i]