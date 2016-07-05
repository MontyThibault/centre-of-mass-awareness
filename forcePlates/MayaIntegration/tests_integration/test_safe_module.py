# from utils.safe_module_wrapper import safe_module_wrapper

# def test_safe_module_wrapper_wraps():

# 	@safe_module_wrapper
# 	def f():

# 		return True


# 	assert f()


# def test_safe_module_wrapper_reimport_module():

# 	@safe_module_wrapper
# 	def f():

# 		import unittest

# 		assert unittest.TestCase

# 	def mess_up():

# 		import unittest

# 		unittest.TestCase = False


# 	f()

# 	mess_up()

# 	f()