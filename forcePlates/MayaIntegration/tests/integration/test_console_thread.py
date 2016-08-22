
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 19, 2016

## ------------------------------------------------------------------------



from plugin.threads.console_thread import ConsoleThread
import sys

def test_console_thread():

	ct = ConsoleThread({})
	ct.start()

	ct.kill()
	ct.join()