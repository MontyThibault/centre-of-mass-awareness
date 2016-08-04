from plugin.DLL_wrappers.AIO import *
from plugin.sixaxis.sixaxis import SixAxis

device = AIODevice(b'AIO000')

device.Init()
device.AioSetAiRangeAll(aio.PM10)


sa = SixAxis(device, [6, 7, 8, 9, 10, 11])