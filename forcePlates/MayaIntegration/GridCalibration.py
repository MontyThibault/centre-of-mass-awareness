import Calibration
import math
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


	def _toIntegerForm(self, point):
		""" The point is transformed in such a way that the integeral values correspond to
		vertices on the graph, with (0, 0) being the first vertex, and (l_seg, w_seg) being
		the far corner.

		They can then be used for rounding or testing, and transormed back again.
		"""

		nw = ((point[0] + self.w) * (self.w_seg)) / (2 * self.w)
		nl = ((point[1] + self.l) * (self.l_seg)) / (2 * self.l)

		return (nw, nl)

	def _fromIntegerForm(self, point):
		""" Inverse of _toIntegerForm. """

		w = (2 * self.w * point[0]) / (self.w_seg) - self.w
		l = (2 * self.l * point[1]) / (self.l_seg) - self.l

		return (w, l)		


	def contains(self, point):
		""" If this grid contains the given point. """

		(w, l) = self._toIntegerForm(point)

		inside = l <= self.l_seg and w <= self.w_seg

		aligned = round(w) == w and round(l) == l


		return inside and aligned


	def square(self, point):
		""" Returns the square to which the point belongs. Opposite vertices are
		congruent modulo 2 the index. IE. 0 is opposite 2 and 1 is opposite 3.

		If the square lies exactly on a vertex or edge, we return those vertices
		as both upper/lower bounds.

		Ex. grid.square((3, 4)) = [(10, 0), (0, 0), (0, 10), (10, 10)]
		Ex. grid.square((0, 0)) = [(0, 0), (0, 0), (0, 0), (0, 0)]
		"""


		# Go to integer form, apply a rounding operation, and then apply the 
		# inverse transformation.

		(nw, nl) = self._toIntegerForm(point)


		points = [
			(math.floor(nw), math.floor(nl)), 
			(math.floor(nw), math.ceil(nl)), 
			(math.ceil(nw), math.ceil(nl)), 
			(math.ceil(nw), math.floor(nl))
		]


		points = [self._fromIntegerForm(p) for p in points]

		return points


	def weightedSquare(self, point):
		""" Returns a list of (point, weight), where the weights correspond to the 
		proximity of the point to that vertex of the grid. The sum of the weights is one. """

		square = self.square(point)


		# Splice lines going horizontally and vertically through the point & calculate
		# the areas for each vertex corner.

		areas = [
			abs((vert[0] - point[0]) * (vert[1] - point[1]))
			for vert in square
		]

		totalArea = sum(areas)

		if totalArea == 0:

			# Single point case
			areas = [1, 0, 0, 0]

		else:
			areas = [a / totalArea for a in areas]


		# Shuffle indicies around such that we interchange opposite vertices on the square.
		# With this we define the weight as the relative area of the opposite vertex.

		opposites = [square[(i + 2) % 2] for i in range(4)]

		return zip(opposites, areas)


	def _pointGenerator(self):
		""" This generator object iterates through all pairs of points in the form (w, l)
		where w is a point along the width axis and l is a point along the length axis.

		There should be no direct access to this method by outside classes. Used next() instead. """

		self.hasMorePoints = True

		for w in range(self.w_seg + 1):
			for l in range(self.l_seg + 1):

				if w == self.w_seg and l == self.l_seg:
					self.hasMorePoints = False

				yield self._fromIntegerForm((w, l))

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
	def simple_contains():

		x = Grid(10, 5, 20, 10)

		assert x.contains((10, 5))
		assert x.contains((-3, -2))
		assert not x.contains((0.3, 3))
		assert not x.contains((11, 0))


	@test
	def simple_square():

		# Unit divisions
		x = Grid(10, 10, 20, 20)

		p = (0.5, 0.5)

		assert (1, 1) in x.square(p)
		assert (0, 0) in x.square(p)
		assert (0, 1) in x.square(p)
		assert (0, 1) in x.square(p)


		p = (6.321, -7.466)

		assert (6, -8) in x.square(p)
		assert (7, -8) in x.square(p)
		assert (6, -7) in x.square(p)
		assert (7, -7) in x.square(p)

	@test
	def weighted_square():

		x = Grid(10, 10, 1, 1)

		p = (0, 0)

		assert x.weightedSquare(p)[0][1] == 0.25

		p = (10, 10)

		assert ((10, 10), 1) in x.weightedSquare(p)

		p = (4.4324, -8.54323)
		ws = x.weightedSquare(p)

		assert sum([w for (p, w) in ws]) == 1



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

	def _chooseSample(self, point, weight):
		""" With a grid-aligned point """

		pass

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