import plugin.load_helper as lh
import unittest


class TestLoadHelper(unittest.TestCase):

	def test_save_and_delete_new_persistent_entry(self):

		lh.save('test', hash(self))
		assert lh.load('test') == hash(self)

		lh.delete('test')
		assert not lh.exists('test')