from plugin.window import Window
import unittest


class TestWindow(unittest.TestCase):


	def setUp(self):

		self.cmds = MockMayaEnv()
		Window.all_windows = dict()


	def test_window_init(self):

		w = Window('', self.cmds)


	def test_prevent_duplicates_with_the_same_name(self):

		w1 = Window('name', self.cmds)
		w2 = Window('name', self.cmds)

		assert not w1.alive
		assert w2.alive



class MockMayaEnv(object):
	"""

	Mimicks maya.cmds

	"""

	window_names = set()


	def window(self, name, *args, **kwargs):

		if 'exists' in kwargs:

			return name in self.window_names

		else:

			self.window_names.add(name)


	def deleteUI(self, name, *args, **kwargs):

		self.window_names.remove(name)


	def columnLayout(self, *args, **kwargs):

		pass



	def button(self, *args, **kwargs):

		pass


	def text(self, *args, **kwargs):

		pass


	def showWindow(self, *args, **kwargs):

		pass


	def scriptJob(self, *args, **kwargs):

		pass


