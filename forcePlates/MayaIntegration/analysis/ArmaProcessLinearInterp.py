
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 23, 2016

## ------------------------------------------------------------------------



import statsmodels.api as sm



class ArmaProcessLinearInterp(object):
	"""

	The cheif concern of this class is to provide a method to linearly interpolate
	between multiple ARMA models based on exogenous values. This is distinct from
	training an exogenous value as in ARMAX.

	>>> 


	"""


	def __init__(self, *args, **kwargs):

		super(self).__init__(*args, **kwargs)


		self.sample_sets = []

		# sm.tsa.ArmaResult({ maparams, arparams })
		




		
	def generate_sample(self, exogs, **kwargs):
		"""

		Mimicks statsmodels' ArmaProcess.generate_sample(n) except we pass an array 
		of exogs instead of an integer.

		"""

		samples = []


		# Take exog to be one-dimensional for now 

		for exog in exogs:

			pass
			
			# self.process.



		return super(self).generate_sample(len(exog), **kwargs)

