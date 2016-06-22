import Calibration
from test_lib import test


class Grid(object):
	""" Represents a rectangular grid of points with iterable capabilities.

	Note: l - length. The grid covers equal spacings in the range [-l, l] (not [0, l]!). 
	Same for w - width.
	"""

	def __init__(self, w, l, w_seg, l_seg):
		self.l = l
		self.w = w
		self.l_seg = l_seg
		self.w_seg = w_seg

		self.hasMorePoints = None
		self.currentPoint = None

		self._pg = None

		self.reset()

	def reset(self):
		""" Reset the iterator. """

		self._pg = self._pointGenerator()
		self.currentPoint = self._pg.next()
		
	def next(self):
		if self.hasMorePoints:
			self.currentPoint = self._pg.next()

		return self.currentPoint

	def square(self, point):
		""" Returns the square to which the point belongs (in no particular order).

		Ex. grid.square((3, 4)) = [(0, 0), (10, 0), (0, 10), (10, 10)]
		"""

		dl = (self.l * 2) / self.l_seg
		dw = (self.w * 2) / self.w_seg

		for l in range(-self.l, self.l, dl * 2):
			pass

		for w in range(-self.w, self.w, dw * 2):
			pass

		




	def _pointGenerator(self):
		""" This generator object iterates through all pairs of points in the form (w, l)
		where w is a point along the width axis and l is a point along the length axis.

		There should be no direct access to this method by outside classes. Used next() instead. """

		self.hasMorePoints = True

		# Changes in length & width for each box
		dl = self.l / self.l_seg
		dw = self.w / self.w_seg

		# W/L are the sets of all points along length/width
		W = [dw * i for i in range(self.w_seg + 1)]
		L = [dl * i for i in range(self.l_seg + 1)]

		# W & L currently range from [0, w] and [0, l]. 
		# We will scale them to range from [-w, w] and [-l, l].
		W = [(w * 2 - self.w) for w in W]
		L = [(l * 2 - self.l) for l in L]

		for w in W:
			for l in L:

				# Last iteration
				if w is W[-1] and l is L[-1]:
					self.hasMorePoints = False

				yield (w, l)

	@test
	def iterate_simple_grid():

		x = Grid(10, 10, 10, 10)

		assert x.currentPoint == (-10, -10)
		assert x.hasMorePoints == True

		for _ in range(10):
			x.next()

		assert x.currentPoint == (-10, 10)
		assert x.hasMorePoints == True

		for _ in range(1000):
			x.next()

		assert x.currentPoint == (10, 10)
		assert x.hasMorePoints == False

		x.reset()

		assert x.currentPoint == (-10, -10)
		assert x.hasMorePoints == True

	@test
	def simple_square():

		# Unit divisions
		x = Grid(10, 10, 20, 20)

		p = (0.5, 0.5)

		assert (1, 1) in x.square(p)
		assert (0, 0) in x.square(p)
		assert (0, 1) in x.square(p)
		assert (0, 1) in x.square(p)


class GridCalibrate(object):
	

	def __init__(self):

		# Length & width of board rectangle
		self.l = 53.0
		self.w = 44.5

		self.l_segments = 6
		self.w_segments = 5

		self.done = False


		self.rpg = self.referencePointGenerator()

		self.nextReferencePoint()
		self.setGridMarker(self.referencePoint)
		
		self.samples = []


	def referencePointGenerator(self):

		

		self.done = True

	def nextReferencePoint(self):

		# Save to file if we are at the end
		if self.done:
			LoadHelper.save('gridcalibration%s' % int(time.time()), self.samples)

			print("Data saved!")
			
			return

		self.referencePoint = self.rpg.next()
		self.setGridMarker(self.referencePoint)


	def takeSample(self, plates):

		totalWeight = sum(plates.forces)
		center = cmds.xform("center", query = True, t = True, ws = True)

		self.samples.append((self.referencePoint, (center[0], center[2]), totalWeight))


	def setGridMarker(self, point):

		# Set gridpoint to the current target
		cmds.xform("gridpoint", t = [
			point[0], 
			0, 
			point[1]
		])


class Maker(object):
	""" Performs a series of calibrations in a grid pattern. """

	@test
	def crappy_test():
		assert True





# 1. Load calibration data

# 2. Interpolate between all four points for the following

# 2. Filter for samples within target range (target & radius)


# 3. Average the samples
# 4. Subtract the difference


class Processor(object):
	""" Processes points through an existing grid calibration. """

	def __init__(self, samples, grid):
		self.samples = samples
		self.grid = grid

	def _processPointWithSample(self, point, sample):
		""" Returns the point-to-be-processed with simple offset applied by the sample. """

		(actual, measured, weight) = sample

		measuredToActual = (actual[0] - measured[0], actual[1] - measured[1])

		return (point[0] + measuredToActual[0], point[1] + measuredToActual[1])


	def _weightSquare(self, point):
		""" Returns a 4-tuple of (point, weight), where the weights correspond to the 
		proximity of the point to that vertex of the grid. The sum of the weights is one. """

		square = grid.square(point)


	def process(self, point, weight):

		return self._processPointWithSample(point, self.samples[0])


	@test 
	def simple_identity():

		gc_object = [((0, 0), (0, 0), 1)]
		grid = Grid(3, 3, 6, 6)

		x = Processor(gc_object, grid)

		assert x.process((0, 0), 1) == (0, 0)
		assert x.process((100, 100), 5) == (100, 100)

	@test
	def single_point_correction():

		gc_object = [((0, 0), (5, 3), 10)]
		grid = Grid(3, 3, 6, 6)

		x = Processor(gc_object, grid)

		assert x.process((5, 3), 100) == (0, 0)

	@test 
	def choose_best_sample():

		gc_object = [
			((0, 0), (0, 0), 0),
			((0, 0), (1, 1), 1)
		]
		grid = Grid(3, 3, 6, 6)

		x = Processor(gc_object, grid)
		
		assert x.process((1, 1), 1) == (0, 0)

	@test
	def interpolate_samples_by_distance():

		gc_object = [
			((0, 0), (0, 0), 0),
			((1, 1), (2, 2), 0)
		]
		grid = Grid(3, 3, 6, 6)

		x = Processor(gc_object, grid)

		assert x.process((0.5, 0.5), 0) == (1, 1) # ???