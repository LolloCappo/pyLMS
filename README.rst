pyLMS
=======
LMS .mat files Reader
---------------------

This module  allows to get raw data from .mat files saved from Siemens LMS TestLab.

Import the package after download
----------------------

.. code-block:: console

	$ from pyLMS import *


Simple example
--------------
.. code-block:: python

	# Import packages
	from pyLMS import *

	filename = 'data/accelerometro.mat'

	sensor = pyLMS(filename)

	time = sensor['signals']['x']
	acceleration = sensor['signals']['y']
	
	units = sensor['units']
	magnitudes = sensor['magnitudes']
