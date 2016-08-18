
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 18, 2016

## ------------------------------------------------------------------------



from plugin.DLL_wrappers.LabProUSB import LabProUSB, LabProUSBError, _ErrorWrapper
import unittest


class TestLabProUSB(unittest.TestCase):

	def test_error_wrapper_on_passing(self):
			
		def returns_pass():
			return 0

		e = _ErrorWrapper(returns_pass)

		# Should not raise error
		e()


	def test_error_wrapper_on_failing(self):
		
		def returns_error():
			return -1

		e = _ErrorWrapper(returns_error)

		with self.assertRaises(LabProUSBError):
			e()



	def test_function_calls(self):

		pass

	def test_function_errors(self):

		pass

	def test_function_elision(self):

		pass