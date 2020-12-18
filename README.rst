pyLMS
=======

LMS .mat files Reader
---------------------

This module  allows to get raw data from .mat files saved from Siemens LMS TestLab.

Import the package after download
----------------------

.. code-block:: console

	$ pip install pyLMS


Simple example
--------------
.. code-block:: python

	# Import packages
	import pyLMS

	filename = 'data/accelerometro.mat'

	sensor = pyLMS(filename)

	time = sensor['signals']['x']
	acceleration = sensor['signals']['y']
	
	units = sensor['units']
	magnitudes = sensor['magnitudes']
