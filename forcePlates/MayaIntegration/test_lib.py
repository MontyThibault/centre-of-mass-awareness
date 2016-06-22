""" Simple automated scheme for running inline tests. """

methods = []

def test(method):
	methods.append(method)

def runall():
	for method in methods:

		print("Running %s" % method.__name__)

		method()

		print("Test passed!\n")