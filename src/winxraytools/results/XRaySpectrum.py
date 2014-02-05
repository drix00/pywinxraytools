#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Philippe Pinard (philippe.pinard@gmail.com)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2007 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = ""
__svnDate__ = ""
__svnId__ = ""

# Standard library modules.
import os.path

# Third party modules.

# Local modules.

# Globals and constants variables.
ENERGY = 'energy'
TOTAL = 'total'
BACKGROUND = 'background'
CHARACTERISTIC = 'characteristic'

class XRaySpectrum(object):
    """
    Read the results file "XSEmi_Spectrum.txt" generated by winxray program.

    """
    def __init__(self, path=None):
        """
        Constructor.

        :arg path: folder where the file could be found (optional).
        """
        self.path = path
        self.filename = "XSEmi_Spectrum.txt"

        if self.path:
            if os.path.exists(self.path):
                self.readFile(os.path.join(self.path, self.filename))
            else:
                raise IOError, "Path does not exists: %s" % path

    def readFile(self, filename):
        """
        Read all lines of the file and extract data.
        """
        self.data = {}

        with open(filename, 'r') as fp:
            for line in fp:
                line = line.strip()
                if line.startswith('#') or not line:
                    continue

                values = line.split("\t")

                energy_eV = float(values[0])
                self.data.setdefault(ENERGY, []).append(energy_eV)

                total = float(values[1])
                self.data.setdefault(TOTAL, []).append(total)

                background = float(values[2])
                self.data.setdefault(BACKGROUND, []).append(background)

                characteristic = float(values[3])
                self.data.setdefault(CHARACTERISTIC, []).append(characteristic)

    def getTotal(self):
        """
        Returns the energy (in eV) and intensities (in counts) of the total
        spectrum. 
        """
        return self.data[ENERGY], self.data[TOTAL]

    def getBackground(self):
        """
        Returns the energy (in eV) and intensities (in counts) of only 
        background of the spectrum.
        """
        return self.data[ENERGY], self.data[BACKGROUND]

    def getCharacteristic(self):
        """
        Returns the energy (in eV) and intensities (in counts) of only the
        characteristic line of the spectrum
        """
        return self.data[ENERGY], self.data[CHARACTERISTIC]

