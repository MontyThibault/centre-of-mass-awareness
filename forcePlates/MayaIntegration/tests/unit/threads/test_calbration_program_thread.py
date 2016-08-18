
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 18, 2016

## ------------------------------------------------------------------------



from plugin.threads.calibration_program_thread import CalibrationProgramThread


def test_calibration_program_without_running_thread():

	gen = MockGenerator()
	fp = MockForcePlates()
	
	cpt = CalibrationProgramThread(gen, fp)

	cpt.fps = 1

	cpt.seconds_per_point = 10
	cpt.seconds_between_points = 10

	
	# Go to the middle of first sample

	for _ in range(15):

		cpt.loop()

	assert cpt._currently_sampling.get()

	# Go to end of first sample

	for _ in range(10):

		cpt.loop()

	assert not cpt._currently_sampling.get()

	# Take many more samples and stop in the middle of sampling

	for _ in range(80):

		cpt.loop()

	assert cpt._currently_sampling.get()


	# Suppose we have reached the end of the grid iterator

	gen.grid.hasMorePoints = False


	# Take many more samples and stop in what would be the middle of sampling

	for _ in range(40):

		cpt.loop()


	# Test that we're not actually sampling

	assert not cpt._currently_sampling.get()



class MockGenerator(object):

	def __init__(self):

		self.grid = MockGrid()
		self.samples = []


	def take_sample(self):

		self.samples.append(None)



class MockGrid(object):

	def __init__(self):

		self.currentPoint = (0, 0)
		self.hasMorePoints = True


	def next(self):

		return (0, 0)



def _instance(cls):
	return cls()


class MockForcePlates(object):

	@_instance
	class forces_after_calibration(object):

		def get(self):

			return [random.random() for i in range(4)]


		def add_listener(self, f):
			pass

		def remove_listener(self, f):
			pass