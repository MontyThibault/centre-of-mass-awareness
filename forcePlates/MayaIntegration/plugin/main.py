import os
import maya.cmds as cmds

from main_thread import MainThread
from forceplates import ForcePlates
from calibration.affine import Affine
from gridcalibration.grid import Grid
from gridcalibration.generator import Generator
from DLL_wrappers.LabProUSB import LabProUSB
from window import Window


def main():

	mt = MainThread()


	# Force plates

	fp = init_forceplates()


	# Generator

	grid = Grid(10, 20, 3, 6)
	gen = Generator(grid, fp)




	# cmds.window('ForcePlates', width = 350, sizeable = False)
	# cmds.columnLayout(adjustableColumn = True)

	# cmds.button(label = 'Kill', command = _callwith(mt.kill))	

	# cmds.showWindow()



	# Ultimately, the window interface is limited and unnecessary
	# Is there an easy way to make a cmd-style interface?



	update_task = _callwith(fp.update, LabProUSB)
	sample_task = _callwith(gen.take_sample)

	mt.tasks.add(update_task)
	mt.tasks.add(sample_task)

	mt.tasks.add(_callwith(print_samples, gen))

	mt.start() 



def print_samples(sampler):
	print sampler.samples



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