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