
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 26, 2016

## ------------------------------------------------------------------------



from plugin.forceplates import ForcePlates
import unittest



class TestForcePlates(unittest.TestCase):

	def setUp(self):
		self.fp = ForcePlates()
		self.lp = MockLabProUSB()


	def test_update_and_get_forces(self):
		
		self.lp.mockString = "{ 4, 3, 2, 1 }"
		self.fp.update(self.lp)

		assert self.fp.forces.get() == [4, 3, 2, 1]


	def test_try_calibs_without_injecting_first(self):

		with self.assertRaises(Exception):
			self.fp.forces_with_calibs()


	def test_blink(self):

		self.fp.blink(self.lp)
		assert self.lp.recentString.value == 's'


	def test_send_program(self):

		mockfile = MockFile()
		self.fp.send_program(self.lp, mockfile)

		assert self.lp.recentString.value == b's{B}\n'
		



class MockLabProUSB(object):

	# The following methods are mirrors of those defined in the LabProUSB 
	# dll header file.

	# Note that we work with ctypes objects, namely string buffers and c_ints.


	def __init__(self):

		self.mockString = "{ 1, 2, 3, 4 }"


		self.recentString = False

		self.numChannels = False
		self.binaryMode = False
		self.realTime = False

		self.opened = False


	def Open(self):
		
		self.opened = True


	def Close(self):

		self.opened = False


	def IsOpen(self):
		
		return self.opened


	def GetAvailableBytes(self):

		return len(self.mockString) + 1


	def ReadBytes(self, n, buffer_):
		
		buffer_.value = self.mockString


	def WriteBytes(self, n, buffer_):
	
		self.recentString = buffer_


	def ClearInputs(self):
		pass

	def SetNumChannelsAndModes(self, numChannels, binaryMode, realTime):

		self.numChannels = numChannels
		self.binaryMode = binaryMode
		self.realTime = realTime



class MockFile(object):

	mockString = "A\nB"

	def readlines(self):

		return self.mockString.split('\n')