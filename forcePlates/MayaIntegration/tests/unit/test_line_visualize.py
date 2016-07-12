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



#
# What do these do? {

def test_visualize_empty(corners, pygame, screen):

	f = lv.generate_sample_visualizer([], corners)

	f(20, 20, screen, pygame)


def test_visualize_simple_samples(corners, pygame, screen, simple_sample_set):

	f = lv.generate_sample_visualizer(simple_sample_set, corners)

	f(20, 20, screen, pygame)

# }


class MockGrid(object):

	def __init__(self):
		self.l = 10
		self.w = 10


def test_grid_visualizer_coordinate_conversions(screen, pygame):

	mock_grid = MockGrid()
	f, screen_to_grid, grid_to_screen = lv.generate_grid_visualizer(mock_grid)


	# width - 200
	# height - 200

	f(200, 200, screen, pygame)

	assert screen_to_grid((200, 200)) == (10, 10)	
	assert screen_to_grid((0, 0)) == (-10, -10)

	assert grid_to_screen((10, 10)) == (200, 200)
	assert grid_to_screen((-10, -10)) == (0, 0)