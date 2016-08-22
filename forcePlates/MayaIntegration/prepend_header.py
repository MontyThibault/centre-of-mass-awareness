import sys
import os
import datetime


header = """
##  Centre of Pressure Uncertainty for Virtual Character Control
##  McGill Computer Graphics Lab
## 
##  Released under the MIT license. This code is free to be modified
##  and distributed.
## 
##  Author: Monty Thibault, montythibault@gmail.com
##  Last Updated: %s

## ------------------------------------------------------------------------



""" % datetime.datetime.now().strftime('%b %d, %Y')


folders = ['plugin', 'tests', 'plot']

lines = 0


for folder in folders:

	for root, dirs, files in os.walk(folder):

		# path = root.split('/')


		for file in files:

			if file.endswith('.py'):

				print root + '\\' + file

				with open(root + '/' + file, 'r') as f:

					contents = f.read()

					lines += len(contents.split('\n'))



				# Remove old header if it's there

				cs = contents.split('## ------------------------------------------------------------------------')
				if len(cs) > 1:
					cs = cs[1].lstrip()
				else:
					cs = cs[0].lstrip()


				with open(root + '/' + file, 'w') as f:

					f.write(header + cs)
					

print '%s lines total.' % lines