"""

Utilities for interfacing pygame & the existing sampling data structure.

TODO: convert these to classes instead of persistent functions & generators. 

"""


LINE_THICKNESS_MIN = 1
LINE_THICKNESS_MAX = 5

def generate_sample_visualizer(samples, grid_to_screen):
	"""

	Generates a callable function to be used in conjunction with pygame_thread.py 
	to visualize samples on screen.

	"""

	rescaler = _generate_min_max_normalizer(samples, LINE_THICKNESS_MIN, LINE_THICKNESS_MAX)


	def f(width, height, screen, pygame):
		
		for sample in samples:

			origin = grid_to_screen(sample[0])
			destination = grid_to_screen(sample[1])
			force = rescaler(sample[2])

			pygame.draw.line(screen, (0, 0, 0), origin, destination, force)


	return f


def _generate_color_spectrum():
	pass


def _generate_min_max_normalizer(samples, new_min, new_max):
	"""

	Scans samples for min and max forces, then returns a linear function that maps those
	values to min_min and new_max respectively.

	"""

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


def generate_grid_visualizer(grid):
	"""

	Generates a callable function to be used in conjunction with pygame_thread.py 
	to visualize grid on screen.

	This function also returns a utility to convert from screen coordinates to grid
	coordinates and vice-versa.

	Note: since they are defined inline, these functions generate_grid_visualizer() 
	is not designed to be fast! (although the returned functions are!)

	"""

	wh = [1, 1]

	def f(width, height, screen, pygame):

		wh[0] = width
		wh[1] = height


		for point in grid.points():

			s = grid_to_screen(point)

			pygame.draw.circle(screen, (128, 128, 128), s, 5)



	def screen_to_grid(point):

		screen_width = wh[0]
		screen_height = wh[1]

		grid_width = grid.w
		grid_height = grid.l


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


	def grid_to_screen(point):


		screen_width = wh[0]
		screen_height = wh[1]

		grid_width = grid.w
		grid_height = grid.l


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


	return f, screen_to_grid, grid_to_screen