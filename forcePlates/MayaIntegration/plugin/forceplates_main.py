from plugin.DLL_wrappers.LabProUSB import LabProUSB
from plugin.forceplates import *

from plugin.calibration.affine import Affine


def main():

	fp = ForcePlates()
	fp.init_calibs(Affine)

	fp.init_labpro(LabProUSB)


	with open('plugin/programs/simple_program.txt', 'r') as f:

		fp.send_program(LabProUSB, f)


	fpt = ForcePlatesThread(fp)
	fpt.start()

	return fp