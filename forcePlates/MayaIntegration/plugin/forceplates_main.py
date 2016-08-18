
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 18, 2016

## ------------------------------------------------------------------------



from plugin.DLL_wrappers.LabProUSB import LabProUSB
from plugin.forceplates import *

from plugin.calibration.affine import Affine


def init_forceplates():

	fp = ForcePlates()
	fp.init_calibs()

	return fp


def send_program(fp):

	fp.init_labpro(LabProUSB)

	with open('plugin/programs/simple_program.txt', 'r') as f:

		fp.send_program(LabProUSB, f)


	