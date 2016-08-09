import pickle
import sys

from collections import deque

from process import convolution_filter, colored_line


import matplotlib.pyplot as plt
import numpy as np


import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

import code


def main(filename):

	FPS = 100


	with open(filename, 'rb') as f:
		samples = pickle.load(f)


	x, y, z = convolution_filter(samples, 5)

	colored_line(x, y, z, linewidth = .0001)


	xy = zip(x, y)
	fft = np.fft.fft(xy)


	indicies = [i / 100.0 for i in range(len(fft))]


	fig = plt.figure()
	ax = fig.gca(projection='3d')

	ax.plot(fft[:, 0], fft[:, 1], indicies)

	plt.show()



	# [X, Y] = np.meshgrid(2 * np.pi * np.arange(200) / 12,
	#                      2 * np.pi * np.arange(200) / 34)

	# S = np.sin(x) + np.cos(y)
	# FS = np.fft.fftn(zip(x, y))

	# plt.imshow(np.log(np.abs(np.fft.fftshift(FS))**2))

	# plt.show()



	# data = np.random.rand(4,4)
	# fig, ax = plt.subplots()
	# heatmap = ax.pcolor(data, cmap=plt.cm.Blues)

	# plt.show()



	# f_xy = np.fft.fftn(xy)

	# plt.imshow(np.log(np.abs(np.fft.fftshift(f_xy))**2))
	# plt.show()





	# ax = plt.subplot(111, projection = 'polar')
	# ax.plot(theta, r, color = 'r', linewidth = 3)

	# ax.grid(True)

	# plt.show()



if __name__ == '__main__':

	if len(sys.argv) == 1:

		raise NameError("Must pass filename argument.")

	main(sys.argv[1])