"""

Utilities for interfacing pygame & the existing sampling data structure.

"""

import time


class PyGameInterface(object):

	def draw(self, width, height, screen, pygame):
		"""
		
		Perform draw functions on each frame.

		"""

		pass



class PointVisualizer(PyGameInterface):

	def __init__(self, point, grid_visualizer, color = (200, 128, 128)):
		"""

		@argument point - A 2-tuple or 2-list if you want mutability.

		"""

		self.point = point
		self.gts = grid_visualizer.grid_to_screen

		self.color = color


	def draw(self, width, height, screen, pygame):

		s = self.gts(self.point)

		pygame.draw.circle(screen, self.color, s, 7)



class SampleVisualizer(PyGameInterface):

	"""

	Generates a callable function to be used in conjunction with pygame_thread.py 
	to visualize samples on screen.

	"""


	LINE_THICKNESS_MIN = 1
	LINE_THICKNESS_MAX = 10


	def __init__(self, samples, grid_visualizer):

		self.samples = samples

		self.rescaler = _generate_min_max_normalizer(
			samples, self.LINE_THICKNESS_MIN, self.LINE_THICKNESS_MAX)

		self.gts = grid_visualizer.grid_to_screen


	def draw(self, width, height, screen, pygame):
		
		for sample in self.samples:

			origin = self.gts(sample[0])
			destination = self.gts(sample[1])
			force = self.rescaler(sample[2])


			# TODO: implement absolute force in addition to relative force

			print origin, destination

			pygame.draw.line(screen, (0, 0, 0), origin, destination, 1)



class COMRecorderVisualizer(PyGameInterface):

	"""

	Visualizes chains of sample points (not to be confused with the above calibration
	samples)

	"""

	def __init__(self, comrc, gv):

		self.comrc = comrc
		self.gv = gv


	def draw(self, width, height, screen, pygame):

		last = None
		now = time.time()


		self.comrc.sample_lock.acquire()


		for sample, time_ in self.comrc.drawable_samples:

			sample = self.gv.grid_to_screen(sample)

			if last != None:

				time_diff = now - time_


				# Reciprocal of number of seconds until lines completely fade

				fade_factor = 1


				color = time_diff * (fade_factor * 255)
				color = int(color)

				color_tuple = (color, color, color)

				if 0 <= color < 255:

					pygame.draw.line(screen, color_tuple, last, sample, 1)


			last = sample


		self.comrc.sample_lock.release()



def _generate_color_spectrum():
	pass


def _generate_min_max_normalizer(samples, new_min, new_max):
	"""

	Scans samples for min and max forces, then returns a linear function that maps those
	values to min_min and new_max respectively.

	"""


	# Define the functionality for zero or one samples to return the identity function.

	if len(samples) <= 1:
		return lambda x: int(x)
		

	forces = [sample[2] for sample in samples]


	old_min = min(forces)
	old_max = max(forces)


	return _generate_rescaler(old_min, old_max, new_min, new_max)



def _generate_rescaler(old_min, old_max, new_min, new_max):
	"""
	
	Returns a single-variate llinear function that maps old_min to old_max to new_max.

	"""

	old_delta = old_max - old_min
	new_delta = new_max - new_min


	def f(x):

		x = float(x)

		# Shift to zero

		x -= old_min


		# Stretch

		x /= old_delta
		x *= new_delta


		# Shift to new_min

		x += new_min

		return int(x)

	return f


class GridVisualizer(PyGameInterface):

	"""

	Generates a callable function to be used in conjunction with pygame_thread.py 
	to visualize grid on screen.

	This function also returns a utility to convert from screen coordinates to grid
	coordinates and vice-versa.

	Note: since they are defined inline, these functions generate_grid_visualizer() 
	is not designed to be fast! (although the returned functions are!)

	"""

	def __init__(self, grid):

		self.grid = grid
		self.wh = [1, 1]


	def set_wh(self, width, height):

		self.wh[0] = width
		self.wh[1] = height


	def draw(self, width, height, screen, pygame):

		self.set_wh(width, height)

		for point in self.grid.points():

			s = self.grid_to_screen(point)

			pygame.draw.circle(screen, (128, 128, 128), s, 5)


	def screen_to_grid(self, point):

		screen_width = self.wh[0]
		screen_height = self.wh[1]

		grid_width = self.grid.l
		grid_height = self.grid.w


		# Transform point to floating point representation such that all of our
		# following calculations are not truncated!

		point = (float(point[0]), float(point[1]))


		# Transform screen coordinate such that zero lies in the center

		point = (point[0] - (screen_width / 2), point[1] - (screen_height / 2))
		

		# Normalize screen coordinates such that borders correspond to +- 1

		point = (point[0] / (screen_width / 2), point[1] / (screen_height / 2))


		# Un-normalize screen such that borders correspond to grid min/max

		point = (point[0] * grid_width, point[1] * grid_height)

		# The grid is already centered about the origin so no more transormations
		# Convert back to ints & return

		return (int(point[0]), int(point[1]))


	def grid_to_screen(self, point):

		screen_width = self.wh[0]
		screen_height = self.wh[1]

		grid_width = self.grid.l
		grid_height = self.grid.w


		# Transform point to floating point representation such that all of our
		# following calculations are not truncated!

		point = (float(point[0]), float(point[1]))


		# Normalize to +- 1

		point = (point[0] / grid_width, point[1] / grid_height)

		# Normalize to screen coords

		point = (point[0] * (screen_width / 2), point[1] * (screen_height / 2))

		# Add offset so that zero lies in the top-left

		point = (point[0] + (screen_width / 2), point[1] + (screen_height / 2))


		# Convert back to ints & return

		return (int(point[0]), int(point[1]))