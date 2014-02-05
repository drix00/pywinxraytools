#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2007 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision: 2663 $"
__svnDate__ = "$Date: 2012-02-08 09:59:51 -0500 (Wed, 08 Feb 2012) $"
__svnId__ = "$Id: ElectronElasticCrossSection.py 2663 2012-02-08 14:59:51Z ppinard $"

# Standard library modules.

# Third party modules.

# Local modules.

# Globals and constants variables.

TYPE_MOTTTABULATED = 0
TYPE_RUTHERFORD = 1
TYPE_MOTTTABULATEDLINEAR = 2
TYPE_MOTTTABULATEDPOWERLAW = 3
TYPE_MOTTTABULATEDCUBICSPLINE = 4
TYPE_MOTTPARAMETRIZEDHD = 5
TYPE_MOTTEQUATIONB = 6
TYPE_MOTTEQUATIONDD = 7
TYPE_RUTHERFORDRELATIVISTIC = 8

def getLabel(type):
    if type == TYPE_MOTTTABULATED:
        return "MottTabulated"
    elif type == TYPE_RUTHERFORD:
        return "Rutherford"
    elif type == TYPE_MOTTTABULATEDLINEAR:
        return "MottTabulatedLinear"
    elif type == TYPE_MOTTTABULATEDPOWERLAW:
        return "MottTabulatedPowerLaw"
    elif type == TYPE_MOTTTABULATEDCUBICSPLINE:
        return "MottTabulatedCubicSpline"
    elif type == TYPE_MOTTPARAMETRIZEDHD:
        return "MottParametrizedHD"
    elif type == TYPE_MOTTEQUATIONB:
        return "MottEquationB"
    elif type == TYPE_MOTTEQUATIONDD:
        return "MottEquationDD"
    elif type == TYPE_RUTHERFORDRELATIVISTIC:
        return "RutherfordRelativistic"
    else:
        raise ValueError, 'Unknown elastic cross section'

if __name__ == '__main__': #pragma: no cover
    import DrixUtilities.Runner as Runner
    Runner.Runner().run(runFunction=None)
