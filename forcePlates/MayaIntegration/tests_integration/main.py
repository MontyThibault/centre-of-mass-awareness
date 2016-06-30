import pytest
import sys


def main():

	overwrite_stdout()

	pytest.main('C:/Users/Monty/Desktop/COMAwareness/forcePlates/MayaIntegration/tests_integration --capture=sys')



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

		return False

	def write(self, *args):

		self.__stdout__.write(*args)


	def flush(self, *args):

		self.__stdout__.flush(*args)