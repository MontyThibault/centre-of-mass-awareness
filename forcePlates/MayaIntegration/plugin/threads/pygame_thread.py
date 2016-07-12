import threading
import pygame
import traceback
from Queue import Queue


_exceptions = Queue()

def _exception_wrapper(f):

	def g(*args, **kwargs):

		try:

			f(*args, **kwargs)

		except Exception as e:

			_exceptions.put((e, traceback.format_exc()))


	return g


class PyGameThread(threading.Thread):
	"""

	Invoke a thread of drawing pygame graphics in a new window.
	
	"""

	options = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE


	def __init__(self):
		threading.Thread.__init__(self)

		self.dead = False


		# This lock is necessary so that we do not close the pygame display while
		# the loop() method is running; doing so will result in a "video system not
		# initialized" error.

		# We also use the lock to prevent calling pygame.init() and pygame.quit()
		# concurrently.

		self.pygame_lock = threading.Lock()

		self.draw_tasks_lock = threading.Lock()
		self.draw_tasks = []


	def kill(self):

		with self.pygame_lock:

			self.dead = True
			pygame.quit()


	@_exception_wrapper
	def run(self):

		with self.pygame_lock:
			
			pygame.init()

			self.screen = pygame.display.set_mode((500, 500), self.options)
			clock = pygame.time.Clock()


		while True:

			clock.tick(60)

			with self.pygame_lock:

				if self.dead:
					return

				self.loop()


	def loop(self):

		pygame.event.pump()
		
		for event in pygame.event.get():

			if event.type == pygame.QUIT: 

				self.pygame_lock.release()
				self.kill()

				return 

			elif event.type == pygame.VIDEORESIZE:

				self.screen = pygame.display.set_mode(event.dict['size'],self.options)


		self.screen.fill((255, 255, 255))

		width = self.screen.get_width()
		height = self.screen.get_height()


		# Do some drawing

		with self.draw_tasks_lock:
			for task in self.draw_tasks:
				task(width, height, self.screen, pygame)

		pygame.display.flip()


	@staticmethod
	def query_exceptions():

		while not _exceptions.empty():

			e, tb = _exceptions.get()

			# One could replace this with a non-terminating utility
			# otherwise there isn't much use for a queue

			raise e

			e.task_done()