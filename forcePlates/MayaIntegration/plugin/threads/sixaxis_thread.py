from killable_thread import KillableThread

from plugin.world_sensor_config import WorldSensorConfiguration


class SixAxisThread(KillableThread):
	
	def __init__(self):
		KillableThread.__init__(self)

		self.fps = 100

		self.world = WorldSensorConfiguration()


	def loop(self):
		
		self.world.update()

		