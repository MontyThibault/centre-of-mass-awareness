import os

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
	

	mt.tasks.add(feed_forces(fp))
	mt.tasks.add(gen.take_sample)

	mt.start() 
	

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


def feed_forces(fp):

	def f():
		msc.call_func(mu.move_markers, fp.forces)

	return f


def _callwith(f, *args, **kwargs):

	def g(*args_, **kwargs_):
		f(*args, **kwargs)

	return g


def init_forceplates():
	
	fp = ForcePlates()

	fp.init_labpro(LabProUSB)
	fp.init_calibs(Affine)

	file = open(os.path.dirname(os.path.realpath(__file__)) + 
		 	'/programs/simple_program.txt', 'r')

	fp.send_program(LabProUSB, file)
	file.close()

	return fp



if __name__ == '__main__':

	main()