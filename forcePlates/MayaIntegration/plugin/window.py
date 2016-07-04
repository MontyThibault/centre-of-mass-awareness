
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

			cmds.deleteUI(self.name)



			# Kill previous window

			self.all_windows[self.name].alive = False


		# Replace thyself on Hamlet's thrown

		self.all_windows[self.name] = self
			


		cmds.window(self.name, width = 350, sizeable = False)
		cmds.columnLayout(adjustableColumn = True)

		cmds.showWindow()


	@staticmethod
	def _stripArgs(f):

		def g(*args, **kwargs):
			return f()

		return g


	def button(self, cmds, label, f):
		"""

		Displays a single button on the window.

		"""

		cmds.select(self.name)

		cmds.button(label = label, command = _stripArgs(f))



	def text(self, text):
		"""

		Displays a text label on the window.

		"""

		cmds.select(self.name)

		cmds.text(label = text)