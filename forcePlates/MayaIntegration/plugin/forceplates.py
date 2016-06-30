from ctypes import *

import DLL_wrappers.LabProUSB_utils as lpuu
import os


class ForcePlates(object):

	def __init__(self):
		self.forces = [0, 0, 0, 0]


	def init_calibs(self, Calibration):
		""" 

		This method is used to inject the calibration dependency.

		Ex.

		>>> from Affine import Affine

		>>> f().initCalibrations(Affine)


		"""

		self.calibrations = [Calibration() 
			for i in range(4)]


	def init_labpro(self, labpro):
		""" 

		Initializes the LabPro state.

		"""

		labpro.Open()
		labpro.SetNumChannelsAndModes(c_int32(4), c_int16(1), c_int16(0))

	def uninit_labpro(self, labpro):
		""" 

		Uninitializes the LabPro state.

		"""

		self.blink() # 
		labpro.Close()



	def update(self, labpro):
		""" 

		Updates the force measurements from the LabPro. 

		"""

		data = lpuu.read_and_interpret(labpro)


		if data is not None:
				
				self.forces = data
				

	def forces_with_calibs(self):
		""" 

		Applies calibrations to the forces and returns the new array. 

		"""

		return [self.calibrations[i].process(self.forces[i])
				for i in range(4)]



	def set_all_zero(self):
		""" 

		Sets all sensors to zero. 

		"""

 		for cal in self.calibrations:
	 		cal.setZero()


	def blink(self, labpro):
	 	"""

	 	Kills program.


	 	"""

		lpuu.send_string(labpro, 's')



	def send_program(self, labpro, file):
		""" 

		Sends a program line-by-line to the LabPro. Since the format s{ ... } is
		required for all instructions, it is added here automatically. The instruction 
		manual has more information for the specification of such programs. 

		"""

		for line in file.readlines():
			lpuu.send_string(labpro, "s{%s}\n" % line.strip('\n'))