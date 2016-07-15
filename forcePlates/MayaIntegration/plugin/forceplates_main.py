from plugin.DLL_wrappers.LabProUSB import LabProUSB
from plugin.forceplates import *

from plugin.calibration.affine import Affine


def init_forceplates():

	fp = ForcePlates()
	fp.init_calibs(Affine)

	return fp


def spin_fpt(fp):

	fpt = ForcePlatesThread(fp)
	fpt.start()


def send_program(fp):

	fp.init_labpro(LabProUSB)

	with open('plugin/programs/simple_program.txt', 'r') as f:

		fp.send_program(LabProUSB, f)


	