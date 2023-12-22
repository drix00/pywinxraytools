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
import os.path

# Third party modules.
from pkg_resources import resource_filename #@UnresolvedImport
import pytest

# Local modules.
import winxraytools.results.FindAllSimulationResults as FindAllSimulationResults

# Globals and constants variables.

class TestFindAllSimulationResults(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.folderPath = resource_filename(__name__, "../testData/Results/HovingtonMM2009")
        if not os.path.isdir(self.folderPath):
            pytest.skip("Test data file not found")

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_getAllPathsFromFolder(self):
        paths = FindAllSimulationResults.getAllPathsFromFolder(self.folderPath)
        paths = list(map(os.path.normpath, paths))

        self.assertEquals(9, len(paths))

        pathRef = os.path.join(self.folderPath, "1000e/Cr_05keV_001")
        pathRef = os.path.normpath(pathRef)
        self.assertTrue(pathRef in paths)

        pathRef = os.path.join(self.folderPath, "1000e/Ni_30keV_001")
        pathRef = os.path.normpath(pathRef)
        self.assertTrue(pathRef in paths)

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_getAllPathsFromZip(self):
        zipPath = resource_filename(__name__, "../testData/Results/HovingtonMM2009.zip")
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
