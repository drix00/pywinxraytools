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
import os.path

# Third party modules.
from pkg_resources import resource_filename #@UnresolvedImport
import pytest

# Local modules.
import winxraytools.results.CorrectionFactor as CorrectionFactor

# Globals and constants variables.

class TestCorrectionFactor(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        resultsFolder = resource_filename(__name__, "../testData/Fe75Ni25_TOA40_25keV_001")
        if not os.path.exists(resultsFolder):
            pytest.skip("Test data file not found")
        self.correctionFactors = CorrectionFactor.CorrectionFactor(resultsFolder)

        resultsFolder = resource_filename(__name__, "../testData/Fe_TOA40_25keV_001")
        if not os.path.exists(resultsFolder):
            pytest.skip("Test data file not found")
        self.correctionFactorsFeStd = CorrectionFactor.CorrectionFactor(resultsFolder)

        resultsFolder = resource_filename(__name__, "../testData/Ni_TOA40_25keV_001")
        if not os.path.exists(resultsFolder):
            pytest.skip("Test data file not found")
        self.correctionFactorsNiStd = CorrectionFactor.CorrectionFactor(resultsFolder)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testConstructor(self):
        resultsFolder = resource_filename(__name__, "../testData/prz Cu 5_001")

        CorrectionFactor.CorrectionFactor(resultsFolder)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testGetAbsorptionCorrection(self):
        Fa = self.correctionFactors.getAbsorptionCorrection(26, 'Ka1')
        FaStd = self.correctionFactorsFeStd.getAbsorptionCorrection(26, 'Ka1')

        self.assertAlmostEqual(1.0030, FaStd / Fa, 4)

        Fa = self.correctionFactors.getAbsorptionCorrection(28, 'Ka1')
        FaStd = self.correctionFactorsNiStd.getAbsorptionCorrection(28, 'Ka1')

        self.assertAlmostEqual(1.1314, FaStd / Fa, 4)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testGetAtomicNumberCorrection(self):
        Fa = self.correctionFactors.getAtomicNumberCorrection(26, 'Ka1')
        FaStd = self.correctionFactorsFeStd.getAtomicNumberCorrection(26, 'Ka1')

        self.assertAlmostEqual(1.0084, FaStd / Fa, 4)

        Fa = self.correctionFactors.getAtomicNumberCorrection(28, 'Ka1')
        FaStd = self.correctionFactorsNiStd.getAtomicNumberCorrection(28, 'Ka1')

        self.assertAlmostEqual(0.9816, FaStd / Fa, 4)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)
