
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Sep 02, 2016

## ------------------------------------------------------------------------



from plugin.gridcalibration.grid import Grid
from plugin.gridcalibration.generator import Generator
from plugin.gridcalibration.processor import Processor
from plugin.gridcalibration.reducer import Reducer
from plugin.gridcalibration.sampler import Sampler

import pytest
import random


def test_integrate_grid_calibrate():
	"""

	We mostly check that the interfaces together do not raise errors;
	this test does not care about the actual outputs.

	"""

	grid = Grid(10, 10, 20, 20)


	# Generate sampling data from a random process

	gen = Generator(grid)
	fp = MockForcePlates()


	# Take 100 samples per grid point

	while grid.hasMorePoints:

		for _ in range(100):
			gen.take_sample(fp.forces_after_calibration.get())

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




def _instance(cls):
	return cls()


class MockForcePlates(object):

	@_instance
	class forces_after_calibration(object):

		def get(self):

			return [random.random() for i in range(4)]
	

def random_point():

	return (random.random() * 20 - 10, random.random() * 20 - 10)