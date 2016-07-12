import threading
import pygame


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


	def kill(self):

		with self.pygame_lock:

			self.dead = True
			pygame.quit()


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
		pygame.display.flip()