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
__svnId__ = "$Id: test_CorrectionFactor.py 2364 2011-05-30 11:15:15Z hdemers $"

# Standard library modules.
import unittest
import logging

# Third party modules.

# Local modules.
import CorrectionFactor
import DrixUtilities.Files as Files
from DrixUtilities.Testings import ignore

# Globals and constants variables.

@ignore()
class TestCorrectionFactor(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        resultsFolder = Files.getCurrentModulePath(__file__, "../testData/Fe75Ni25_TOA40_25keV_001")
        self.correctionFactors = CorrectionFactor.CorrectionFactor(resultsFolder)

        resultsFolder = Files.getCurrentModulePath(__file__, "../testData/Fe_TOA40_25keV_001")
        self.correctionFactorsFeStd = CorrectionFactor.CorrectionFactor(resultsFolder)

        resultsFolder = Files.getCurrentModulePath(__file__, "../testData/Ni_TOA40_25keV_001")
        self.correctionFactorsNiStd = CorrectionFactor.CorrectionFactor(resultsFolder)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testConstructor(self):
        resultsFolder = Files.getCurrentModulePath(__file__, "../testData/prz Cu 5_001")

        CorrectionFactor.CorrectionFactor(resultsFolder)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testGetAbsorptionCorrection(self):
        Fa = self.correctionFactors.getAbsorptionCorrection(26, 'Ka1')
        FaStd = self.correctionFactorsFeStd.getAbsorptionCorrection(26, 'Ka1')

        print "A"
        #print 1.0/FaStd, 1.0/Fa, FaStd/Fa
        print "%s %0.4f" % ("Fe", FaStd/Fa)

        Fa = self.correctionFactors.getAbsorptionCorrection(28, 'Ka1')
        FaStd = self.correctionFactorsNiStd.getAbsorptionCorrection(28, 'Ka1')

        #print 1.0/FaStd, 1.0/Fa, FaStd/Fa
        print "%s %0.4f" % ("Ni", FaStd/Fa)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testGetAtomicNumberCorrection(self):
        Fa = self.correctionFactors.getAtomicNumberCorrection(26, 'Ka1')
        FaStd = self.correctionFactorsFeStd.getAtomicNumberCorrection(26, 'Ka1')

        print "Z"
        #print FaStd, Fa, FaStd/Fa
        print "%s %0.4f" % ("Fe", FaStd/Fa)

        Fa = self.correctionFactors.getAtomicNumberCorrection(28, 'Ka1')
        FaStd = self.correctionFactorsNiStd.getAtomicNumberCorrection(28, 'Ka1')

        #print FaStd, Fa, FaStd/Fa
        print "%s %0.4f" % ("Ni", FaStd/Fa)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

if __name__ == '__main__': #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    unittest.main()
