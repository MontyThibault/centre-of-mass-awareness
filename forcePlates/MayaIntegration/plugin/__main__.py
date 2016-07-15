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

from DLL_wrappers.LabProUSB import LabProUSB

import maya_utils as mu
import maya_socket_connection as msc

from forceplates_main import init_forceplates, spin_fpt, send_program

import line_visualize as lv


def main():


	pst = PersistenceSyncThread(os.path.dirname(__file__) + '/.sync.pickle')
	pst.start()

	d = pst.objs


	#######################
	# Force plates

	# !! NO TESTS !!
	# (how?)

	if 'fp' not in d:
		d['fp'] = init_forceplates()

	fp = d['fp']

	send_program(fp)
	spin_fpt(fp)
	



	# Generator

	grid = Grid(44.5, 53, 6, 7)
	generator = Generator(grid, fp)


	########################

	copt = CenterOfPressureThread(fp, grid)
	copt.start()

	########################

	st = SamplingThread(generator)
	st.start()

	########################

	mt = MainThread()

	mt.tasks.add(feed_forces(fp))

	mt.start() 


	########################

	pgt = PyGameThread()
	pgt.start()

	gv = lv.GridVisualizer(grid)
	pv = lv.PointVisualizer(copt.center_of_pressure, gv)
	sv = lv.SampleVisualizer(generator.samples, gv)


	with pgt.draw_tasks_lock:

		pgt.draw_tasks.append(gv.draw)
		pgt.draw_tasks.append(pv.draw)
		pgt.draw_tasks.append(sv.draw)


	########################

	# !! NO TESTS !!

	kpt = CalibrationProgramThread(generator)
	# kpt.start()

	kpt.fps = mt.fps

	kpt.seconds_per_point = .02
	kpt.seconds_between_points = .01


	#####################

	msc.call_func(mu.createLocatorTransformPair, 'sampling_marker')


	def f(currently_sampling):

		p = kpt.generator.grid.currentPoint


		if currently_sampling:

			print "Sampling started at %s" % str(p)
			
		elif not currently_sampling:

			print "Sampling stopped. Next point is %s" % str(p)		

		msc.call_func(mu.moveObject, [p[0], 0, p[1]], 'sampling_marker')


	kpt._currently_sampling.add_listener(f)



	###################

	# Load samples
	# 
	#
	# How to test?
	# How to test MAIN program?

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

		d['fp'] = fp

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




def feed_forces(fp):

	def f():
		msc.call_func(mu.move_markers, fp.forces_after_calibration)

	return f


if __name__ == '__main__':
	main()