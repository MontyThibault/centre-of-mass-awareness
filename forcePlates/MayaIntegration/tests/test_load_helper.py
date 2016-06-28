from plugin.load_helper import LoadHelper
import unittest


class TestLoadHelper(unittest.TestCase):

	def test_save_and_delete_new_persistent_entry(self):

		LoadHelper.save('test', hash(self))
		assert LoadHelper.load('test') == hash(self)

		LoadHelper.delete('test')
		assert not LoadHelper.exists('test')


	def test_calibrate_matrix_test_and_save(self):

		x = SixAxisCalibrationMatrix()

		assert x.process([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

		x.matrix[2][3] = 1
		assert x.process([0, 0, 0, 1, 0, 0]) == [0, 0, 1, 1, 0, 0]

		x.name = 'test'
		x.save()

		x.matrix[2][3] = 0

		x.load()
		assert x.process([0, 0, 0, 1, 0, 0]) == [0, 0, 1, 1, 0, 0]

		x.delete()