from plugin.gridcalibration.grid import Grid
from plugin.gridcalibration.generator import Generator
from plugin.gridcalibration.processor import Processor
from plugin.gridcalibration.reducer import Reducer
from plugin.gridcalibration.sampler import Sampler

import pytest
import random


def test_integrate_grid_calibrate():

	grid = Grid(10, 10, 20, 20)


	# Generate sampling data from a random process

	gen = Generator(grid, MockForcePlates())


	# Take 100 samples per grid point

	while grid.hasMorePoints:

		for _ in range(100):
			gen.take_sample()

		grid.next()


	# Use the sampler to take samples

	sampler = Sampler(gen.samples)


	# Sample random points on grid

	for _ in range(20):

		sampler.closest(random_point(), random.random() * 4, 0.2)
		sampler.simpleComposite(random_point(), random.random() * 4, 0.2)
		sampler.distanceComposite(random_point(), random.random() * 4, 0.2)


	# Reduce samples

	reducer = Reducer()
	samples_before_reduction = gen.samples

	ps = reducer.partitionBySource(samples_before_reduction)


	for i, p in enumerate(ps):

		ps[i] = reducer.reduce(p, 0.1)


	samples_after_reduction = reducer.merge(ps)

	assert len(samples_after_reduction) < len(samples_before_reduction)


	# User sampler on reduced sample set

	sampler = Sampler(samples_after_reduction)


	# Sample random points on grid

	for _ in range(20):

		sampler.closest(random_point(), random.random() * 4)
		sampler.simpleComposite(random_point(), random.random() * 4, 0.2)
		sampler.distanceComposite(random_point(), random.random() * 4, 0.2)


	# Test processor now

	proc = Processor(sampler.closest, grid)

	for _ in range(20):


		# Apply corrections for all of the samples we've just randomly generated and
		# reduced.

		proc.process(random_point(), random.random() * 4)



class MockForcePlates(object):

	@property
	def forces_after_calibration(self):

		return [random.random() for i in range(4)]
	

def random_point():

	return (random.random() * 20 - 10, random.random() * 20 - 10)