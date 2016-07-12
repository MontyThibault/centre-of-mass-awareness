from plugin.threads.pygame_thread import PyGameThread
import time

def test_spin_up_and_kill_pygame_thread():

	# Instantaneous

	pgt = PyGameThread()
	pgt.start()

	pgt.kill()
	pgt.join()


	# With enough time to initialize the process

	pgt = PyGameThread()
	pgt.start()

	time.sleep(0.1)

	pgt.kill()
	pgt.join()