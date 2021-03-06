
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Sep 02, 2016

## ------------------------------------------------------------------------



import pickle 
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

from process import convolution_filter, colored_line



class SampleSet(object):
	"""

	Processing of a single data set with a particular set of parameters.

	"""


	model_order = (3, 3)
	

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

		x = map(lambda s: s[0][0], self.samples)
		y = map(lambda s: s[0][1], self.samples)
		xy = zip(x, y) 

		indicies = [float(i) / self.FPS for i in range(len(x))]


		plt.plot(indicies, x)
		plt.show()


	def fit_arma(self):

		# Fit the process to an ARMA model


		# Note!: currently only fits X!!!

		x = map(lambda s: s[0][0], self.samples)
		y = map(lambda s: s[0][1], self.samples)
		xy = zip(x, y) 


		model = sm.tsa.ARMA(x, self.model_order)
		self.fit = model.fit()


	def recreate(self):

		x = map(lambda s: s[0][0], self.samples)
		y = map(lambda s: s[0][1], self.samples)
		xy = zip(x, y)



		indicies = [float(i) / self.FPS for i in range(len(x))]

		# Recreate the ARMA process

		process = sm.tsa.ArmaProcess.from_estimation(self.fit)
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


		# Power plot

		x_fft = np.fft.fft(x)
		x_fft = abs(x_fft)
		x_fft = x_fft ** 0.5

		forecast_fft = np.fft.fft(forecast)
		forecast_fft = abs(forecast_fft)
		forecast_fft = forecast_fft ** 0.5

		plt.plot(zip(x_fft[:len(x)/5], forecast_fft[:len(x)/5]))
		plt.show()

		



	@staticmethod
	def generate_training_set(samplesets):

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


	@staticmethod
	def convert_exog_to_ar_ma_list(samplesets, exog):

		ar = []
		ma = []

		for e in exog:

			i = 0

			while samplesets[i].stance_width > e:

				if i == len(samplesets) - 1:
					break

				i += 1



			lower = samplesets[i]
			upper = samplesets[i + 1]


			ar.append(lower.fit.ar)
			ma.append(lower.fit.ma)

		return ar, ma