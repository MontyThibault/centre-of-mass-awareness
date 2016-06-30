import os


from main_thread import MainThread

from forceplates import ForcePlates

from calibration.affine import Affine

from gridcalibration.grid import Grid
from gridcalibration.generator import Generator

from DLL_wrappers.LabProUSB import LabProUSB


def main():

	mt = MainThread()


	# Force plates

	fp = init_forceplates()


	# Generator

	grid = Grid(10, 20, 3, 6)
	gen = Generator(grid, fp)


	# window
	# todo
	

	mt.tasks.add(fp.update)
	mt.tasks.add(gen.take_sample)


	mt.start()



def init_forceplates():
	
	fp = ForcePlates()
	fp.init_calibs(Affine)

	file = open(os.path.dirname(os.path.realpath(__file__)) + 
		 	'/programs/simple_program.txt', 'r')

	fp.send_program(LabProUSB, file)
	file.close()

	return fp