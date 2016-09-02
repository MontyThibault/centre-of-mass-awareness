
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Sep 02, 2016

## ------------------------------------------------------------------------



import os

from gridcalibration.grid import Grid

from threads.killable_thread import KillableThread as KT
from threads.console_thread import ConsoleThread
from threads.center_of_pressure_thread import CenterOfPressureThread
from threads.pygame_thread import PyGameThread
from threads.sixaxis_thread import SixAxisThread

# import maya_utils as mu
# import maya_socket_connection as msc

from dynamic_color import DynamicColor

from sixaxis.sixaxis import SixAxis

from center_of_pressure import CenterOfPressure
from com_recorder import COMRecorder

import line_visualize as lv

import pygame_interaction


def main():

	sat = SixAxisThread()
	sat.start()


	########################

	# The frame of the visualization is +- 15cm on both axes, with
	# six evenly-spaced dots for reference.

	grid = Grid(0.15, 0.15, 6, 6)

	########################

	pgt = PyGameThread()
	pgt.start()

	gv = lv.GridVisualizer(grid)
	

	pgt.add_draw_task(gv.draw)


	for w_sensor in sat.world.world_sensors + [sat.world]:

		comrc = COMRecorder(w_sensor)
		comrc.bind_listeners()

		w_sensor.comrc = comrc



		base_color = (255, 0, 0)

		if w_sensor == sat.world:

			base_color = (0, 255, 0)
			comrc.record_permanent = True

		# Highlighting

		# elif w_sensor.sensor == sat.world.M5170:
		# 	base_color = (0, 0, 255)

		color_list = DynamicColor(w_sensor, base_color).color

		cp_v = lv.PointVisualizer(w_sensor.centre_of_pressure.get(), gv, color_list)


		crv = lv.COMRecorderVisualizer(comrc, gv)

		pgt.add_draw_task(cp_v.draw)
		pgt.add_draw_task(crv.draw)




	timeframe = [0, 1e99]

	def start():
		import time
		timeframe[0] = time.time()

	def stop():
		import time
		timeframe[1] = time.time()

	def save(filename):

		ss = sat.world.comrc.samples
		tf = timeframe

		ss = filter(lambda s: tf[0] <= s[2] <= tf[1], ss)


		import pickle 

		with open('C:/Users/Monty/Desktop/COMAwareness/forcePlates/MayaIntegration/data/' + filename, 'wb') as f:
			pickle.dump(ss, f)


		sat.world.comrc.samples = []


	####################################
	# Interactive console utilities


	# Kill the threads and exit the interactive console
	# Just quit() won't do it.

	def kill():

		KT.killAll()
		pgt.kill()
		quit()


	####################################
	# Begin interactive console
	
	l = locals()
	l.update(globals())

	c = ConsoleThread(l)
	c.start()


if __name__ == '__main__':
	main()