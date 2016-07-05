import os
import code

from main_thread import MainThread
from forceplates import ForcePlates
from calibration.affine import Affine
from gridcalibration.grid import Grid
from gridcalibration.generator import Generator
from console import Console

from DLL_wrappers.LabProUSB import LabProUSB

from killable_thread import KillableThread as KT

import maya_utils as mu
import maya_socket_connection as msc


def main():

	mt = MainThread()


	# Force plates

	fp = init_forceplates()


	# Generator

	grid = Grid(10, 20, 3, 6)
	gen = Generator(grid, fp)
	

	# How to pass arguments into call_func?


	update_task = _callwith(fp.update, LabProUSB)
	# move_markers_task = _callwith(msc.call_func, lambda: mu.move_markers(fp.forces))
	sample_task = _callwith(gen.take_sample)

	mt.tasks.add(update_task)
	# mt.tasks.add(move_markers_task)
	mt.tasks.add(sample_task)

	mt.start() 



	####################################

	# import maya_socket_connection as msc

	####################################
	
	# Kill the threads and exit the interactive console
	# Just quit() won't do it.

	def kill():
		KT.killAll()
		exit()

	####################################
	# Begin interactive console

	c = Console(locals())
	c.start()



def _callwith(f, *args, **kwargs):

	def g(*args_, **kwargs_):
		f(*args, **kwargs)

	return g


def init_forceplates():
	
	fp = ForcePlates()
	fp.init_calibs(Affine)

	file = open(os.path.dirname(os.path.realpath(__file__)) + 
		 	'/programs/simple_program.txt', 'r')

	fp.send_program(LabProUSB, file)
	file.close()

	return fp



if __name__ == '__main__':

	main()