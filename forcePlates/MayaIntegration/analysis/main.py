
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 23, 2016

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



class SampleSet(object):

	model_order = (2, 2)
	

	def __init__(self, filename):

		with open(filename, 'rb') as f:
			self.samples = pickle.load(f)


		self.FPS = 100.0
		self.stance_width = 0.0

		self.fit = None


	def convolve(self, n):

		self.samples = convolution_filter(self.samples, n)


	def normalize(self):

		x = []
		y = []

		for sample in self.samples:

			x.append(sample[0][0])
			y.append(sample[0][1])


		x = x - np.mean(x)
		y = y - np.mean(y)


		for i, sample in enumerate(self.samples):

			new_sample = ((x[i], y[i]), sample[1])

			self.samples[i] = new_sample


	def trim(self, start, stop):

		self.samples = self.samples[start:stop]


	def show_plot(self):

		xy = map(lambda s: (s[0][0], s[0][1]), self.samples)

		plt.plot(xy)
		plt.show()


	def fit(self):

		# Fit the process to an ARMA model

		model = sm.tsa.ARMA(self.samples, self.model_order)
		self.fit = model.fit()



	def recreate(self):

		x = map(lambda s: s[0][0], self.samples)
		y = map(lambda s: s[0][1], self.samples)
		xy = zip(x, y)



		indicies = [float(i) / FPS for i in range(len(x))]

		# Recreate the ARMA process

		process = sm.tsa.ArmaProcess.from_estimation(fit)
		forecast = process.generate_sample(len(x))


		# forecast = 
		# forecast, strerr, conf_int = fit.forecast(len(x), exog)


		r = max(x) / max(forecast)
		forecast = [m * r for m in forecast]


		gt, = plt.plot(indicies, x, 'b', label = 'Ground Truth')
		fsm, = plt.plot(indicies, forecast, 'r', label = 'Fitted Stochastic Model')

		plt.legend(handles = [gt, fsm])

		plt.title('Centre of Pressure along Single Axis')

		plt.xlabel('Time (s)')
		plt.ylabel('Position (m)')

		plt.show()



	@classmethod
	def generate_training_set(cls, samplesets):

		mega_samples = []

		for sampleset in samplesets:
			mega_samples += sampleset.samples



		mega_exog = []


		for sampleset in samplesets:

			num_samples = len(sampleset.samples)
			exog_var = sampleset.stance_width
			uniform_exog = [exog_var] * num_samples

			mega_exog += uniform_exog


		return mega_samples, mega_exog




def main(filename):

	s0 = SampleSet('data/standing_Monty_0cm')
	s0.stance_width = 0.0
	s0.trim(192, 3911)
	s0.normalize()


	s5 = SampleSet('data/standing_Monty_5cm')
	s5.stance_width = 0.05
	s5.trim(89, 3876)
	s5.normalize()


	s15 = SampleSet('data/standing_Monty_15cm')
	s15.stance_width = 0.15
	s15.trim(176, 4231)
	s15.normalize()


	s30 = SampleSet('data/standing_Monty_30cm')
	s30.stance_width = 0.30
	s30.trim(332, 6157)
	s30.normalize()


	s40 = SampleSet('data/standing_Monty_40cm')
	s40.stance_width = 0.40
	s40.trim(190, 3330)
	s40.normalize()



	# Note: attempt exog with 2d matrix

	samples, exog = SampleSet.generate_training_set([s0, s5, s15, s30, s40])
	# samples, exog = SampleSet.generate_training_set([s0, s40])


	x = map(lambda s: s[0][0], samples)
	y = map(lambda s: s[0][1], samples)
	xy = zip(x, y)



	# Exogenous variables: crappy
	# Method 2: linearly interpolate params?
	


	# s30.samples = samples
	# s30.show_plot()

	# y = map(lambda s: (s[0][0][0], s[0][0][1], s[1]), zip(samples, exog))
	# plt.plot(y)
	# plt.show()


	# (Autoregression order, moving average order) as per the statsmodels ArmaProcess
	# documentation.
	model_order = (4, 4, 1)


	fit = ARMA_train(x, exog, model_order)
	# ARMA_save(FPS, model_order, fit, filename)

	ARMA_recreate(x, fit, exog, 100)




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



def ARMA_train(samples, exog, model_order):


	# Fit the process to an ARMA model

	model = sm.tsa.ARMA(samples, model_order, exog = exog)
	fit = model.fit()


	return fit


def ARMA_recreate(x, fit, exog, FPS):

	indicies = [float(i) / FPS for i in range(len(x))]

	# Recreate the ARMA process

	process = sm.tsa.ArmaProcess.from_estimation(fit)
	forecast = process.generate_sample(len(x))


	# forecast = 
	# forecast, strerr, conf_int = fit.forecast(len(x), exog)


	r = max(x) / max(forecast)
	forecast = [m * r for m in forecast]


	gt, = plt.plot(indicies, x, 'b', label = 'Ground Truth')
	fsm, = plt.plot(indicies, forecast, 'r', label = 'Fitted Stochastic Model')

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