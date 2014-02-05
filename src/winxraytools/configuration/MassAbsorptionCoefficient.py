#!/usr/bin/env python
"""
================================================================================
:mod:`MassAbsorptionCoefficient` -- Type of mass absorption coefficients
================================================================================

.. module:: MassAbsorptionCoefficient
   :synopsis: Type of mass absorption coefficients

.. inheritance-diagram:: wixnrayTools.Configuration.MassAbsorptionCoefficient

"""

# Script information for the file.
__author__ = "Philippe T. Pinard"
__email__ = "philippe.pinard@gmail.com"
__version__ = "0.1"
__copyright__ = "Copyright (c) 2012 Philippe T. Pinard"
__license__ = "GPL v3"

# Standard library modules.

# Third party modules.

# Local modules.

# Globals and constants variables.

TYPE_HEINRICH = 0
TYPE_THINH_LEROUX = 1
TYPE_HENKE = 2

def getLabel(type):
    if type == TYPE_HEINRICH:
        return 'Heinrich (1966) modified by Gauvin'
    elif type == TYPE_THINH_LEROUX:
        return 'Thinh and Leroux (1979)'
    elif type == TYPE_HENKE:
        return 'Henke (1992)'
    else:
        raise ValueError, 'Unknown mass absorption coefficient'
