from ctypes import *


GAIN = 4000
EXCITATION_VOLTAGE = 10

SENSITIVITY_TERMS = {

	'M5237': [0.67887, 0.68076, 0.16426, 38.72479, 38.66569, 27.58195]

}


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

		# Dirty ctypes list for device interface
		self._measurements_c = (c_float * 6)()

		# Good Python list for public interface
		self.measurements = [0, 0, 0, 0, 0, 0]


		# mac = measurements after calibration
		self.mac = [0, 0, 0, 0, 0, 0]

		self.centre_of_pressure = [0, 0]


	def update(self):

		self._update_measurements()
		self._update_centre_of_pressure()


	def _update_measurements(self):

		ptr = cast(self._measurements_c, c_voidp).value
		for (i, channel) in enumerate(self.channels):
			
			slot = cast(ptr + (4 * i), POINTER(c_float))
			self.device.AioSingleAiEx(c_short(channel), slot)


			val = self._measurements_c[i]

			self.measurements[i] = val


			# Calibration equation defined on page 10 of "Single Element 
			# Multi-Component Transducer" instructions, model MC2.5A-1K-6278.

			self.mac[i] = val / (EXCITATION_VOLTAGE * SENSITIVITY_TERMS['M5237'][i] * GAIN * 1e-6)


	def _update_centre_of_pressure(self):

		_, _, F_z, M_x, M_y, _ = self.mac 


		# Given that the force is straight downwards (might not be the case with dynamics)
		# we arrive at these equations and rearrange them:

		# M_x = F_z * y
		# M_y = F_z * x

		try: 

			print M_y, F_z

			self.centre_of_pressure[0] = 100 * M_y / F_z
			self.centre_of_pressure[1] = 100 * M_x / F_z

		except ZeroDivisionError:

			pass