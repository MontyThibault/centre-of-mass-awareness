import os
import pickle

class LoadHelper(object):
	""" Keeps calibration data persistent between sessions. This class defines 
	a simple interface from which other functions can read and write aribtrary
	data to a dictionary stored in a file somewhere in the system. """

	# Append to Calibration.py's directory
	calibration_file = os.path.dirname(os.path.realpath(__file__)) + "/calibration/calib.txt"

	@classmethod
	def _getdict(cls):
		file = open(cls.calibration_file, 'rb')
		dictionary = pickle.load(file)
		file.close()

		return dictionary

	@classmethod
	def _savedict(cls, dictionary):
		file = open(cls.calibration_file, 'wb')
		pickle.dump(dictionary, file)
		file.close()

	@classmethod
	def exists(cls, key):
		dictionary = cls._getdict()
		return key in dictionary

	@classmethod
	def load(cls, key):
		return cls._getdict()[key]
	
	@classmethod
	def save(cls, key, value):
		dictionary = cls._getdict()
		dictionary[key] = value

		cls._savedict(dictionary)

	@classmethod
	def delete(cls, key):
		dictionary = cls._getdict()
		dictionary.pop(key, None)

		cls._savedict(dictionary)

	@classmethod
	def clear(cls):
		""" Call this once in case of an "insecure pickle string" error. That means the file is corrupted. """
		cls._savedict({})
