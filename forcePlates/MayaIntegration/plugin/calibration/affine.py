
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 23, 2016

## ------------------------------------------------------------------------



class Affine(object):
	""" Defines an affine transformation on a single input. """

	def __init__(self):
		self.offset = 0
		self.gain = 1

		# The last output
		self.last = 0

	def process(self, c):
		self.last = c

		return (c + self.offset) * self.gain

	def setZero(self, c):
		self.offset = -c

	def setZeroLast(self):
		self.offset = -self.last

	def setOne(self, c):
		self.gain = 1.0 / (c + self.offset)

	def setOneLast(self):
		self.gain = 1.0 / (self.last + self.offset)