from plugin.forceplates import ForcePlates, ForcePlatesThread
from plugin.DLL_wrappers.LabProUSB import LabProUSB
from plugin.calibration.affine import Affine
from plugin.main_thread import MainThread

from plugin.forceplates_main import init_forceplates, spin_fpt, send_program

import time
import pytest

@pytest.yield_fixture
def kill_threads_after():

	yield

	ForcePlatesThread.killAll()


def test_labpro_returns_non_zero_forces_then_dies(kill_threads_after):

	fp = init_forceplates()
	send_program(fp)
	spin_fpt(fp)


	max_waiting_time = 6 # seconds
	initial_time = time.time()


	# Wait until we get real force measurements

	while sum(fp.forces) == 0:

		if time.time() - initial_time > max_waiting_time:

			assert False, "Max waiting time exceeded to get forces."

		time.sleep(1.0 / 60)


	# Blinks (terminal program) and dies
	# Definition "dies": returns a zero-array of forces

	fp.blink(LabProUSB)

	max_waiting_time = 5 # seconds
	initial_time = time.time()


	previous_forces = fp.forces


	# While there is no change in forces from one frame to the next

	while sum([a - b for a, b in zip(previous_forces, fp.forces)]) != 0:


		previous_forces = fp.forces

		if time.time() - initial_time > max_waiting_time:

			assert False, "Max waiting time exceeded for program to die."


		# Here we use ten frames instead of one frame to give a larger margin
		# to change forces.

		time.sleep(10.0 / 60)


def test_main(kill_threads_after):

	fp = init_forceplates()
	send_program(fp)
	spin_fpt(fp)
