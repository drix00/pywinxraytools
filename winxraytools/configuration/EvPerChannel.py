#!/usr/bin/env python
"""
================================================================================
:mod:`EvPerChannel` -- Type of eV per channel
================================================================================

.. module:: EvPerChannel
   :synopsis: Type of eV per channel

.. inheritance-diagram:: winxraytools.configuration.EvPerChannel

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

TYPE_5 = 1
TYPE_10 = 2
TYPE_20 = 3
TYPE_40 = 4

def getLabel(type):
    if type == TYPE_5:
        return '5 eV/channel'
    elif type == TYPE_10:
        return '10 eV/channel'
    elif type == TYPE_20:
        return '20 eV/channel'
    elif type == TYPE_40:
        return '40 eV/channel'
    else:
        raise ValueError('Unknown eV/channel')
