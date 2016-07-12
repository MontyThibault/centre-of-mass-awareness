import threading
import time

class ThreadError(NotImplementedError):
	"""
	The loop method of KillableThread has not been overwritten.
	"""

	pass

class KillableThread(threading.Thread):
	""" 

	Denotes threads with a set framerate that are capable of being killed. The `run` 
	method is provided in this class whereas subtypes are expected to implement a 
	`loop` method as the body of the repeating portion.

	Ex.

	class MyKillableThread(KillableThread):
		
		def __init__(self):
			self.fps = 10

		def loop(self):
			print 'hello, world ten times per second!'

	>>> mkt = MyKillableThread().start()

	hello, world ten times per second!
	hello, world ten times per second!
	...

	>>> mkt.kill()
	OR
	>>> KillableThread.killAll()

	"""


	objs = set()

	def __init__(self):
		threading.Thread.__init__(self)
		
		self.objs.add(self)
		self.dead = False

		self.fps = 1
		

	def __del__(self):
		threading.Thread.__del__(self)
		
		self.dead = True
		self.objs.remove(self)
			
	def kill(self):
		self.dead = True

	@classmethod
	def killAll(cls):
		for obj in cls.objs:
			obj.kill()

	def run(self):

		while not self.dead:

			self.loop()

			time.sleep(1.0 / self.fps)


	# The following should be overridden in subtypes. A `ThreadError` will be raised
	# if the default method is used.

	def loop(self):
		raise ThreadError("Loop method not overwritten.")