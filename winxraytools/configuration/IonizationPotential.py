#!/usr/bin/env python
"""
================================================================================
:mod:`IonizationPotential` -- Type of ionization potentials
================================================================================

.. module:: IonizationPotential
   :synopsis: Type of ionization potentials

.. inheritance-diagram:: IonizationPotential

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

TYPE_JOY_LUO = 0

def getLabel(type):
    if type == TYPE_JOY_LUO:
        return 'Joy and Luo (1989)'
    else:
        raise ValueError('Unknown ionization potential')
