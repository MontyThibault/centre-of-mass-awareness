import plugin.line_visualize as lv
import pytest


@pytest.fixture
def simple_sample_set():

	return [
		((0, 0), (1, 1), 10),
		((0, 0), (-1, -1), 20)
	]


@pytest.fixture
def corners():

	return [
		(-10, -10),
		(-10, 10),
		(10, 10),
		(10, -10)
	]


def _instance(f):
	return f()


@pytest.fixture
def pygame():

	@_instance
	class pygame(object):
		
		@_instance
		class draw(object):
			pass

		@_instance
		class display(object):
			pass


	return pygame


@pytest.fixture
def screen():

	@_instance
	class screen(object):
		pass

	return screen


def test_mix_max_normalizer():

	o = (0, 0)
	samples = [(o, o, 1), (o, o, 2)]

	f = lv._generate_min_max_normalizer(samples, -1, 1)

	assert f(samples[0][2]) == -1
	assert f(samples[1][2]) == 1



# Test identity functionality for incomplete data
# {

def test_min_max_normalizer_no_data():

	samples = []

	f = lv._generate_min_max_normalizer(samples, -1, 1)

	assert f(2) == 2


def test_min_max_normalizer_one_sample():

	samples = [((0, 0), (0, 0), 0)]

	f = lv._generate_min_max_normalizer(samples, -1, 1)

	assert f(2) == 2

# }


class MockGrid(object):

	def __init__(self):
		self.l = 10
		self.w = 10


	def points(self):
		return [(-10, -10), (10, 10)]



def test_grid_visualizer_coordinate_conversions(screen, pygame):

	mock_grid = MockGrid()
	gv = lv.GridVisualizer(mock_grid)

	gv.set_wh(200, 200)

	assert gv.screen_to_grid((200, 200)) == (10, 10)	
	assert gv.screen_to_grid((0, 0)) == (-10, -10)

	assert gv.grid_to_screen((10, 10)) == (200, 200)
	assert gv.grid_to_screen((-10, -10)) == (0, 0)