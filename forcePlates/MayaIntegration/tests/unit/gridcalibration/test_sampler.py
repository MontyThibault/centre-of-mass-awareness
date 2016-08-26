
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 26, 2016

## ------------------------------------------------------------------------



from plugin.gridcalibration.sampler import Sampler
import unittest

class SamplerTest(unittest.TestCase):

	def test_average_samples(self):

		samples = [
			((0, 0), (-3, -3), 0),
			((0, 0), (3, 3), 1),
			((0, 0), (0, 0), -1)
		]

		assert Sampler._averageSamples(samples) == ((0, 0), (0, 0), 0)


	def test_weighted_average_samples(self):

		samples = [
			((0, 0), (0, 0), 0),
			((0, 0), (3, 3), 6)
		]

		weights = [
			1,
			2
		]

		weightedSamples = zip(samples, weights)

		assert Sampler._averageWeightedSamples(weightedSamples) == ((0, 0), (2, 2), 4)

	def test_fetch_best_sample_spot_on(self):

		samples = [
			((0, 0), (8, -7), 0),
			((0, 0), (1, 1), 1),
			((0, 0), (-10, 2), 3)
		]

		x = Sampler(samples)
		
		assert x.closest((0, 0), 0) == ((0, 0), (8, -7), 0)

	def test_fetch_closest_sample_without_exact_match(self):

		samples = [
			((0, 0), (8, -7), 0),
			((0, 0), (1, 1), 1),
			((0, 0), (-10, 2), 4)
		]

		x = Sampler(samples)
		
		assert x.closest((0, 0), 2) == ((0, 0), (1, 1), 1)

	def test_simple_composite_sample(self):

		samples = [
			((0, 0), (442, -33), -1.1),
			((0, 0), (0, 0), -1),
			((0, 0), (-3, -3), 0),
			((0, 0), (3, 3), 1),
			((0, 0), (-54, 999), 1.36)
		]

		s = Sampler(samples)

		assert s.simpleComposite((0, 0), 0, 1) == ((0, 0), (0, 0), 0)