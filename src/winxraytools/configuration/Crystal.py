#!/usr/bin/env python
"""
================================================================================
:mod:`Crystal` -- Type of detector crystal
================================================================================

.. module:: Crystal
   :synopsis: Type of detector crystal

.. inheritance-diagram:: winxrayTools.Configuration.Crystal

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

TYPE_GE = 1
TYPE_SI = 2

def getLabel(type):
    if type == TYPE_GE:
        return 'Ge'
    elif type == TYPE_SI:
        return 'Si'
    else:
        raise ValueError, 'Unknown crystal'
