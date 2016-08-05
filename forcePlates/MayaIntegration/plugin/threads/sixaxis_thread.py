from killable_thread import KillableThread
from plugin.DLL_wrappers.AIO import *
from plugin.sixaxis.sixaxis import SixAxis

from ctypes import c_short


class SixAxisThread(KillableThread):
	
	def __init__(self):
		KillableThread.__init__(self)

		self.fps = 120


		device0 = AIODevice(b'AIO000')
		device0.Init()

		device0.AioSetAiInputMethod(c_short(0))
		device0.AioSetAiRangeAll(aio.PM10)


		device1 = AIODevice(b'AIO001')
		device1.Init()

		device1.AioSetAiInputMethod(c_short(0))
		device1.AioSetAiRangeAll(aio.PM10)

		

		self.M5237 = SixAxis(device1, [6, 7, 8, 9, 10, 11], 'M5237')
		self.M5238 = SixAxis(device0, [6, 7, 8, 9, 10, 11], 'M5238')
		self.M5170 = SixAxis(device0, [0, 1, 2, 3, 4, 5], 'M5170')
		self.M5240 = SixAxis(device0, [18, 19, 20, 21, 22, 23], 'M5240')


		self.all_sensors = [self.M5237, self.M5238, self.M5170, self.M5240]

		for s in self.all_sensors:

			s.update()
			s.set_zero()



	def loop(self):
		
		for s in self.all_sensors:

			s.update()
