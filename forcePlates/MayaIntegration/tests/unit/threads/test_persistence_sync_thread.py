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