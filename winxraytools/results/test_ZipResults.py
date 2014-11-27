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
__svnId__ = "$Id: test_ZipResults.py 2364 2011-05-30 11:15:15Z hdemers $"

# Standard library modules.
import unittest
import os.path

# Third party modules.
from pkg_resources import resource_filename #@UnresolvedImport
from nose.plugins.skip import SkipTest

# Local modules.
import winxraytools.results.ZipResults as ZipResults

# Globals and constants variables.

class TestZipResults(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.zipFilename = resource_filename(__name__, "../testData/zipFileTest.zip")
        if not os.path.exists(self.zipFilename):
            raise SkipTest

        self.zipResults = ZipResults.ZipResults(self.zipFilename)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testConstructor(self):
        zipFilename = resource_filename(__name__, "../testData/zipFileTest.zip")

        zipResults = ZipResults.ZipResults(zipFilename)

        self.assertNotEquals(None, zipResults)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testExtractFolderList(self):
        folderList = self.zipResults.extractFolderList(self.zipFilename)

        self.assertEquals(4, len(folderList))

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testGetAvailableSimulations(self):
        folderListReference = ['zipFileTest/E15.0keV_Al_0.4100wf_Zn_001'
                                                     , 'zipFileTest/E05.0keV_Al_0.0000wf_Zn_001'
                                                     , 'zipFileTest/E10.0keV_Al_0.1100wf_Zn_001'
                                                     , 'zipFileTest/E20.0keV_Al_0.3100wf_Zn_001']

        folderList = self.zipResults.getAvailableSimulations()

        self.assertEquals(4, len(folderList))

        self.assertEquals(folderListReference, folderList)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testGetResults(self):
        results = self.zipResults.getResults("E15.0keV_Al_0.4100wf_Zn_001")

        self.assertNotEquals(None, results)

        meanDensity_g_cm3 = results["GeneralResults"].getMeanDensity_g_cm3()

        self.assertAlmostEquals(4.26467, meanDensity_g_cm3, 4)

        intensityFilm = results["CharacteristicIntensity"].getData(13, 'Kb1')['film']

        self.assertAlmostEquals(1.69531, intensityFilm * 1.0E5, 5)

        absorptionCorrection = results["CorrectionFactor"].getAbsorptionCorrection(13, 'Ka1')

        self.assertAlmostEquals(0.442838, absorptionCorrection, 5)

        depth = results["CharateristicPhirhoz"].data["Generated"]['Z (nm)'][0]

        self.assertAlmostEquals(-1804.09, depth, 4)

        value = results["CharateristicPhirhoz"].data["Generated"]['phirhoz'][30]['L'][-1]

        self.assertAlmostEquals(1.60278, value, 5)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

if __name__ == '__main__': #pragma: no cover
    import logging, nose
    logging.getLogger().setLevel(logging.DEBUG)
    nose.runmodule()
