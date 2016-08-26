
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 26, 2016

## ------------------------------------------------------------------------



from plugin.threads.pygame_thread import PyGameThread
import plugin.line_visualize as lv
from plugin.gridcalibration.grid import Grid

import time
import pytest


@pytest.fixture
def restart_pygame():

	import pygame
	pygame.quit()


def test_feed_visualizers_to_pygame(restart_pygame):
	"""

	This test will draw an array of ten by ten points, stretched to fit the window.

	"""

	pgt = PyGameThread()
	pgt.start()

	grid = Grid(8, 10, 8, 10)



	# Generate arbitrary samples

	samples = []

	for p in grid.points():

		origin = p
		destination = (p[0] + 1, p[1] + 1)
		force = abs(p[0])

		sample = (origin, destination, force)
		samples.append(sample)


	# Generate the drawing functions for the pygame thread

	gv = lv.GridVisualizer(grid)
	pv = lv.PointVisualizer((0, 0), gv)
	sv = lv.SampleVisualizer(samples, gv)


	pgt.add_draw_task(gv.draw)
	pgt.add_draw_task(pv.draw)
	pgt.add_draw_task(sv.draw)


	time.sleep(0.1)

	# pgt.kill()
	# pgt.join()

	# pgt.query_exceptions()
