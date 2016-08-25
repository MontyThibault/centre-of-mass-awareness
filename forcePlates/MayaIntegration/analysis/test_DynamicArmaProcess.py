from DynamicArmaProcess import DynamicArmaProcess
import numpy
import pytest


def test_equivalence():

	_equivalence([1], [1])
	_equivalence([1, 2, 3], [1, 2, 3])

	_equivalence([-1, -2, 1, -3], [-1])
	_equivalence([1], [1, -5, 1, -99])



def one_distrvs(size = None):

	if size:
		return numpy.add(numpy.zeros(size), 1.0)

	return 1.0


def _equivalence(ar, ma):

	dap = DynamicArmaProcess(ar, ma)

	samples_vanilla = dap.generate_sample(nsample = 10, distrvs = one_distrvs).tolist()
	samples_generated = []


	gen = dap.sample_generator(distrvs = one_distrvs)

	for _ in range(10):
		samples_generated.append(gen.next())


	assert samples_vanilla == samples_generated



def test_dynamic_arma():
	"""

	Tests to see we can indeed change the ar and ma parameters mid-sampling.

	"""

	ar = [1, 99, 99]
	ma = [1, 99, 99]

	dap = DynamicArmaProcess(ar, ma)

	gen = dap.sample_generator(distrvs = one_distrvs)

	gen.next()
	gen.next()
	gen.next()

	dap.ar = [1, 0, 0]
	dap.ma = [1, 0, 0]

	assert gen.next() == 1



def test_sample_dynamic():

	ar = [1, 99, 99]
	ma = [1, 99, 99]


	nsamples = 10

	ar_dyn = [ar] * nsamples
	ma_dyn = [ma] * nsamples

	dap = DynamicArmaProcess(ar, ma)


	gsd = dap.generate_sample_dynamic(nsample = nsamples, distrvs = one_distrvs, ma = ma_dyn, ar = ar_dyn)
	gs = dap.generate_sample(nsample = nsamples, distrvs = one_distrvs).tolist()

	assert gsd == gs