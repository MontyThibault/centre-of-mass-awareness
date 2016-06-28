class Utility(object):
	""" Used in conjunction with Maya to sample points. This will be revised. """

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