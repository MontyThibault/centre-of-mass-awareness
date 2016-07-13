from plugin.threads.console_thread import ConsoleThread
import sys

def test_console_thread():

	ct = ConsoleThread({})
	ct.start()

	ct.kill()
	ct.join()