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
__svnId__ = "$Id: test_CharateristicPhirhoz.py 2364 2011-05-30 11:15:15Z hdemers $"

# Standard library modules.
import unittest
import logging
import os

# Third party modules.

# Local modules.
import CharateristicPhirhoz
import DrixUtilities.Files as Files
from DrixUtilities.Testings import ignore

# Globals and constants variables.

@ignore()
class TestCharateristicPhirhoz(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        filename = Files.getCurrentModulePath(__file__, "../testData/prz Cu 5_001/XCharPRZEm_Reg1.txt")

        self.type = "Emitted"

        self.lines = open(filename, 'r').readlines()

        self.headersReference = ['Z (nm)', 'La29PRZ', 'La29Error PRZ', 'Lb129PRZ', 'Lb129Error PRZ']

        self.phirhozFile = CharateristicPhirhoz.CharateristicPhirhoz()

        self.infoReference = {'La29PRZ': ('La', 29, 'value')
                                                    , 'La29Error PRZ': ('La', 29, 'error')
                                                    , 'Lb129PRZ':    ('Lb1', 29, 'value')
                                                    , 'Lb129Error PRZ':('Lb1', 29, 'error')
                                                    , 'L29PRZ': ('L', 29, 'value')
                                                    , 'L29Error PRZ': ('L', 29, 'error')
                                                    , 'K5PRZ': ('K', 5, 'value')
                                                    , 'K5PRZ': ('K', 5, 'value')
                                                    , 'K5Error PRZ': ('K', 5, 'error')
                                                    , 'Ka15PRZ': ('Ka1', 5, 'value')
                                                    , 'Ka15Error PRZ':    ('Ka1', 5, 'error')
                                                    }

        self.phirhozFile.extractData(self.lines, self.type)

        self.maximumDepthsReference = {}
        self.maximumDepthsReference[29] = {'La': -92.1666, 'Lb1': -89.2637}

        self.integralsReference = {}
        self.integralsReference[29] = {'La': 93.2397, 'Lb1': 76.5829}

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testExtractHeader(self):
        headers = self.phirhozFile.extractHeader(self.lines[0])

        self.assertEquals(len(self.headersReference), len(headers))

        self.assertEquals(self.headersReference, headers)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testExtractData(self):
        self.phirhozFile.extractData(self.lines, self.type)

        data = self.phirhozFile.data[self.type]

        self.assertAlmostEquals(-142.967, data['Z (nm)'][0], 2)

        self.assertAlmostEquals(-0.725721, data['Z (nm)'][-1], 2)

        self.assertAlmostEquals(0.0, data['phirhoz error'][29]['Lb1'][0], 2)

        self.assertAlmostEquals(0.00406639, data['phirhoz error'][29]['Lb1'][0], 2)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testExtractInfo(self):
        for key in self.infoReference:
            self.assertEquals(self.infoReference[key], self.phirhozFile.extractInfo(key))

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testComputeMaximumDepth(self):
        self.phirhozFile.computeMaximumDepth(self.phirhozFile.data[self.type])

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testGetMaximumDepth(self):
        maximumDepths = self.phirhozFile.getMaximumDepth(self.type)

        for atomicNumber in self.maximumDepthsReference:
            for xrayLine in self.maximumDepthsReference[atomicNumber]:
                self.assertAlmostEquals(self.maximumDepthsReference[atomicNumber][xrayLine], maximumDepths[atomicNumber][xrayLine], 3)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testGetIntegral(self):
        integrals = self.phirhozFile.getIntegral(self.type)

        for atomicNumber in self.integralsReference:
            for xrayLine in self.integralsReference[atomicNumber]:
                #print atomicNumber, xrayLine, integrals[atomicNumber][xrayLine]
                self.assertAlmostEquals(self.integralsReference[atomicNumber][xrayLine], integrals[atomicNumber][xrayLine], 3)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

if __name__ == '__main__': #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    os.chdir("../")
    unittest.main()
