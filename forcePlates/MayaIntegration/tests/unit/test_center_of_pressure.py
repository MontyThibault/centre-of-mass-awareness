
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 19, 2016

## ------------------------------------------------------------------------



from plugin.center_of_pressure import CenterOfPressure, MIN, MAX
import pytest


def test_center_of_pressure_on_update():

	cop = CenterOfPressure(MockGrid())


	cop.on_update([1, 1, 1, 1])

	assert cop.center == [0, 0]

	cop.on_update([1, 0, 0, 0])

	assert cop.center == [-1, -1]


def test_center_of_pressure_limits():

	cop = CenterOfPressure(MockGrid())


	cop.center = [MIN - 10, MAX + 10]
	cop.limits()

	assert cop.center == [MIN, MAX]


class MockGrid(object):

	def corners(self):

		return [(-1, -1), (-1, 1), (1, 1), (1, -1)]