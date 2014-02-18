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
import winxraytools.results.GeneralResults as GeneralResults
import winxraytools.results.BseResults as BseResults
import winxraytools.results.CharacteristicIntensity as CharacteristicIntensity
import winxraytools.results.CharateristicPhirhoz as CharateristicPhirhoz
import winxraytools.results.CorrectionFactor as CorrectionFactor
import winxraytools.results.XRaySpectrumLine as XRaySpectrumLine
import winxraytools.results.XRayIntensity as XRayIntensity
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
        typeList = list(self.keys())

        typeList.sort()

        return typeList
