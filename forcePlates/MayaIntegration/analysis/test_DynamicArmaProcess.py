from DynamicArmaProcess import DynamicArmaProcess
import numpy
import pytest


def test_equivalence():

	_equivalence([1], [1])
	_equivalence([1, 2, 3], [1, 2, 3])

	_equivalence([1, -2, 1, -3], [1])
	_equivalence([1], [1, -5, 1, -99])




def _equivalence(ar, ma):

	dap = DynamicArmaProcess(ar, ma)


	def my_distrvs(size = None):

		if size:
			return numpy.add(numpy.zeros(size), 1.0)

		return 1.0

	
	samples_vanilla = dap.generate_sample(nsample = 10, distrvs = my_distrvs).tolist()
	samples_generated = []


	gen = dap.sample_generator(distrvs = my_distrvs)

	for _ in range(10):
		samples_generated.append(gen.next())


	assert samples_vanilla == samples_generated