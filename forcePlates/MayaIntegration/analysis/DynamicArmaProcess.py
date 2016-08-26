

import collections
import statsmodels.api as sm
import numpy as np
from scipy import signal, optimize, linalg


class DynamicArmaProcess(sm.tsa.ArmaProcess):

	"""

	This class implements our own sample generator that does not use sci.py's lfilter,
	allowing us to change the parameters during sample generation.

	"""


	# Original statsmodels source, unmodified for reference
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


		# TODO: revise this with self.ar_coefs instead of self.ar & self.ma_coefs...
		# Or not

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
			# thus ar_polynomial = past_val (dot) self.ar[1:]

			ar_polynomial = [a * y for a, y in zip(past_val, self.ar[1:])]
			ar_term = sum(ar_polynomial)


			yn = (ma_term - ar_term) / self.ar[0]
			past_val.appendleft(yn)


			yield yn



	def generate_sample_dynamic(self, nsample=100, scale=1., distrvs=None, 
			ma=None, ar=None):
		"""

		This method mostly mimicks the interface of self.generate_sample(), minus
		the bells and whistles.

		@argument ma - an array of length `nsample` where is element is values to be
			substituted into self.ma during the run.
		@argument ar - ditto for self.ar


		"""

		if ma == None or ar == None:

			raise ValueError("MA or AR must be specified in generate_sample_dynamic.")

		if len(ma) != nsample or len(ar) != nsample:

			raise ValueError("Length of MA and AR do not match nsample.")

		if len(ma[0]) != len(self.ma) or len(ar[0]) != len(self.ar):

			# Since the sizes of the deques in generator are static, we must have it
			# the size of self.ma and self.ar match.

			raise ValueError("MA and/or AR do not match existing sizes.")



		gen = self.sample_generator(scale = scale, distrvs = distrvs)
		out = []


		for current_ma, current_ar in zip(ma, ar):

			for i in range(len(current_ma)):
				self.ma[i] = current_ma[i]

			for i in range(len(current_ar)):
				self.ar[i] = current_ar[i]


			out.append(gen.next())


		return out


	@classmethod
	def from_order(cls, order):

		ar = np.array([0] * order[0])
		ma = np.array([0] * order[1])

		return cls.from_coeffs(ar, ma)


	@staticmethod
	def convert_exog_to_ar_ma_list(exog, samplesets):
		"""
	
		

		"""

		return 