
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Sep 02, 2016

## ------------------------------------------------------------------------



class DynamicColor(object):
	"""

	Changes color based on observer.

	"""

	def __init__(self, sensor, base_color):

		self.color = [0, 0, 0]
		self.base_color = base_color

		self.sensor = sensor

		sensor.centre_of_pressure.add_listener(self.on_update)


	def on_update(self, cop):

		tf = self.sensor.total_force


		# This many newtons until color is fully bright

		full_weight = 350

		tf_rel = tf / full_weight
		tf_rel = min(1, max(0, tf_rel)) # Contrain to [0, 1]

		tf_rel = 1 - tf_rel


		for i in range(3):

			self.color[i] = (255 - self.base_color[i]) * tf_rel + self.base_color[i]
			self.color[i] = int(self.color[i])