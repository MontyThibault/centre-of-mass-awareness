from plugin.forceplates import ForcePlates
from plugin.DLL_wrappers.LabProUSB import LabProUSB
from plugin.calibration.affine import Affine


def test_labpro_read_forces():

	fp = ForcePlates()
	
	fp.init_calibs(Affine)
	fp.init_labpro(LabProUSB)
	fp.uninit_labpro(LabProUSB)


	# something something to do with proper functionality


def test_labpro_blink_and_die():

	pass