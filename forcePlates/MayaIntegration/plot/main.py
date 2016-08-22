
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 19, 2016

## ------------------------------------------------------------------------



import sys
import os

import pickle 


from process import convolution_filter, colored_line

import textwrap

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
import matplotlib.mlab as mlab
from mpl_toolkits.mplot3d import Axes3D

import statsmodels.api as sm
import statsmodels.graphics

import random
import code


def main(filename):

	FPS = 100.0


	with open(filename, 'rb') as f:
		samples = pickle.load(f)


	x, y, z, speed, curvature = convolution_filter(samples, 1, FPS)

	x = x - np.mean(x)
	y = y - np.mean(y)



	# (Autoregression order, moving average order) as per the statsmodels ArmaProcess
	# documentation.
	model_order = (2, 2)


	fit = ARMA_train(x, model_order, FPS)
	ARMA_save(FPS, model_order, fit, filename)



def fft_projection_figure(x, y):

	code.InteractiveConsole(locals()).interact()


	fig = plt.figure()
	ax = fig.gca(projection='3d')

	# ax.plot(x, y, indicies)
	ax.plot(fft[:, 0], fft[:, 1], indicies)

	plt.show()



def speed_histogram(speed):

	n, bins, patches = plt.hist(speed[1:], 100, normed = True)

	plt.title('Centre of Pressure Velocity')
	plt.xlabel('Centre of Pressure Velocity (m/s)')
	plt.ylabel('Relative Frequency')

	plt.grid(True)

	plt.show()



def ARMA_train(x, model_order, FPS):

	indicies = [i / float(FPS) for i in range(len(x))]


	# Fit the process to an ARMA model

	model = sm.tsa.ARMA(x, model_order)
	fit = model.fit()


	return fit


def ARMA_recreate(x, fit):

	# Recreate the ARMA process

	process = sm.tsa.ArmaProcess.from_estimation(fit)


	fake_x = process.generate_sample(len(x))


	r = max(x) / max(fake_x)
	fake_x = [m * r for m in fake_x]


	gt, = plt.plot(indicies, x, 'b', label = 'Ground Truth')
	fsm, = plt.plot(indicies, fake_x, 'r', label = 'Fitted Stochastic Model')

	plt.legend(handles = [gt, fsm])

	plt.title('Centre of Pressure along Single Axis')

	plt.xlabel('Time (s)')
	plt.ylabel('Position (m)')

	plt.show()



def ARMA_save(FPS, model_order, fit, filename):


	with open('data/ArmaModels/' + os.path.basename(filename) + '.py', 'w') as f:

		contents = textwrap.dedent("""

			fps = %s
			model_order = %s
			params = %s

			""" % (FPS, model_order, fit.params.tolist()))


		f.write(contents)





if __name__ == '__main__':

	if len(sys.argv) == 1:

		raise NameError("Must pass filename argument.")

	main(sys.argv[1])