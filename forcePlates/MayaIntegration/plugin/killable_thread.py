import threading

# TODO - override the loop function to die automatically??

class KillableThread(threading.Thread):
	objs = set()

	def __init__(self):
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