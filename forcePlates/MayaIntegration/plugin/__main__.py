import os

from gridcalibration.grid import Grid
from gridcalibration.generator import Generator, SamplingThread
from gridcalibration.reducer import Reducer
from gridcalibration.sampler import Sampler
from gridcalibration.processor import Processor

from threads.killable_thread import KillableThread as KT
from threads.main_thread import MainThread
from threads.console_thread import ConsoleThread
from threads.persistence_sync_thread import PersistenceSyncThread
from threads.calibration_program_thread import CalibrationProgramThread
from threads.center_of_pressure_thread import CenterOfPressureThread
from threads.pygame_thread import PyGameThread

import maya_utils as mu
import maya_socket_connection as msc

from forceplates import ForcePlates, ForcePlatesThread
from forceplates_main import send_program


from center_of_pressure import CenterOfPressure

import line_visualize as lv

import pygame_interaction
import maya_interaction


def main():


	pst = PersistenceSyncThread(os.path.dirname(__file__) + '/.sync.pickle')
	pst.start()

	d = pst.objs

	# del d['fp']

	#######################
	# Force plates

	# !! NO TESTS !!
	# (how?)


	fp = ForcePlates()

	if 'fp_calibs' not in d:

		fp.init_calibs()
		d['fp_calibs'] = fp.calibrations

	else:

		fp.calibrations = d['fp_calibs']

	send_program(fp)
	



	fpt = ForcePlatesThread(fp)
	fpt.start()
	

	########################

	grid = Grid(44.5, 53, 6, 7)
	generator = Generator(grid)


	########################


	cop = CenterOfPressure(grid)
	cop.bind_listeners(fp)


	########################

	# Kill this thread

	# st = SamplingThread(generator)
	# st.start()

	########################

	# !! NO TESTS !!

	kpt = CalibrationProgramThread(fp, generator)

	kpt.fps = 10

	kpt.seconds_per_point = 2
	kpt.seconds_between_points = 1


	########################

	pgt = PyGameThread()
	pgt.start()

	gv = lv.GridVisualizer(grid)
	cp_v = lv.PointVisualizer(cop.center, gv)
	sv = lv.SampleVisualizer(generator.samples, gv)

	pgt.add_draw_task(gv.draw)
	pgt.add_draw_task(cp_v.draw)
	pgt.add_draw_task(sv.draw)

	pygame_interaction.bind_listeners(kpt, pgt, gv)


	#####################

	maya_interaction.create_sampling_locator()
	maya_interaction.bind_listeners(kpt, fpt)

	


	###################

	# Console


	def reduce():

		s = d['s']
		reducer = Reducer()
	
		ps = reducer.partitionBySource(s)


		for i, p in enumerate(ps):
			ps[i] = reducer.reduce(p, 0.1)

		merged = reducer.merge(ps)
		d['s'] = reducer.filter_min_max(merged, 0.1, 9999)



	def sample_and_process(p):
		""" p = ((x, y), w) """

		sampler = Sampler(d['s'])
		processor = Processor(sampler.closest, grid)

		return processor.process(*p)



	####################################
	# Interactive console utilities


	# Kill the threads and exit the interactive console
	# Just quit() won't do it.

	def kill():

		d['fp_calibs'] = fp.calibrations

		KT.killAll()
		pgt.kill()

		# c.kill() doesn't work?

		quit()


	saz = fp.set_all_zero
	fpc = fp.calibrations

	####################################
	# Begin interactive console
	
	l = locals()
	l.update(globals())

	c = ConsoleThread(l)
	c.start()


if __name__ == '__main__':
	main()