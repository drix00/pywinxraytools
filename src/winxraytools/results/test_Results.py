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
__svnId__ = "$Id: test_Results.py 2706 2012-04-01 15:13:10Z ppinard $"

# Standard library modules.
import unittest

# Third party modules.
from pkg_resources import resource_filename #@UnresolvedImport
from nose.plugins.attrib import attr

# Local modules.
import winxraytools.results.Results as Results

# Globals and constants variables.

@attr('ignore')
class TestResults(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.resultsFolder = resource_filename(__name__, "../testData/ana 644_001")

        self.results = Results.Results(self.resultsFolder)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testConstructor(self):
        results = Results.Results(self.resultsFolder)

        self.assertNotEquals(None, results)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testGetResultsTypeList(self):
        typeListReference = ["BseResults",
                             "CharacteristicIntensity",
                             "CharateristicPhirhoz",
                             "CorrectionFactor",
                             "GeneralResults",
                             "Options",
                             'XRayIntensity',
                             'XRaySpectrumLine']

        typeListReference.sort()

        typeList = self.results.getResultsTypeList()

        self.assertEquals(typeListReference, typeList)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testExtractResults(self):
        meanDensity_g_cm3 = self.results["GeneralResults"].getMeanDensity_g_cm3()

        self.assertAlmostEquals(8.9338, meanDensity_g_cm3, 4)

        intensityFilm = self.results["CharacteristicIntensity"].getData(29, 'La')['film']

        self.assertAlmostEquals(3.07652, intensityFilm * 1.0E6, 5)

        absorptionCorrection = self.results["CorrectionFactor"].getAbsorptionCorrection(29, 'La')

        self.assertAlmostEquals(0.8894, absorptionCorrection, 5)

        depth = self.results["CharateristicPhirhoz"].data["Generated"]['Z (nm)'][0]

        self.assertAlmostEquals(-44.1548, depth, 4)

        value = self.results["CharateristicPhirhoz"].data["Generated"]['phirhoz'][29]['L'][-1]

        self.assertAlmostEquals(1.23292, value, 5)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

if __name__ == '__main__': #pragma: no cover
    import logging, nose
    logging.getLogger().setLevel(logging.DEBUG)
    nose.runmodule()
