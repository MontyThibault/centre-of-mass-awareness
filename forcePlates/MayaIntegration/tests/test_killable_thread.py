from plugin.killable_thread import KillableThread
import unittest

class TestKillableThread(unittest.TestCase):

	def test_spawn_killable_thread(self):
		
		class A(KillableThread):
			x = 10
			y = 20

			def run(self):
				pass

		a = A()
		a.start()

		assert hasattr(a, 'dead')
		assert hasattr(a, 'kill')

		a.kill()

		assert a.dead == True

	def test_spawn_multiple_killable_threads(self):

		class A(KillableThread):
			def run(self):
				pass

		class B(KillableThread):
			def run(self):
				pass

		a = A()
		b = B()
		a.start()
		b.start()

		KillableThread.killAll()

		assert a.dead == True
		assert b.dead == True