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
__svnId__ = "$Id: BseResults.py 2364 2011-05-30 11:15:15Z hdemers $"

# Standard library modules.
import os.path

# Third party modules.

# Local modules.

# Globals and constants variables.
FILENAME = "BSEGeneral.txt"
BSE_YIELD = "BseYield"

class BseResults(object):
    def __init__(self, path=None):
        """
        Constructor.

         path - folder where the file could be found.

        """
        self.path = path

        self.filename = FILENAME

        if self.path:
            if os.path.exists(self.path):
                self.readFile(os.path.join(self.path, self.filename))
            else:
                raise ValueError("Path does not exists: " + path)

    def readFile(self, filename):
        """
        Read all lines of the file and extract data.

        """
        lines = open(filename, 'r').readlines()

        self.extractData(lines)

    def extractData(self, lines):
        self._results = self._extractData(lines)

    def _extractData(self, lines):
        results = {}

        bseValue = float(lines[2].split(':')[1])
        bseError = float(lines[3].split(':')[1])

        results[BSE_YIELD] = (bseValue, bseError)

        return results

    def getBseYield(self):
        return self._results[BSE_YIELD][0]

    def getBseYieldError(self):
        return self._results[BSE_YIELD][1]

