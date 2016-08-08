from plugin.DLL_wrappers.AIO import *
from plugin.sixaxis.sixaxis import SixAxis
from plugin.sixaxis.sixaxis_world import SixAxisWorld
from plugin.observable import Observable

from ctypes import c_short



class WorldSensorConfiguration(object):
	"""

	Keeps track of real-world positions and orientations of sensors alongside their
	coordinate systems.

	"""

	def __init__(self):
		

		### Hard-coded configuration follows



		# Distance between two adjacent sensors on the same plate (m)

		sensor_diff = 7.68e-2


		# Distance between plates (m)

		stance_width = 15e-2



		device0 = AIODevice(b'AIO000')
		device0.Init()

		device0.AioSetAiInputMethod(c_short(0))
		device0.AioSetAiRangeAll(aio.PM25)


		device1 = AIODevice(b'AIO001')
		device1.Init()

		device1.AioSetAiInputMethod(c_short(0))
		device1.AioSetAiRangeAll(aio.PM25)


		self.M5170 = SixAxis(device0, [0, 1, 2, 3, 4, 5], 'M5170')
		self.M5238 = SixAxis(device0, [6, 7, 8, 9, 10, 11], 'M5238')
		self.M5239 = SixAxis(device0, [12, 13, 14, 15, 16, 17], 'M5239')
		self.M5240 = SixAxis(device0, [18, 19, 20, 21, 22, 23], 'M5240')


		self.sensors = [self.M5238, self.M5239, self.M5170, self.M5240]


		self.world_sensors = [SixAxisWorld(s) for s in self.sensors]

		


		###

		self.total_force = 0
		self.centre_of_pressure = Observable([0, 0])


		for s in self.sensors:

			s.update()
			s.set_zero()



	def update(self):

		for s in self.sensors:

			s.update()



		# Weighted sum of world coordinates of sensors

		accumulator = [0, 0]
		force_accum = 0

		for w in self.world_sensors:

			l = w.centre_of_pressure.get()
			f = w.sensor.total_force

			accumulator[0] += l[0] * f
			accumulator[1] += l[1] * f

			force_accum += f


		self.total_force = force_accum


		# Division by zero

		if force_accum == 0:
			return


		accumulator[0] /= force_accum
		accumulator[1] /= force_accum


		cop = self.centre_of_pressure.get()
		cop[0] = accumulator[0]
		cop[1] = accumulator[1]

		self.centre_of_pressure.notify_all()