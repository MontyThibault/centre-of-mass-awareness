""" 

Keeps calibration data persistent between sessions. This class defines 
a simple interface from which other functions can read and write aribtrary
data to a dictionary stored in a file somewhere in the system. 

An "insecure pickle string" error means the file is corrupted. Call clear()
once.

"""

import os
import pickle


# Append to Calibration.py's directory
calibration_file = os.path.dirname(os.path.realpath(__file__)) + "/calibration/calib.txt"


def _getdict():
	file = open(calibration_file, 'rb')
	dictionary = pickle.load(file)
	file.close()

	return dictionary

def _savedict(dictionary):
	file = open(calibration_file, 'wb')
	pickle.dump(dictionary, file)
	file.close()

def exists(key):
	dictionary = _getdict()
	return key in dictionary

def load(key):
	return _getdict()[key]

def save(key, value):
	dictionary = _getdict()
	dictionary[key] = value

	_savedict(dictionary)

def delete(key):
	dictionary = _getdict()
	dictionary.pop(key, None)

	_savedict(dictionary)

def clear():
	_savedict({})