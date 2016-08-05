

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

		tf = tf / full_weight

		for i in range(3):

			self.color[i] = 255 - (self.base_color[i] * tf)
			self.color[i] = int(self.color[i])
			self.color[i] = min(255, max(0, self.color[i]))