# TODO: this code is disfunctional and raises an error on import
# Just awful


from ctypes import *
import os


def instance(cls):
	return cls()


@instance
class ForcePlates(object):

	def __init__(self):

		self.measurements = [0, 0, 0, 0]

		

	def inject(self, Calibration, LabProUSB):
		""" 

		This method is used to inject the calibration and LabProUSB dependencies.

		Ex.

		>>> from Affine import Affine
		>>> from LabProUSB import LabProUSB

		>>> f().inject(Affine, LabProUSB)


		"""

		pass

		self.LabProUSB = LabProUSB
		self.calibrations = [Calibration() 
			for i in range(4)]




	# 	self.Open()
	# 	self.SetNumChannelsAndModes(c_int32(4), c_int16(1), c_int16(0))
	# 	self.program()

	# def __del__(self):
	# 	self.blink()
	# 	self.Close()

	# def blink(self):
	# 	self.SendString('s')



	# ############
	# Make this part of LabProUSB

	# def updateMeasurements(self):
	# 	n = self.GetAvailableBytes()
		
	# 	# No new data
	# 	if n == 0:
	# 		return

	# 	n_ = c_int32(n)
	# 	buffer_ = create_string_buffer(n + 1)

	# 	data = self.ReadBytes(byref(n_), buffer_)

	# 	try:
	# 		# Crazy hack
	# 		data = eval(buffer_.value.replace('{', '[').replace('}', ']'))
	# 		self.measurements = data[:4]

	# 		# time_interval = data[4]
	# 	except:
	# 		return


	# @property
	# def forces(self):
	# 	""" Converts from a c_types float array to a native Python number array and applies 
	#    calibration. """

	# 	return [self.calibrations[i].process(self.measurements[i])
	# 			for i in range(4)]


	# def save(self):
	# 	""" Saves calibration on all channels. Load is handled automatically on 
	# 	creation. """
		
	# 	for cal in self.calibrations:
	# 		cal.save()

	# def setAllZero(self):
	# 	""" Sets all sensors to zero. """

	# 	for cal in self.calibrations:
	# 		cal.setZero()

	# def program(self):
	# 	""" Sends a program line-by-line to the LabPro. Thre instruction manual has more 
	# 	information for the specification of such programs. """

	# 	file = open(os.path.dirname(os.path.realpath(__file__)) + 
	# 		'/programs/simple_program.txt', 'r')

	# 	for line in file.readlines():
	# 		self.SendString("s{%s}\n" % line.strip('\n'))
	# 	file.close()