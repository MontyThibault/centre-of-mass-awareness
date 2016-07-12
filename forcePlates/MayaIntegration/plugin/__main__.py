import os

from forceplates import ForcePlates

from calibration.affine import Affine
from gridcalibration.grid import Grid
from gridcalibration.generator import Generator
from gridcalibration.reducer import Reducer
from gridcalibration.sampler import Sampler
from gridcalibration.processor import Processor

from threads.killable_thread import KillableThread as KT
from threads.main_thread import MainThread
from threads.console_thread import ConsoleThread
from threads.persistence_sync_thread import PersistenceSyncThread
from threads.calibration_program_thread import CalibrationProgramThread
from threads.pygame_thread import PyGameThread

from DLL_wrappers.LabProUSB import LabProUSB

import maya_utils as mu
import maya_socket_connection as msc



def main():


	pst = PersistenceSyncThread(os.path.dirname(__file__) + '/.sync.pickle')
	pst.start()
	d = pst.objs


	mt = MainThread()


	#######################
	# Force plates

	# !! NO TESTS !!
	# (how?)

	if 'fp' not in d:
		d['fp'] = init_forceplates()


	fp = d['fp']
	send_program(fp)



	# Generator

	grid = Grid(44.5, 53, 6, 7)
	gen = Generator(grid, fp)
	

	mt.tasks.add(_callwith(fp.update, LabProUSB))
	# mt.tasks.add(lambda: fp.update(LabProUSB))

	mt.tasks.add(feed_forces(fp))
	mt.tasks.add(gen.take_sample)

	mt.start() 


	########################

	pgt = PyGameThread()
	pgt.start()


	########################

	# !! NO TESTS !!

	kpt = CalibrationProgramThread(gen)
	kpt.start()

	kpt.fps = mt.fps

	kpt.seconds_per_point = .02
	kpt.seconds_between_points = .01


	#####################

	msc.call_func(mu.createLocatorTransformPair, 'sampling_marker')


	def f(cs):

		p = gen.grid.currentPoint

		if cs:
			print "Sampling started at %s" % str(p)
			
		else:
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



	# Monday: finish this calibration program
	# and implement reverse-correction.

	# Tuesday: visualization utility

	# Wednesday: Collect calibration data & ready to use


	####################################
	# Interactive console utilities


	# Kill the threads and exit the interactive console
	# Just quit() won't do it.

	def kill():

		d['fp'] = fp

		KT.killAll()
		exit()


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


def _callwith(f, *args, **kwargs):

	def g(*args_, **kwargs_):
		f(*args, **kwargs)

	return g

def init_forceplates():

	fp = ForcePlates()
	fp.init_calibs(Affine)

	return fp

def send_program(fp):

	fp.uninit_labpro(LabProUSB)
	fp.init_labpro(LabProUSB)

	with open(os.path.dirname(os.path.realpath(__file__)) + 
		 	'/programs/simple_program.txt', 'r') as f:

		fp.send_program(LabProUSB, f) 


if __name__ == '__main__':
	main()