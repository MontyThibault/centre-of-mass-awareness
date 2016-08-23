
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 23, 2016

## ------------------------------------------------------------------------



import stastsmodels.api as sm



class ArmaProcessLinearInterp(sm.tsa.ArmaProcess):
	"""

	The cheif concern of this class is to provide a method to linearly interpolate
	between multiple ARMA models based on exogenous values. This is distinct from
	training an exogenous value as in ARMAX.

	>>> 


	"""


	def __init__(self, *args, **kwargs):

		super(self).__init__(*args, **kwargs)


		