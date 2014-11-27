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
import os.path

# Third party modules.
from pkg_resources import resource_filename #@UnresolvedImport
from nose.plugins.skip import SkipTest

# Local modules.
import winxraytools.results.CharacteristicIntensity as CharacteristicIntensity

# Globals and constants variables.

class TestCharacteristicIntensity(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testReadFile(self):
        path = resource_filename(__name__, "../testData/ana 644_001")
        if not os.path.exists(path):
            raise SkipTest

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
    import logging, nose
    logging.getLogger().setLevel(logging.DEBUG)
    nose.runmodule()
