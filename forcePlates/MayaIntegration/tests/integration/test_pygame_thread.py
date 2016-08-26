
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 26, 2016

## ------------------------------------------------------------------------



from plugin.threads.pygame_thread import PyGameThread
import time
import pytest


@pytest.fixture
def restart_pygame():

	import pygame
	
	pygame.init()
	pygame.quit()


def test_spin_up_and_kill_pygame_thread(restart_pygame):

	# Instantaneous

	pgt = PyGameThread()
	pgt.start()

	pgt.kill()
	pgt.join()

	pgt.query_exceptions()


	# With enough time to initialize the process

	pgt = PyGameThread()
	pgt.start()

	pgt.kill()

	time.sleep(0.1)

	pgt.join()

	pgt.query_exceptions()


def test_exception_handler(restart_pygame, monkeypatch):

	class ArbitraryError(Exception):
		pass

	def bad_func():
		raise ArbitraryError


	pgt = PyGameThread()

	monkeypatch.setattr(pgt, 'loop', bad_func)

	pgt.start()
	pgt.join()


	with pytest.raises(ArbitraryError):
		pgt.query_exceptions()


def test_drawing_tasks(restart_pygame):

	pgt = PyGameThread()
	pgt.start()


	def draw(w, h, screen, pygame):

		pygame.draw.line(screen, (255, 0, 0), (0, 0), (w, h), 10)


	pgt.add_draw_task(draw)


	time.sleep(0.1)

	pgt.kill()
	pgt.join()

	pgt.query_exceptions()