


def generate_sample_visualizer(samples, corners):
	"""

	Generates a callable function to be used in conjunction with pygame_thread.py 
	to visualize samples on screen.

	"""

	def f(width, height, screen, pygame):
		
		for sample in samples:

			pass


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


		# for point in grid.points():

		# 	s = grid_to_screen(point)

		# 	pygame.draw.circle(s)



	def screen_to_grid(point):

		screen_width = wh[0]
		screen_height = wh[1]

		grid_width = grid.w
		grid_height = grid.l


		# Transform screen coordinate such that zero lies in the center

		point = (point[0] - (screen_width / 2), point[1] - (screen_height / 2))
		

		# Normalize screen coordinates such that borders correspond to +- 1

		point = (point[0] / (screen_width / 2), point[1] / (screen_height / 2))


		# Un-normalize screen such that borders correspond to grid min/max

		point = (point[0] * grid_width, point[1] * grid_height)

		# The grid is already centered about the origin so no more transormations

		return point


	def grid_to_screen(point):


		screen_width = wh[0]
		screen_height = wh[1]

		grid_width = grid.w
		grid_height = grid.l


		# Normalize to +- 1

		point = (point[0] / grid_width, point[1] / grid_height)

		# Normalize to screen coords

		point = (point[0] * (screen_width / 2), point[1] * (screen_height / 2))

		# Add offset so that zero lies in the top-left

		point = (point[0] + (screen_width / 2), point[1] + (screen_height / 2))

		return point


	return f, screen_to_grid, grid_to_screen