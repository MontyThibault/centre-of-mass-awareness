from killable_thread import KillableThread

class MainThread(KillableThread):

	fps = 10

	def loop(self):
		print "hello, world again!"