from plugin.threads.calibration_program_thread import CalibrationProgramThread


def test_calibration_program_without_thread():

	gen = MockGenerator()
	cpt = CalibrationProgramThread(gen)

	cpt.fps = 1

	cpt.seconds_per_point = 10
	cpt.seconds_between_points = 10

	
	# Go to the middle of first sample

	for _ in range(15):

		cpt.loop()

	assert cpt._currently_sampling

	# Go to end of first sample

	for _ in range(10):

		cpt.loop()

	assert not cpt._currently_sampling

	# Take many more samples and stop in the middle of sampling

	for _ in range(80):

		cpt.loop()

	assert cpt._currently_sampling


	# Suppose we have reached the end of the grid iterator

	gen.grid.hasMorePoints = False


	# Take many more samples and stop in what would be the middle of sampling

	for _ in range(40):

		cpt.loop()


	# Test that we're not actually sampling

	assert not cpt._currently_sampling

	assert len(cpt.generator.samples) == 55



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