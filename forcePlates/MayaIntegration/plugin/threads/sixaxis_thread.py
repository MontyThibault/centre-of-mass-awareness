
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 18, 2016

## ------------------------------------------------------------------------



from killable_thread import KillableThread

from plugin.world_sensor_config import WorldSensorConfiguration


class SixAxisThread(KillableThread):
	
	def __init__(self):
		KillableThread.__init__(self)

		self.fps = 100

		self.world = WorldSensorConfiguration()


	def loop(self):
		
		self.world.update()

		