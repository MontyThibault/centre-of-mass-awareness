

device = AIODevice(b'AIO001')

# See Contec API-PAC(W32) CAIO reference manual

device.Init()

device.AioSetAiInputMethod(c_short(0))
device.AioSetAiRangeAll(aio.PM25)





import time

while True:

	sa.update()
	print [round(m, 3) for m in sa.mac]
	time.sleep(1.0 / 60)