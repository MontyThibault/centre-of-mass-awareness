
class Window(object):
	"""

	This class represents an object-oriented abstraction over Maya's API handling windows.


	"""

	all_windows = dict()


	def __init__(self, name, cmds):

		self.name = name
		self.alive = True


		# Prevent duplicates

		if cmds.window(self.name, exists = True):

			self.all_windows[self.name].delete(cmds)


		# Replace thyself on Hamlet's thrown

		self.all_windows[self.name] = self
			


		cmds.window(self.name, width = 350, sizeable = False)
		cmds.columnLayout(adjustableColumn = True)
		

		cmds.showWindow()


	def delete(self, cmds):
		"""

		Removes this window.

		"""

		cmds.deleteUI(self.name)

		self.alive = False

		self.all_windows.pop(self.name)


	@staticmethod
	def _stripArgs(f):

		def g(*args, **kwargs):
			return f()

		return g


	def button(self, label, f, cmds):
		"""

		Displays a single button on the window.

		"""

		cmds.button(label = label, command = self._stripArgs(f))
		cmds.showWindow()



	def text(self, text, cmds):
		"""

		Displays a text label on the window.

		"""

		cmds.text(label = text)
