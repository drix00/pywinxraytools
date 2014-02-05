#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2007 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision: 2364 $"
__svnDate__ = "$Date: 2011-05-30 07:15:15 -0400 (Mon, 30 May 2011) $"
__svnId__ = "$Id: XRayIntensity.py 2364 2011-05-30 11:15:15Z hdemers $"

# Standard library modules.
import os.path

# Third party modules.

# Local modules.

# Globals and constants variables.

class XRayIntensity(object):
    """
    Read the results file "XSIntensity.txt" generated by winxray program.

    """
    def __init__(self, path=None):
        """
        Constructor.

         path - folder where the file could be found.

        """
        self.path = path
        self.filename = "XSIntensity.txt"

        if self.path:
            if os.path.exists(self.path):
                self.readFile(os.path.join(self.path, self.filename))
            else:
                print "Path does not exists:", path

    def extractData(self, lines):
        self.data = {}

        self.data.setdefault("Intensity", {})
        self.data.setdefault("IntensityNormalized", {})

        # Skip 1 header line.
        for line in lines[1:]:
            values = line.split("\t")

            try:
                if values[0] == "Emi Spectrum":
                    key = "Intensity"
                if values[0] == "Emi Spectrum_N":
                    key = "IntensityNormalized"

                intensityTotal = float(values[1])
                intensityBremsstrahlung = float(values[2])
                intensityCharacteristic = float(values[3])

                self.data[key]["intensityTotal"] = intensityTotal
                self.data[key]["intensityBremsstrahlung"] = intensityBremsstrahlung
                self.data[key]["intensityCharacteristic"] = intensityCharacteristic

            except ValueError:
                pass

    def readFile(self, filename):
        """
        Read all lines of the file and extract data.

        """
        lines = open(filename, 'r').readlines()

        self.extractData(lines)

if __name__ == '__main__': #pragma: no cover
    import DrixUtilities.Runner as Runner
    Runner.Runner().run(runFunction=None)
