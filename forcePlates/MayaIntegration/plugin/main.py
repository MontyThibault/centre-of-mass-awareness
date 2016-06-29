from main_thread import MainThread


# from plugin.killable_thread import KillableThread
# KillableThread.killAll()


def main():

	print "hey, world"

	mt = MainThread()
	mt.start()

	mt.tasks.add(loopsy)


def loopsy():
	print "looping"