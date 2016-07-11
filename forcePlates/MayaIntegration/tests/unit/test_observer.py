from plugin.observer import Observer

def test_observer_notify():

	c = Observer()

	c.set(5)

	assert c.get() == 5


	triggered = [False]

	def f(c):

		triggered[0] = True


	c.add_listener(f)
	c.set(10)

	assert triggered[0]

	triggered = [False]
	c.remove_listener(f)

	c.set(20)

	assert not triggered[0]

	c.add_listener(f)
	c.notify_all()

	assert triggered[0]