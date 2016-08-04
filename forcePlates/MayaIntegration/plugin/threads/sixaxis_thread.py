from killable_thread import KillableThread
from plugin.DLL_wrappers.AIO import *
from plugin.sixaxis.sixaxis import SixAxis

from ctypes import c_short


class SixAxisThread(KillableThread):
	
	def __init__(self):
		KillableThread.__init__(self)

		self.fps = 24


		device = AIODevice(b'AIO001')
		device.Init()

		device.AioSetAiInputMethod(c_short(0))
		device.AioSetAiRangeAll(aio.PM25)

		self.M5237 = SixAxis(device, [6, 7, 8, 9, 10, 11])



	def loop(self):

		self.M5237.update()