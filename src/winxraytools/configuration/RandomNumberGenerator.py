#!/usr/bin/env python
"""
================================================================================
:mod:`RandomNumberGenerator` -- Type of random number generator
================================================================================

.. module:: RandomNumberGenerator
   :synopsis: Type of random number generator

.. inheritance-diagram:: winxrayTools.Configuration.RandomNumberGenerator

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

TYPE_RAN1 = 0
TYPE_RAN2 = 1
TYPE_RAN3 = 2
TYPE_RAN4 = 3

def getLabel(type):
    if type == TYPE_RAN1:
        return 'ran1 (Press et al. 1986)'
    elif type == TYPE_RAN2:
        return 'ran2 (Press et al. 1986)'
    elif type == TYPE_RAN3:
        return 'ran3 (Press et al. 1986)'
    elif type == TYPE_RAN4:
        return 'ran4 (Press et al. 1986)'
    else:
        raise ValueError, 'Unknown random number generator'
