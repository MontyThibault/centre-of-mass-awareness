from plugin.center_of_pressure import CenterOfPressure
import pytest


def test_center_of_pressure_on_update():

	cop = CenterOfPressure(MockGrid())


	cop.on_update([1, 1, 1, 1])

	assert cop.center == [0, 0]

	cop.on_update([1, 0, 0, 0])

	assert cop.center == [-1, -1]



class MockGrid(object):

	def corners(self):

		return [(-1, -1), (-1, 1), (1, 1), (1, -1)]