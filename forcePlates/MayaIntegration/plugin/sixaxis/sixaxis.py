#### Decomissioned

# from ctypes import *

# class SixAxis(object):
# 	def __init__(self, device, channels):
# 		""" Maps a single six-axis sensor to a Maya transform 
# 		Device: An instance of PAIO.AIODevice()
# 		Channels: The channel indicies for the sensor in the following order:
# 			[forceX, forceY, forceZ, torqueX, torqueY, torqueZ] """

# 		self.device = device
# 		self.channels = channels
# 		self.measurements = (c_float * 6)()

# 		if len(channels) != 6:
# 			assert("Error: must give six channels in SixAxis.")

# 		# self.transform = cmds.createNode('transform', name = self.name)
# 		# self.calibration = C.SixAxisCalibrationMatrix(name, load)


# 	def __del__(self):
# 		pass 
		
# 		# cmds.delete(self.transform)

# 	@property
# 	def forces(self):
# 		""" Channels 1 - 3 """

# 		return self.calibration.process(self.measurements)[:3]

# 	@property
# 	def torques(self):
# 		""" Channels 4 - 6 """

# 		return self.calibration.process(self.measurements)[3:]

# 	def updateMeasurements(self):
# 		""" Update sensor measurements. Wrap this in an executeDeferred(). """

# 		ptr = cast(self.measurements, c_voidp).value
# 		for (i, channel) in enumerate(self.channels):
			
# 			slot = cast(ptr + (4 * i), POINTER(c_float))
# 			self.device.AioSingleAiEx(c_short(channel), slot)


# 		# This will feed the data into the calibration object so that the user 
# 		# can set calibrations without accessing the data first.

# 		self.forces
# 		self.torques

# 	def updateTransform(self):
# 		""" Update Maya transform object. Wrap this in an executeDeferred(). """

# 		pass 
# 		# cmds.xform(self.transform, t = self.forces, ro = self.torques)