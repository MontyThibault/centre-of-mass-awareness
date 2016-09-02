
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Sep 02, 2016

## ------------------------------------------------------------------------



import sys
import os


from process import colored_line

import textwrap

import numpy as np
import matplotlib.pyplot as plt


import statsmodels.api as sm
import statsmodels.graphics

import random
import code


from DynamicArmaProcess import DynamicArmaProcess
from SampleSet import SampleSet





def main():

	s0 = SampleSet('data/standing_Monty_0cm')
	s0.stance_width = 0.0
	s0.trim(192, 3911)


	s5 = SampleSet('data/standing_Monty_5cm')
	s5.stance_width = 0.05
	s5.trim(89, 3876)


	s15 = SampleSet('data/standing_Monty_15cm')
	s15.stance_width = 0.15
	s15.trim(176, 4231)


	s30 = SampleSet('data/standing_Monty_30cm')
	s30.stance_width = 0.30
	s30.trim(332, 6157)


	s40 = SampleSet('data/standing_Monty_40cm')
	s40.stance_width = 0.40
	s40.trim(190, 3330)


	samplesets = [s0, s5, s15, s30, s40]

	for sampleset in samplesets:

		sampleset.normalize()
		# sampleset.fit_arma()



	# dap = DynamicArmaProcess.from_order(SampleSet.model_order)
	# dap = DynamicArmaProcess.from_estimation(samplesets[0].fit)

	
	# ar, ma = SampleSet.convert_exog_to_ar_ma_list(samplesets, exog)


	######################

	# samples, exog = SampleSet.generate_training_set(samplesets)

	# x = map(lambda s: s[0][0], samples)
	# y = map(lambda s: s[0][1], samples)
	# xy = zip(x, y) 

	# indicies = [float(i) / 100.0 for i in range(len(x))]

	# exog = [e * 0.022 for e in exog]


	############

	# plt.plot(indicies, zip(x, exog))

	# plt.show()

	s30.fit_arma()
	s30.recreate()

	########################


	# samplesets[0].recreate()


	# samples, exog = SampleSet.generate_training_set(samplesets)
	# s0.samples = samples
	# s0.show_plot()



	# Exogenous variables: crappy
	# Method 2: linearly interpolate params?
	


	# s30.samples = samples
	# s30.show_plot()

	# y = map(lambda s: (s[0][0][0], s[0][0][1], s[1]), zip(samples, exog))
	# plt.plot(y)
	# plt.show()


	# (Autoregression order, moving average order) as per the statsmodels ArmaProcess
	# documentation.
	# model_order = (4, 4, 1)


	# fit = ARMA_train(x, exog, model_order)
	# ARMA_save(FPS, model_order, fit, filename)

	# ARMA_recreate(x, fit, exog, 100)




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

	main()