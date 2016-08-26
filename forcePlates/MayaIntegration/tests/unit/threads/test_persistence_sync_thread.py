
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 26, 2016

## ------------------------------------------------------------------------



from plugin.threads.persistence_sync_thread import PersistenceSyncThread as PST

import os
import pytest


@pytest.yield_fixture
def teardown_pickle_files():

	yield

	os.remove('.test.pickle')


def test_persistence_sync_thread_without_starting(teardown_pickle_files):

	x = PST('.test.pickle')
	x.objs['abc'] = 123
	x.objs.close()

	y = PST('.test.pickle')
	assert y.objs['abc'] == 123