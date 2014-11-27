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
__svnId__ = "$Id: test_GeneralResults.py 2364 2011-05-30 11:15:15Z hdemers $"

# Standard library modules.
import unittest
import os.path

# Third party modules.
from pkg_resources import resource_filename #@UnresolvedImport
from nose.plugins.skip import SkipTest

# Local modules.
import winxraytools.results.GeneralResults as GeneralResults

# Globals and constants variables.

class TestGeneralResults(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        path = resource_filename(__name__, "../testData/ana 644_001")
        if not os.path.exists(path):
            raise SkipTest

        self.generalResult = GeneralResults.GeneralResults(path)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testReadFile(self):
        path = resource_filename(__name__, "../testData/ana 644_001")
        if not os.path.exists(path):
            raise SkipTest

        generalResult = GeneralResults.GeneralResults(path)

        self.assertEquals("1.3.0.11", generalResult.versionStr)

        self.assertEquals((1, 3, 0, 11), generalResult.version)

        self.assertEquals(132.719, generalResult.time_s)

        #self.assertEquals(360.066, generalResult.efficiency)

        self.assertEquals(10000, generalResult.numberElectron)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testGetMeanDensity_g_cm3(self):
        meanDensity_g_cm3 = self.generalResult.getMeanDensity_g_cm3()

        self.assertAlmostEquals(8.9338, meanDensity_g_cm3)
        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

if __name__ == '__main__': #pragma: no cover
    import logging, nose
    logging.getLogger().setLevel(logging.DEBUG)
    nose.runmodule()
