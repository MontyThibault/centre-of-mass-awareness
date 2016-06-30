from killable_thread import KillableThread
import maya.utils


def _callWith(f, *args, **kwargs):
	""" 

	Returns a function that will be called with the given *args and **kwargs. 

	"""

	def g(*_args, **_kwargs):
		f(*args, **kwargs)

	return g



def _defer(f):
	"""

	Wraps the specified function in a maya.utils.executeDeffered(). Should be called
	on a method with `self` as the first argument.

	"""

	def deferred(self, *args):
		maya.utils.executeDeferred(_callWith(f, self))

	return deferred



# Run this in cmd to kill

# from plugin.killable_thread import KillableThread
# KillableThread.killAll()


class MainThread(KillableThread):
	"""

	Simpler looper; executes all tasks inside of the tasks set with self as an argument
	on each frame.

	"""


	fps = 10
	tasks = set()

	@_defer
	def loop(self):
		
		for task in self.tasks:
			task(self)