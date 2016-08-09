from collections import deque
import matplotlib.pyplot as plt
import numpy as np

def convolution_filter(samples, n):

	x = []
	y = []
	z = []

	convolution = deque([], n)

	for s in samples:

		# Unsuitable sample 

		if abs(s[0][0]) > 0.15 or abs(s[0][1]) > 0.15 or s[1] < 24:

			if len(convolution) > 0:
				convolution.pop()

			continue 


		convolution.appendleft(s)


		# Take average of samples in the convolution deque

		accum = [0, 0, 0]

		for c in convolution:

			accum[0] += c[0][0] / len(convolution)
			accum[1] += c[0][1] / len(convolution)
			accum[2] += c[1] / len(convolution)


		# Disable convolution
		# accum[0] = s[0][0]
		# accum[1] = s[0][1]
		# accum[2] = s[1]

		x.append(accum[0])
		y.append(accum[1])
		z.append(accum[2])

	return x, y, z



# Sourced from StackOverflow

def colored_line(x, y, z=None, linewidth=1, MAP='jet'):
	# this uses pcolormesh to make interpolated rectangles
	xl = len(x)
	[xs, ys, zs] = [np.zeros((xl,2)), np.zeros((xl,2)), np.zeros((xl,2))]

	# z is the line length drawn or a list of vals to be plotted
	if z == None:
		z = [0]

	for i in range(xl-1):
		# make a vector to thicken our line points
		dx = x[i+1]-x[i]
		dy = y[i+1]-y[i]
		perp = np.array( [-dy, dx] )
		unit_perp = (perp/np.linalg.norm(perp))*linewidth

		# need to make 4 points for quadrilateral
		xs[i] = [x[i], x[i] + unit_perp[0] ]
		ys[i] = [y[i], y[i] + unit_perp[1] ]
		xs[i+1] = [x[i+1], x[i+1] + unit_perp[0] ]
		ys[i+1] = [y[i+1], y[i+1] + unit_perp[1] ]

		if len(z) == i+1:
			z.append(z[-1] + (dx**2+dy**2)**0.5)     
		# set z values
		zs[i] = [z[i], z[i] ] 
		zs[i+1] = [z[i+1], z[i+1] ]

	fig, ax = plt.subplots()
	cm = plt.get_cmap(MAP)
	ax.pcolormesh(xs, ys, zs, shading='gouraud', cmap=cm)
	plt.axis('scaled')
	plt.show()