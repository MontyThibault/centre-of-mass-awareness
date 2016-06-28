class Affine(object):
	""" Defines an affine transformation on a single input. """

	def __init__(self, name = False, load = True):
		self.name = name
		self.offset = 0
		self.gain = 1

		# The last 
		self.last = 0

		if name and load:
			self.load()

	def process(self, c):
		self.last = c

		return (c + self.offset) * self.gain

	def setZero(self, c = None):
		if c is None:
			c = self.last

		self.offset = -c

	def setOne(self, c = None):
		if c is None:
			c = self.last

		self.gain = 1.0 / (c + self.offset)

	def load(self):
		if LoadHelper.exists(self.name):
			(self.offset, self.gain) = LoadHelper.load(self.name)
		else:
			# Save with defaults
			self.save()

	def save(self):
		LoadHelper.save(self.name, (self.offset, self.gain))


	def delete(self):
		""" Deletes the calibration entry, not the instance. """
		LoadHelper.delete(self.name)


