
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

import threading
import os

from observable import Observable

from plugin.threads.killable_thread import KillableThread

from plugin.DLL_wrappers.LabProUSB import LabProUSB
import DLL_wrappers.LabProUSB_utils as lpuu

from plugin.calibration.affine import Affine


class ForcePlates(object):

	def __init__(self):

		self.forces = Observable([0, 0, 0, 0])
		self.forces_after_calibration = Observable([0, 0, 0, 0])

		self.calibrations = False


	def init_calibs(self):
		""" 

		This method is used to inject the calibration dependency.

		Ex.

		>>> from Affine import Affine

		>>> f().initCalibrations(Affine)


		"""

		self.calibrations = [Affine() 
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

		self.blink(labpro) 
		labpro.Close()



	def update(self, labpro):
		""" 

		Updates the force measurements from the LabPro. 

		"""

		data = lpuu.read_and_interpret(labpro)

		if data is not None:

			self.forces.set(data[:4])

			if self.calibrations:

				fac = self.forces_with_calibs()
				self.forces_after_calibration.set(fac)
				

	def forces_with_calibs(self):
		""" 

		Applies calibrations to the forces and returns the new array. 

		"""

		f = self.forces.get()

		return [self.calibrations[i].process(f[i])
				for i in range(4)]



	def set_all_zero(self):
		""" 

		Sets all sensors to zero. 

		"""

 		for cal in self.calibrations:
	 		cal.setZeroLast()


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



class ForcePlatesThread(KillableThread):
	""" 

	Keep forces syncronized.

	"""
	
	def __init__(self, fp):
		KillableThread.__init__(self)

		self.fps = 60
		self.fp = fp


	def loop(self):
		self.fp.update(LabProUSB)