pyLMS
=======

LMS .mat files Reader
---------------------

This module  allows to get raw data from .mat files saved from Siemens LMS TestLab.

Installing the package
----------------------

.. code-block:: console
	$ pip install pyLMS


Simple example
--------------
.. code-block:: python

	# Import packages
	import pyLMS
	import matplotlib.pyplot as plt

	filename = 'data/accelerometro.mat'

	accelerometer = pyLMS(filename)

	plt.plot(accelerometer['signals']['x'], accelerometer['signals']['y'])
	plt.xlabel(accelerometer['magnitudes']['x'] + ' [' + accelerometer['units']['x'] +']')
	plt.ylabel(accelerometer['magnitudes']['y'] + ' [' + accelerometer['units']['y'] +']')
	plt.grid()
