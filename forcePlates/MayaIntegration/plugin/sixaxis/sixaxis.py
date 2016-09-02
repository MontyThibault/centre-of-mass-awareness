
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Sep 02, 2016

## ------------------------------------------------------------------------



from plugin.observable import Observable
from ctypes import *


# Middle set of jumpers on the AMTI MSA-6 board

GAIN = 1000


# Top set of jumpers on the AMTI MSA-6 board


EXCITATION_VOLTAGE = 5


# Sourced from orange AMTI reference manuals

SENSITIVITY_TERMS = {
	
	'M5119': [0.67622, 0.67497, 0.16651, 38.93765, 37.99575, 28.19990],
	'M5170': [0.35517, 0.35401, 0.08807, 20.54487, 20.45965, 13.74638],
	'M5237': [0.67887, 0.68076, 0.16426, 38.72479, 38.66569, 27.58195],
	'M5238': [0.33738, 0.33820, 0.08474, 19.75560, 19.83606, 13.16477],
	'M5239': [0.34821, 0.34677, 0.08705, 20.45356, 20.43072, 13.53383],
	'M5240': [0.34302, 0.34242, 0.08554, 20.18649, 20.12639, 13.68040]

}

AXIS_ORIGIN = {
	
	# in mm

	'M5119': [-0.09745, 0.693442, 38.32484],
	'M5170': [0.118819, 0.342403, 29.35282],
	'M5237': [-0.1659, -0.00759, -50.2849],
	'M5238': [-0.4428, -0.0631, -29.2569],
	'M5239': [-0.0630, -0.2750, -29.1772],
	'M5240': [-0.2998, -0.3227, -29.2305]

}


class SixAxis(object):
	def __init__(self, device, channels, code):
		""" 

		One single six-axis sensor.

		Device: An instance of PAIO.AIODevice()
		Channels: The channel indicies for the sensor in the following order:
			[forceX, forceY, forceZ, torqueX, torqueY, torqueZ] 

		"""

		self.device = device
		self.channels = channels
		self.code = code

		# Dirty ctypes list for device interface
		self._measurements_c = (c_float * 6)()

		# Good Python list for public interface
		self.measurements = [0, 0, 0, 0, 0, 0]

		self.zeroes = [0, 0, 0, 0, 0, 0]


		# It is always assumed that total_force is updated alongside centre_of_pressure,
		# and that it is ready to go whenever the observer is notified.

		self.total_force = 0
		self.centre_of_pressure = Observable([0, 0])


	def update(self):

		old_measurement = self.measurements[:]

		self._update_measurements()


		for old, new in zip(old_measurement, self.measurements):


			# Only update everything if there was a change

			if old != new:
				
				self._update_centre_of_pressure()
				return

		print "skipped"
		


	def _update_measurements(self):

		ptr = cast(self._measurements_c, c_voidp).value
		for (i, channel) in enumerate(self.channels):
			
			slot = cast(ptr + (4 * i), POINTER(c_float))
			self.device.AioSingleAiEx(c_short(channel), slot)


			val = self._measurements_c[i]

			self.measurements[i] = val


	def _update_centre_of_pressure(self):

		zipped = zip(self.measurements, self.zeroes)

		after_zeroing = [m - z for m, z in zipped] 
		
		
		after_calibration = []
		
		for i, x in enumerate(after_zeroing):

			# Calibration equation defined on page 10 of "Single Element 
			# Multi-Component Transducer" instructions, model MC2.5A-1K-6278.

			v = x / (EXCITATION_VOLTAGE * SENSITIVITY_TERMS[self.code][i] * GAIN * 1e-6)
			after_calibration.append(v)


		F_x, F_y, F_z, M_x, M_y, M_z = after_calibration

		# Given that the force is straight downwards (might not be the case with dynamics)
		# we arrive at these equations and rearrange them:

		# M_x = F_z * y
		# M_y = F_z * x


		self.total_force = F_z


		if F_z == 0:
			return

		cop = self.centre_of_pressure.get()


		scale = 0.5

		cop[0] = scale * M_y / F_z
		cop[1] = scale * M_x / F_z

		self.centre_of_pressure.notify_all()


	def set_zero(self):

		for i in range(6):
			self.zeroes[i] = self.measurements[i]