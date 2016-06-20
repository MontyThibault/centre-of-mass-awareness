import unittest
import threading

class KillableThread(threading.Thread):
	objs = set()

	def __init__(self):

		print('hello, world')

		threading.Thread.__init__(self)
		
		self.objs.add(self)
		self.dead = False

	def __del__(self):
		self.objs.remove(self)
			
	def kill(self):
		self.dead = True

	@classmethod
	def killAll(cls):
		for obj in cls.objs:
			obj.kill()


class Tests(object):
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