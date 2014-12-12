#!/usr/bin/env python
"""
================================================================================
:mod:`Window` -- Type of detector window
================================================================================

.. module:: Window
   :synopsis: Type of detector window

.. inheritance-diagram:: winxraytools.configuration.Window

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

TYPE_BE = 1
TYPE_NONE = 2
TYPE_USER = 3

def getLabel(type):
    if type == TYPE_BE:
        return 'Be'
    elif type == TYPE_NONE:
        return 'None'
    elif type == TYPE_USER:
        return 'User'
    else:
        raise ValueError('Unknown window')
