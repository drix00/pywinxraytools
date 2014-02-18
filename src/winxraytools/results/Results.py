#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2007 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision: 2706 $"
__svnDate__ = "$Date: 2012-04-01 11:13:10 -0400 (Sun, 01 Apr 2012) $"
__svnId__ = "$Id: Results.py 2706 2012-04-01 15:13:10Z ppinard $"

# Standard library modules.
import os.path

# Third party modules.

# Local modules.
import GeneralResults
import BseResults
import CharacteristicIntensity
import CharateristicPhirhoz
import CorrectionFactor
import XRaySpectrumLine
import XRayIntensity
import winxraytools.configuration.OptionsFile as OptionsFile

# Globals and constants variables.

class Results(dict):
    def __init__(self, resultsPath):
        dict.__init__(self)

        self.resultsPath = resultsPath

        self.extractResults()

    def extractResults(self):
        optionFilepath = os.path.join(self.resultsPath, "Option.wxc")

        self["Options"] = OptionsFile.OptionsFile(optionFilepath)

        self["GeneralResults"] = GeneralResults.GeneralResults(self.resultsPath)

        self["BseResults"] = BseResults.BseResults(self.resultsPath)

        self["CharacteristicIntensity"] = CharacteristicIntensity.CharacteristicIntensity(self.resultsPath)

        self["XRaySpectrumLine"] = XRaySpectrumLine.XRaySpectrumLine(self.resultsPath)

        self["XRayIntensity"] = XRayIntensity.XRayIntensity(self.resultsPath)

        self["CharateristicPhirhoz"] = CharateristicPhirhoz.CharateristicPhirhoz(self.resultsPath)

        self["CorrectionFactor"] = CorrectionFactor.CorrectionFactor(self.resultsPath)

    def getResultsTypeList(self):
        typeList = self.keys()

        typeList.sort()

        return typeList
