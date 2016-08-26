
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 26, 2016

## ------------------------------------------------------------------------



from ctypes import *
import os

def instance(cls):
	return cls()


class LabProUSBError(Exception):
	pass


@instance
class LabProUSB(object):
	""" 

	Load the library only once & prints error message given the common return pattern 
	is `0 -> success. Less than 0 -> failure`. See `LabProUSB_interface.h for function 
	descriptions. 

	"""


	# Load dependency

	cdll.LoadLibrary(os.path.dirname(os.path.realpath(__file__)) + 
		"/../../../LabProUSB_SDK/redist/LabProUSB_lib/win64/wdapi921.dll")

	# Load library

	_raw = cdll.LoadLibrary(
		os.path.dirname(os.path.realpath(__file__)) + 
		"/../../../LabProUSB_SDK/redist/LabProUSB_lib/win64/LabProUSB.dll")



	# The following functions do not conform to the `0 -> success. Less than 0 -> failure`
	# pattern and must be specified independently.

	def Close(self):
		self._raw.LabProUSB_Close()

	def IsOpen(self):
		return self._raw.LabProUSB_Close()

	def __getattr__(self, key):
		return _ErrorWrapper(getattr(self._raw, "LabProUSB_" + key))



class _ErrorWrapper(object):
	def __init__(self, f):
		self.f = f

	def __call__(self, *args, **kwargs):
		errorCode = self.f(*args, **kwargs)

		if errorCode < 0:

			code = "%s = %s : Returned unsuccessful." % (self.f.__name__, errorCode)
			raise LabProUSBError(code)


		returnValue = errorCode
		return returnValue