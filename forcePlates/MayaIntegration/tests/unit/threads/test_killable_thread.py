
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Sep 02, 2016

## ------------------------------------------------------------------------



from plugin.threads.killable_thread import KillableThread, ThreadError
import unittest

class TestKillableThread(unittest.TestCase):

	def test_spawn_killable_thread(self):
		
		class A(KillableThread):
			x = 10
			y = 20

			fps = 60

			def loop(self):
				pass

		a = A()
		a.start()

		assert hasattr(a, 'dead')
		assert hasattr(a, 'kill')

		a.kill()

		assert a.dead == True


	# TODO: how to test a thread exception?


	# def test_killable_thread_should_throw_error_with_no_loop_method(self):

	# 	class A(KillableThread):
	# 		pass

	# 	a = A().start()

	# 	with self.assertRaises(ThreadError):
	# 		a.kill()
			

	def test_spawn_multiple_killable_threads(self):

		class A(KillableThread):
			fps = 1
			def loop(self):
				pass

		class B(KillableThread):
			fps = 1
			def loop(self):
				pass

		a = A()
		b = B()
		a.start()
		b.start()

		KillableThread.killAll()

		assert a.dead == True
		assert b.dead == True