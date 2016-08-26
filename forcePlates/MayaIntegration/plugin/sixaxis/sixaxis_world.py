
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 26, 2016

## ------------------------------------------------------------------------



from plugin.observable import Observable


class SixAxisWorld(object):
	"""

	Keeps track of a single real-world position and orientation of a sensor and
	its coordinate system.

	"""


	def __init__(self, sensor, mat = None):
		"""

		@argument mat - A 3x3 matrix to transform the vector [x; y; 1] into world coordinates.
		The matrix [[1, 0, 0], [0, 1, 0], [0, 0, 1]] corresponds to the identity.

		"""

		self.sensor = sensor

		if mat == 'i':
			self.mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
		elif mat == 'z':
			self.mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		else:
			self.mat = mat

		self.total_force = 0
		self.centre_of_pressure = Observable([0, 0])

		sensor.centre_of_pressure.add_listener(self.on_update)


	def on_update(self, cop):
		"""

		On update of underlying sensor, apply transformations, then set own cop.

		"""

		self.total_force = self.sensor.total_force


		cop3 = 1

		new_cop = (


			cop[0] * self.mat[0][0] + cop[1] * self.mat[0][1] + cop3 * self.mat[0][2],
			cop[0] * self.mat[1][0] + cop[1] * self.mat[1][1] + cop3 * self.mat[1][2],
			cop[0] * self.mat[2][0] + cop[1] * self.mat[2][1] + cop3 * self.mat[2][2]

		)


		l = self.centre_of_pressure.get()
		l[0] = new_cop[0]
		l[1] = new_cop[1]

		self.centre_of_pressure.notify_all()


	def set_x(self, x):

		self.mat[0][2] = x
		

	def set_y(self, y):

		self.mat[1][2] = y