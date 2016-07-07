from plugin.forceplates import ForcePlates
from plugin.DLL_wrappers.LabProUSB import LabProUSB
from plugin.calibration.affine import Affine
from plugin.main_thread import MainThread

import time


def test_labpro_returns_non_zero_forces_then_dies():

	fp = ForcePlates()
	
	fp.init_calibs(Affine)
	fp.init_labpro(LabProUSB)


	# Spin up the main thread for updates

	mt = MainThread()
	mt.tasks.add(fp.update)
	mt.start


	max_waiting_time = 5 # seconds
	initial_time = time.time()


	while sum(fp.forces) == 0:

		if time.time() - initial_time > max_waiting_time:

			assert False, "Max waiting time exceeded to get forces."

		time.sleep(1.0 / mt.fps)


	fp.uninit_labpro(LabProUSB)


	# Blinks and dies

	max_waiting_time = 2 # seconds
	initial_time = time.time()


	while sum(fp.forces) != 0:

		if time.time() - initial_time > max_waiting_time:

			assert False, "Max waiting time exceeded for program to die."

		time.sleep(1.0 / mt.fps)