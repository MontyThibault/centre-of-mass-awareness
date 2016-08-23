
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 23, 2016

## ------------------------------------------------------------------------



"""

This module defines useful utilities over the LabProUSB library.

"""

from ctypes import *


def send_string(LabProUSB, string):
	"""

	Sends a string to the LabPro device. 

	Ex. 

	>>> send_string(labpro, "s")

	*blink*

	"""


	length = c_int32(len(string) + 1)
	encoded = string.encode('ASCII')

	LabProUSB.WriteBytes(byref(length), c_char_p(encoded))



def read_data(LabProUSB):
	""" 

	Checks for available data on the LabPro and reads it into a ctypes buffer.

	Ex.

	>>> string = read_data(labpro)
	>>> string
	<ctypes.c_char_Array_8 object at 0x028B9850>

	>>> string.value
	"Example"

	"""

	n = LabProUSB.GetAvailableBytes()
	
	# No new data
	if n == 0:
		return

	n_ = c_int32(n)
	buffer_ = create_string_buffer(n + 1)

	LabProUSB.ReadBytes(byref(n_), buffer_)

	return buffer_


def interpret(buffer_):
	""" 

	Evaluates a string buffer to be interpreted as a Python object, replacing curlies
	with squares.

	Ex.

	>>> buffer_.value
	"{ 1, 2, 3, 4 }"
	
	>>> interpret(buffer_)
	[1, 2, 3, 4]

	"""


	try:
		# Crazy hack
		data = eval(buffer_.value.replace('{', '[').replace('}', ']'))
		return data

	except:
		return


def read_and_interpret(LabProUSB):

	buffer_ = read_data(LabProUSB)
	return interpret(buffer_)