#!/usr/bin/env python
"""
================================================================================
:mod:`DirectionCosine` -- Type of direction cosines
================================================================================

.. module:: DirectionCosine
   :synopsis: Type of direction cosines

.. inheritance-diagram:: DirectionCosine

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

TYPE_DEMERS = 0

def getLabel(type):
    if type == TYPE_DEMERS:
        return 'Matrices rotation (Demers, 2000)'
    else:
        raise ValueError, 'Unknown direction cosines'
