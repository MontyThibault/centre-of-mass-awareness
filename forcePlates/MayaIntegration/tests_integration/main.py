try:

	import pytest

except:

	print "pytest could not be imported (check PATH)"
	

import sys


def main():

	overwrite_stdout()

	pytest.main('C:/Users/Monty/Desktop/COMAwareness/forcePlates/MayaIntegration/tests_integration -s') #--capture=sys')


def overwrite_stdout():

	if not isinstance(sys.stdout, FauxLogger):

		# We save the existing stdout into __stdout__ and rewrite it with our
		# own. This is because pytest expects us to implement isatty(), which
		# the native Maya terminal does not.

		sys.__stdout__ = sys.stdout
		sys.stdout = FauxLogger(sys.__stdout__)


class FauxLogger(object):

	def __init__(self, __stdout__):
		self.__stdout__ = __stdout__


	def isatty(self):

		# We must set this to false, otherwise PyTest will try to colour the 
		# terminal window, resulting in annoying characters everywhere.

		return False


	def __getattr__(self, attr):
		return getattr(self.__stdout__, attr)