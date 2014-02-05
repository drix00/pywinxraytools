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
__svnId__ = "$Id: test_CharacteristicIntensity.py 2364 2011-05-30 11:15:15Z hdemers $"

# Standard library modules.
import unittest
import logging

# Third party modules.

# Local modules.
import CharacteristicIntensity
import DrixUtilities.Files as Files
from DrixUtilities.Testings import ignore

# Globals and constants variables.

class TestCharacteristicIntensity(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    @ignore()
    def testReadFile(self):
        path = Files.getCurrentModulePath(__file__, "../testData/ana 644_001")

        ci = CharacteristicIntensity.CharacteristicIntensity(path)

        self.assertEquals(2, len(ci.intensities))

        self.assertEquals(2, len(ci.intensities[29]))

        self.assertEquals(930, ci.intensities[29]['La']['energy'])

        self.assertEquals((6627.84, 21.6808), ci.intensities[28]['La']['generated'])

        self.assertEquals((1174.89, 3.58807), ci.intensities[29]['Lb1']['emitted'])

        self.assertEquals((5611.92, 0), ci.intensities[28]['Lb1']['detected'])

        self.assertEquals(3.71136e-06, ci.intensities[28]['Lb1']['film'])

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

if __name__ == '__main__': #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    unittest.main()
