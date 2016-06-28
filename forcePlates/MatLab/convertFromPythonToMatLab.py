##
## This script converts the grid calibration data present in MayaIntegration/calibration/calib.txt
## to a MatLab source file. It requires SciPy, which can be run on Windows from the Python executable
## bundled with an Anaconda installation.
##

import scipy.io
import pickle
import os

path = os.path.dirname(os.path.realpath(__file__)) + "/../MayaIntegration/calibration/calib.txt"

calib = open(path, 'rb')
obj = pickle.load(calib)

scipy.io.savemat('calib.mat', obj)