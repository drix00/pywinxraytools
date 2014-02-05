#!/usr/bin/env python
"""
================================================================================
:mod:`IonizationCrossSection` -- Type of ionization cross section
================================================================================

.. module:: IonizationCrossSection
   :synopsis: Type of ionization cross section

.. inheritance-diagram:: winxrayTools.Configuration.IonizationCrossSection

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

TYPE_CASNATI = 1

def getLabel(type):
    if type == TYPE_CASNATI:
        return 'Casnati (1982)'
    else:
        raise ValueError, 'Unknown ionization cross section'
