import unittest

import test_test

def main():



	loader = unittest.TestLoader()

	suite = loader.discover('.')

	testRunner = unittest.runner.TextTestRunner()
	testRunner.run(suite)

