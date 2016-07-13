from plugin.forceplates_main import main
from plugin.threads.killable_thread import KillableThread

from plugin.DLL_wrappers.LabProUSB import LabProUSB

from plugin.gridcalibration.grid import Grid
from plugin.gridcalibration.generator import Generator, SamplingThread

from plugin.threads.pygame_thread import PyGameThread
import plugin.line_visualize as lv

import os
import time

import pytest



def test_take_samples_from_force_plates():

	# TODO: make this test smaller, AKA, break into components

	fp = main()


	# Start generator

	grid = Grid(10, 10, 20, 20)
	generator = Generator(grid, fp)

	st = SamplingThread(generator)
	st.start()


	# TODO: remove duplication with this and test_pygame_grid_visualize()

	# Start pygame

	pgt = PyGameThread()
	pgt.start()


	grid_task, stg, gts = lv.generate_grid_visualizer(grid)
	sample_task = lv.generate_sample_visualizer(generator.samples, gts)


	with pgt.draw_tasks_lock:

		pgt.draw_tasks.append(grid_task)
		pgt.draw_tasks.append(sample_task)


	# Kill all threads

	KillableThread.killAll()


	pgt.kill()
	pgt.join()

	pgt.query_exceptions()