

import collections
import statsmodels.api as sm
import numpy as np
from scipy import signal, optimize, linalg


class DynamicArmaProcess(sm.tsa.ArmaProcess):

	"""

	This class implements our own sample generator that does not use sci.py's lfilter,
	allowing us to change the parameters during sample generation.

	"""


	# Original statsmodels source
	# http://statsmodels.sourceforge.net/devel/_modules/statsmodels/tsa/arima_process.html#ArmaProcess

	def generate_sample(self, nsample=100, scale=1., distrvs=None, axis=0,
						burnin=0):
		'''generate ARMA samples

		Parameters
		----------
		nsample : int or tuple of ints
			If nsample is an integer, then this creates a 1d timeseries of
			length size. If nsample is a tuple, then the timeseries is along
			axis. All other axis have independent arma samples.
		scale : float
			standard deviation of noise
		distrvs : function, random number generator
			function that generates the random numbers, and takes sample size
			as argument
			default: np.random.randn
			TODO: change to size argument
		burnin : integer (default: 0)
			to reduce the effect of initial conditions, burnin observations
			at the beginning of the sample are dropped
		axis : int
			See nsample.

		Returns
		-------
		rvs : ndarray
			random sample(s) of arma process

		Notes
		-----
		Should work for n-dimensional with time series along axis, but not
		tested yet. Processes are sampled independently.
		'''
		if distrvs is None:
			distrvs = np.random.normal
		if np.ndim(nsample) == 0:
			nsample = [nsample]
		if burnin:
			#handle burin time for nd arrays
			#maybe there is a better trick in scipy.fft code
			newsize = list(nsample)
			newsize[axis] += burnin
			newsize = tuple(newsize)
			fslice = [slice(None)]*len(newsize)
			fslice[axis] = slice(burnin, None, None)
			fslice = tuple(fslice)
		else:
			newsize = tuple(nsample)
			fslice = tuple([slice(None)]*np.ndim(newsize))

		eta = scale * distrvs(size=newsize)


		return signal.lfilter(self.ma, self.ar, eta, axis=axis)[fslice]



	def sample_generator(self, scale = 1., distrvs = None):


		if distrvs is None:
			distrvs = np.random.normal

		past_rvs = collections.deque([0] * len(self.ma), len(self.ma))
		past_val = collections.deque([0] * len(self.ar[1:]), len(self.ar[1:]))

		out = []


		while True:

			rnd = scale * distrvs()
			past_rvs.appendleft(rnd)


			# Reimplementing scipy.signal.lfilter
			# See http://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.lfilter.html


			# "The filter function is implemented as a direct II transposed structure. This means that the filter implements:

			# a[0]*y[n] = b[0]*x[n] + b[1]*x[n-1] + ... + b[M]*x[n-M]
			#                       - a[1]*y[n-1] - ... - a[N]*y[n-N]"

			# Where a = self.ar, b = self.ma, y = out and x signal input (random variables in the case of ARMA) 
			# Note: the first AR term is a multiplier for the current y[n], thus omitted below


			# Let MA polynomial equal b[0]*x[n] + b[1]*x[n-1] + ... + b[M]*x[n-M]
			# thus ma_polynomial = past_rvs (dot) self.ma

			ma_polynomial = [b * x for b, x in zip(past_rvs, self.ma)]
			ma_term = sum(ma_polynomial)


			# Let AR polynomial equal a[1]*y[n-1] + ... + a[N]*y[n-N]
			# thus ma_polynomial = past_rvs (dot) self.ma

			ar_polynomial = [a * y for a, y in zip(past_val, self.ar[1:])]
			ar_term = sum(ar_polynomial)


			yn = (ma_term - ar_term) / self.ar[0]
			past_val.appendleft(yn)


			yield yn