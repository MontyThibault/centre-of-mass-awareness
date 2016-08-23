
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: Aug 23, 2016

## ------------------------------------------------------------------------



"""

This module is the bridge between the calibration program thread, the force plates, 
and Maya.

"""


import maya_utils as mu
import maya_socket_connection as msc


# Out stream for the sampling status

PRINT_IN_MAYA_TERMINAL = True


def create_sampling_locator():

	msc.call_func(mu.createLocatorTransformPair, 'sampling_marker')


def _move_sampling_locator_maya(currently_sampling, current_point):
	"""

	Move the Maya sampling marker to the current sampling location on
	state change.

	"""

	p = current_point

	msc.call_func(mu.moveObject, [p[0], 0, p[1]], 'sampling_marker')


def _print_sampling_status(currently_sampling, current_point):
	"""

	This function adds a print-out of the coordinates of the current sampling
	points. It is generic in that it can be called within the Maya Python environment
	or within current Python environment.

	"""

	p = current_point


	# Terminal printout 

	if currently_sampling:

		print "Sampling started at %s" % str(p)
		
	elif not currently_sampling:

		print "Sampling stopped. Next point is %s" % str(p)	


def _update_forces(forces_after_calibration):
	"""

	This is called on when the LabPro recieved a new measurement; we want to update
	Maya's marker sizes, the interpolation of the center marker, etc.

	"""

	msc.call_func(mu.move_markers, forces_after_calibration)


def _create_current_point_obj(kpt):
	"""

	The way the grid class works is by replacing grid.currentPoint with immutable
	tuples, but the grid object itself cannot be pickled to be sent into Maya.

	Here we define a list object that is updated automatically with the values of the 
	tuples, so that we can simply send the list instead of the grid object.

	"""

	l = [0, 0]

	update_callable = lambda _: _update_current_point_obj(l, kpt.generator.grid)
	kpt._currently_sampling.add_listener(update_callable)

	return l


def _update_current_point_obj(l, grid):

	p = grid.currentPoint

	l[0] = p[0]
	l[1] = p[1]


def bind_listeners(kpt, fpt):
	"""

	Bind all the above to the calibration program thread (kpt) through listeners on
	the _currently_sampling attribute.

	"""

	l = _create_current_point_obj(kpt)


	# Sampling locator relocation

	move_locator_callable = lambda cs: _move_sampling_locator_maya(cs, l)
	kpt._currently_sampling.add_listener(move_locator_callable)



	# Sampling printouts

	if PRINT_IN_MAYA_TERMINAL:


		maya_callable = lambda cs: msc.call_func(_print_sampling_status, cs, l)

		kpt._currently_sampling.add_listener(maya_callable)

	else:	

		shell_callable = lambda cs: _print_sampling_status(cs, l)

		kpt._currently_sampling.add_listener(shell_callable)


	# Force updates

	fpt.fp.forces_after_calibration.add_listener(_update_forces)