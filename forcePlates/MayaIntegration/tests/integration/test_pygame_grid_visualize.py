from plugin.threads.pygame_thread import PyGameThread
import plugin.line_visualize as lv
from plugin.gridcalibration.grid import Grid

import time
import pytest


@pytest.fixture
def restart_pygame():

	import pygame
	pygame.quit()


def test_feed_drawing_function_to_pygame(restart_pygame):

	pgt = PyGameThread()
	pgt.start()

	grid = Grid(10, 10, 10, 10)




	# Generate the drawing functions for the pygame thread

	task, stg, gts = lv.generate_grid_visualizer(grid)

	with pgt.draw_tasks_lock:

		pgt.draw_tasks.append(task)



	time.sleep(10)

	pgt.kill()
	pgt.join()

	pgt.query_exceptions()
