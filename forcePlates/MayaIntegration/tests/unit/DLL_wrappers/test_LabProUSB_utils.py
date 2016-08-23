
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 23, 2016

## ------------------------------------------------------------------------



import plugin.DLL_wrappers.LabProUSB_utils as lpuu
import unittest
import ctypes


class TestLabProUSBUtils(unittest.TestCase):

	class MockLabProUSB(object):

		# The following methods are mirrors of those defined in the LabProUSB 
		# dll header file.

		# Note that we work with ctypes objects, namely string buffers and c_ints.


		def __init__(self):
			self.recentString = False


		def Open(self):
			pass

		def Close(self):
			pass

		def IsOpen(self):
			pass

		def GetAvailableBytes(self):

			return len("{ 1, 2, 3, 4 }") + 1


		def ReadBytes(self, n, buffer_):
			
			buffer_.value = "{ 1, 2, 3, 4 }"


		def WriteBytes(self, n, buffer_):
		
			self.recentString = buffer_


		def ClearInputs(self):
			pass

		def SetNumChannelsAndModes(self, numChannels, binaryMode, realTime):
			pass



	def setUp(self):

		self.lp = self.MockLabProUSB()



	def test_send_string(self):

		lpuu.send_string(self.lp, "Hello, World")

		assert self.lp.recentString.value == "Hello, World"


	def test_read_data(self):
		
		assert lpuu.read_data(self.lp).value == "{ 1, 2, 3, 4 }" 


	def test_interpret(self):

		buffer_ = ctypes.create_string_buffer(20)
		buffer_.value = "{ 1, 2, 3, 4 }"

		assert lpuu.interpret(buffer_) == [1, 2, 3, 4]


	def test_read_and_interpret(self):

		assert lpuu.read_and_interpret(self.lp) == [1, 2, 3, 4]