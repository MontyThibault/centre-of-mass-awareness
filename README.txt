Source code lies predominantly in the follwonig folders:

1. Cartwheel/cartwheel-3d

- Mostly forked from the original cartwheel-3d on Google Code.
- Some modifications to /Physics and /Core to enable centre of mass injection.
- Some modifications to /Python for the follwing changes:
	- Differences in user interface
	- Centre of mass sliders (currently non-functional)
	- Dynamic ARMA process reconstruction.


2. forcePlates/MayaIntegration

- Complete original Python source code for centre of mass capture and analysis
- Runs in an anaconda environment with the following module dependencies:
	- scipy & numpy
	- pygame
	- statsmodels

- Old versions of the code in this directory were a functioning plugin that interacted LabPro forceplates with Maya3d. However the current code consists of two stand-alone Python programs with Contec six-axis sensors and pygame.