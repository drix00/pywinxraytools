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
__svnId__ = "$Id: CorrectionFactor.py 2364 2011-05-30 11:15:15Z hdemers $"

# Standard library modules.
import os.path

# Third party modules.

# Local modules.
import CharateristicPhirhoz
import winxraytools.configuration.OptionsFile as OptionsFile

# Globals and constants variables.

class CorrectionFactor(object):
    def __init__(self, resultsFolder=None):
        self.integralsEmitted = None

        self.integralsGenerated = None

        self.meanDensity_g_cm3 = None

        self.weightFractions = None

        if resultsFolder != None:
            self.readEmittedData(resultsFolder)

            self.readGeneratedData(resultsFolder)

            self.readSimulationOptions(resultsFolder)

    def readSimulationOptions(self, resultsFolder):
        filename = os.path.join(resultsFolder, "Option.wxc")

        self.extractSimulationOptions(filename)

    def readGeneratedData(self, resultsFolder):
        filename = os.path.join(resultsFolder, "XCharPRZGen_Reg1.txt")

        lines = open(filename, 'r').readlines()

        self.extractGeneratedData(lines)

    def readEmittedData(self, resultsFolder):
        filename = os.path.join(resultsFolder, "XCharPRZEm_Reg1.txt")

        lines = open(filename, 'r').readlines()

        self.extractEmittedData(lines)

    def extractGeneratedData(self, lines):
        phirhozFile = CharateristicPhirhoz.CharateristicPhirhoz()

        phirhozFile.extractData(lines, "Generated")

        self.integralsGenerated = phirhozFile.getIntegral("Generated")

    def extractEmittedData(self, lines):
        phirhozFile = CharateristicPhirhoz.CharateristicPhirhoz()

        phirhozFile.extractData(lines, "Emitted")

        self.integralsEmitted = phirhozFile.getIntegral("Emitted")

    def extractSimulationOptions(self, filename):
        optionsFile = OptionsFile.OptionsFile(filename)

        self.meanDensity_g_cm3 = optionsFile.getMeanDensity_g_cm3()

        atomicNumbers, weightFractions = optionsFile.getElements()

        self.weightFractions = {}

        for index in range(len(atomicNumbers)):
            self.weightFractions[atomicNumbers[index]] = weightFractions[index]

    def getAbsorptionCorrection(self, atomicNumber, xrayLine):
        subshell = xrayLine[0]

        F0 = self.integralsGenerated[atomicNumber][subshell]

        if xrayLine in self.integralsEmitted[atomicNumber]:
            FX = self.integralsEmitted[atomicNumber][xrayLine]
        else:
            for key in self.integralsEmitted[atomicNumber]:
                if xrayLine in key:
                    FX = self.integralsEmitted[atomicNumber][key]
                    break

        F0 *= self.meanDensity_g_cm3

        FX *= self.meanDensity_g_cm3

        if F0 != 0.0:
            absorptionCorrection = FX / F0

            return absorptionCorrection

    def getAtomicNumberCorrection(self, atomicNumber, xrayLine):
        subshell = xrayLine[0]

        F0 = self.integralsGenerated[atomicNumber][subshell]

        #print F0, self.weightFractions

        #atomicNumberCorrection = F0/self.weightFractions[atomicNumber]
        atomicNumberCorrection = F0 * self.meanDensity_g_cm3

        return atomicNumberCorrection
