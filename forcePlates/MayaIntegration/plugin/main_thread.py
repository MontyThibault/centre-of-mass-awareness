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

	Wraps the specified function in a maya.utils.executeDeffered().

	"""

	def deferred(self, *args):
		maya.utils.executeDeferred(_callWith(f, self))

	return deferred



class MainThread(KillableThread):

	fps = 10
	tasks = set()

	@_defer
	def loop(self):
		
		for task in self.tasks:
			task()