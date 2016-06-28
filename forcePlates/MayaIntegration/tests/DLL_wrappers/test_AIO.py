from plugin.DLL_wrappers.AIO import aio, AIODevice
import unittest

class TestPAIO(unittest.TestCase):

	def test_access_PAIO_functions(self):
		assert hasattr(aio, 'AioInit')
		assert hasattr(aio, 'AioGetErrorString')

	def test_access_PAIO_constants(self):
		assert hasattr(aio, 'PM10')
		assert hasattr(aio, 'AIOM_CNTM_CARRY_BORROW')

	def test_PAIO_error_wrapping(self):

		def alwaysFails():
			return 10101

		aio._raw.bad = alwaysFails
		assert aio.bad() == 10101

		del aio._raw.bad

	def test_PAIO_device_argument_elision(self):

		def noArguments(deviceID):
			assert deviceID == 123

		aio._raw.noargs = noArguments

		d = AIODevice('name')
		d.deviceID = 123

		d.noargs()

		del aio._raw.noargs