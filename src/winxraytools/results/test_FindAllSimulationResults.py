#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2009 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision$"
__svnDate__ = "$Date$"
__svnId__ = "$Id$"

# Standard library modules.
import unittest
import logging
import os.path

# Third party modules.

# Local modules.
import FindAllSimulationResults
import DrixUtilities.Files as Files
from DrixUtilities.Testings import ignore

# Globals and constants variables.

class TestFindAllSimulationResults(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.folderPath = Files.getCurrentModulePath(__file__, "../testData/Results/HovingtonMM2009")

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    @ignore()
    def test_getAllPathsFromFolder(self):
        paths = FindAllSimulationResults.getAllPathsFromFolder(self.folderPath)

        self.assertEquals(9, len(paths))

        pathRef = os.path.join(self.folderPath, "1000e/Cr_05keV_001")
        pathRef = os.path.normpath(pathRef)
        self.assertTrue(pathRef in paths)

        pathRef = os.path.join(self.folderPath, "1000e/Ni_30keV_001")
        pathRef = os.path.normpath(pathRef)
        self.assertTrue(pathRef in paths)

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    @ignore()
    def test_getAllPathsFromZip(self):
        zipPath = Files.getCurrentModulePath(__file__, "../testData/Results/HovingtonMM2009.zip")
        paths = FindAllSimulationResults.getAllPathsFromZip(zipPath)

        self.assertEquals(9, len(paths))

        pathRef = os.path.join("HovingtonMM2009", "1000e/Cr_05keV_001")
        pathRef = os.path.normpath(pathRef)
        self.assertTrue(pathRef in paths)

        pathRef = os.path.join("HovingtonMM2009", "1000e/Ni_30keV_001")
        pathRef = os.path.normpath(pathRef)
        self.assertTrue(pathRef in paths)

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

if __name__ == '__main__':    #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    unittest.main()
