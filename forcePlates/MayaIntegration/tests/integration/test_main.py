# import subprocess
# import time


# TODO: wrestle with this some more


# def test_program_runs_without_error(monkeypatch):

# 	p = subprocess.Popen('python plugin -m', stdin = subprocess.PIPE)

# 	time.sleep()


# 	start = time.time()
# 	max_wait = 5


# 	while p.poll() is None:

# 		p.communicate('kill()')

# 		time.sleep(0.1)

# 		if time.time() - start > max_wait:

# 			assert "Program did not terminate."


# 	p.wait()

# 	assert not p.returncode