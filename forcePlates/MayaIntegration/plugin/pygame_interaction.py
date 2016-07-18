import line_visualize as lv


def _move_target_pygame(currently_sampling, kpt, tm_v):

	tm_v.point[0] = kpt.generator.grid.currentPoint[0]
	tm_v.point[1] = kpt.generator.grid.currentPoint[1]


	green = (50, 200, 50)
	red = (200, 50, 50)

	if currently_sampling:

		tm_v.color = green

	else:

		tm_v.color = red


def bind_listeners(kpt, pgt, gv):

	# kpt = calibration program thread
	# pgt = pygame thread


	# target marker visualizer
	tm_v = lv.PointVisualizer([0, 0], gv)

	pgt.add_draw_task(tm_v.draw)

	kpt._currently_sampling.add_listener(lambda x: _move_target_pygame(x, kpt, tm_v))