
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 18, 2016

## ------------------------------------------------------------------------



from plugin.forceplates_main import init_forceplates, send_program
from plugin.forceplates import ForcePlatesThread
from plugin.threads.killable_thread import KillableThread

from plugin.DLL_wrappers.LabProUSB import LabProUSB

from plugin.gridcalibration.grid import Grid
from plugin.gridcalibration.generator import Generator

from plugin.threads.pygame_thread import PyGameThread
import plugin.line_visualize as lv

import os
import time

import pytest


@pytest.yield_fixture
def pygame_thread():

	pgt = PyGameThread()
	pgt.start()

	yield pgt

	pgt.kill()
	pgt.join()

	pgt.query_exceptions()


def test_take_samples_from_force_plates(pygame_thread):

	# TODO: make this test smaller, AKA, break into components

	fp = init_forceplates()
	send_program(fp)

	fpt = ForcePlatesThread(fp)
	fpt.start()


	# Start generator

	grid = Grid(10, 10, 20, 20)
	generator = Generator(grid)

	# st = SamplingThread(generator)
	# st.start()


	# TODO: remove duplication with this and test_pygame_grid_visualize()

	# Start pygame

	
	pgt = pygame_thread

	gv = lv.GridVisualizer(grid)
	sv = lv.SampleVisualizer(generator.samples, gv)

	pgt.add_draw_task(gv.draw)
	pgt.add_draw_task(sv.draw)



	# Kill all threads

	KillableThread.killAll()