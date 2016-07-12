from plugin.threads.pygame_thread import PyGameThread
import time
import pytest

def test_spin_up_and_kill_pygame_thread():

	# Instantaneous

	pgt = PyGameThread()
	pgt.start()

	pgt.kill()
	pgt.join()

	pgt.query_exceptions()


	# With enough time to initialize the process

	pgt = PyGameThread()
	pgt.start()

	time.sleep(0.1)

	pgt.kill()
	pgt.join()

	pgt.query_exceptions()


def test_exception_handler(monkeypatch):

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