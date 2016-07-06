from subprocess import call

def test_persistence():

	call(['python', 'part1.py'])
	assert call(['python', 'part2.py'])