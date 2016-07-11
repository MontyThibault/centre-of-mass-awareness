

class Observer(object):
	"""

	Simple Python observer implementation.

	Ex.

	>>> obj = Observer()
	>>> obj.set(10)
	>>> obj.get()
	10
	
	>>> obj.add_observer(my_func)
	>>> obj.remove_observer(my_func)

	"""

	def __init__(self):

		self._val = None
		self.listeners = set()


	def set(self, v):

		self._val = v
		self.notify_all()


	def get(self):

		return self._val


	def add_listener(self, f):

		self.listeners.add(f)


	def remove_listener(self, f):

		self.listeners.remove(f)


	def notify_all(self):

		for listener in self.listeners:
			listener(self._val)