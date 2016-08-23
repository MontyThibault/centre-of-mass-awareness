


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


		