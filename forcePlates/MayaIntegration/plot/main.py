
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 18, 2016

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

import code


def main(filename):

	FPS = 100.0


	with open(filename, 'rb') as f:
		samples = pickle.load(f)


	x, y, z, speed, curvature = convolution_filter(samples, 1, FPS)

	x = x - np.mean(x)
	y = y - np.mean(y)

	# colored_line(x, y, z, linewidth = .0001)


	xy = zip(x, y)


	# Turning radius? (curvature)
	# Speed?

	# Variance & covariance

	# Fourier

	# etc.



	# code.InteractiveConsole(locals()).interact()


	# fig = plt.figure()
	# ax = fig.gca(projection='3d')

	# # ax.plot(x, y, indicies)
	# ax.plot(fft[:, 0], fft[:, 1], indicies)

	# plt.show()



	# n, bins, patches = plt.hist(speed[1:], 100, normed = True)

	# plt.title('Centre of Pressure Velocity')
	# plt.xlabel('Centre of Pressure Velocity (m/s)')
	# plt.ylabel('Relative Frequency')

	# plt.grid(True)

	# plt.show()


	indicies = [i / float(FPS) for i in range(len(x))]


	# Fit the process to an ARMA model

	# (Autoregression order, moving average order) as per the statsmodels ArmaProcess
	# documentation.
	model_order = (50, 50)

	model = sm.tsa.ARMA(x, model_order)
	fit = model.fit([-1] * 101)


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

	# plt.show()


	print(fit.params)

	with open('data/ArmaModels/' + os.path.basename(filename) + '.py', 'w') as f:

		contents = textwrap.dedent("""

			fps = %s
			model_order = %s
			params = %s

			""" % (FPS, model_order, fit.params.tolist()))


		f.write(contents)



	# print(results.summary())

	# print(results.params)

	# results.plot()
	# plt.show()
	






	# [X, Y] = np.meshgrid(2 * np.pi * np.arange(200) / 12,
	#                      2 * np.pi * np.arange(200) / 34)

	# S = np.sin(x) + np.cos(y)
	# FS = np.fft.fftn(zip(x, y))

	# plt.imshow(np.log(np.abs(np.fft.fftshift(FS))**2))

	# plt.show()



	# data = np.random.rand(4,4)
	# fig, ax = plt.subplots()
	# heatmap = ax.pcolor(data, cmap=plt.cm.Blues)

	# plt.show()



	# f_xy = np.fft.fftn(xy)

	# plt.imshow(np.log(np.abs(np.fft.fftshift(f_xy))**2))
	# plt.show()





	# ax = plt.subplot(111, projection = 'polar')
	# ax.plot(theta, r, color = 'r', linewidth = 3)

	# ax.grid(True)

	# plt.show()



if __name__ == '__main__':

	if len(sys.argv) == 1:

		raise NameError("Must pass filename argument.")

	main(sys.argv[1])