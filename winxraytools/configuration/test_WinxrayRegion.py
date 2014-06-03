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
__svnId__ = "$Id: test_WinxrayRegion.py 2364 2011-05-30 11:15:15Z hdemers $"

# Standard library modules.
import unittest

# Third party modules.

# Local modules.
import winxraytools.configuration.WinxrayRegion as WinxrayRegion

# Globals and constants variables.

class TestWinxrayRegion(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.regionAl = WinxrayRegion.WinxrayRegion([13], [1.0], None, None)

        self.regionMgAl = WinxrayRegion.WinxrayRegion([12, 13], [0.25, 0.75], None, None)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testCreateLabel(self):
        self.assertEqual('Al', self.regionAl.createLabel())

        self.assertEqual('MgAl', self.regionMgAl.createLabel())

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testComputeTotalWeightFraction(self):
        self.assertEqual(1.0, self.regionAl.computeTotalWeightFraction())

        self.assertEqual(1.0, self.regionMgAl.computeTotalWeightFraction())

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testComputeTotalAtomicFraction(self):
        self.assertEqual(1.0, self.regionAl.computeTotalAtomicFraction())

        self.assertEqual(1.0, self.regionMgAl.computeTotalAtomicFraction())

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testComputeMeanDensity(self):
        self.assertAlmostEqual(2.7, self.regionAl.computeMeanDensity(), 4)

        self.assertAlmostEqual(2.3727, self.regionMgAl.computeMeanDensity(), 4)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testComputeMeanZ(self):
        self.assertEqual(13, self.regionAl.computeMeanZ())

        self.assertEqual(12.75, self.regionMgAl.computeMeanZ())

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testComputeMeanAtomicMass(self):
        self.assertAlmostEqual(26.9815, self.regionAl.computeMeanAtomicMass(), 4)

        self.assertAlmostEqual(26.3124, self.regionMgAl.computeMeanAtomicMass(), 4)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def test_computeAtomicFractions(self):
        # Test with AlTiV
        regionAlTiV = WinxrayRegion.WinxrayRegion([13, 22, 23], [0.2, 0.5, 0.3], None, None)

        atomicFractionsRef = [0.31224, 0.4397, 0.24807]

        atomicFractions = regionAlTiV.computeAtomicFractions()

        self.assertEquals(len(atomicFractionsRef), len(atomicFractions))

        for afRef, af in zip(atomicFractionsRef, atomicFractions):
            self.assertAlmostEquals(afRef, af, 5)

        # Test with Al
        atomicFractionsRef = [1.0]

        atomicFractions = self.regionAl.computeAtomicFractions()

        self.assertEquals(len(atomicFractionsRef), len(atomicFractions))

        for afRef, af in zip(atomicFractionsRef, atomicFractions):
            self.assertAlmostEquals(afRef, af)

        # Test with MgAl
        atomicFractionsRef = [0.27011, 0.72996]

        atomicFractions = self.regionMgAl.computeAtomicFractions()

        self.assertEquals(len(atomicFractionsRef), len(atomicFractions))

        for afRef, af in zip(atomicFractionsRef, atomicFractions):
            self.assertAlmostEquals(afRef, af, 3)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def test_computeWeightFractions(self):
        # Test with AlTiV
        regionAlTiV = WinxrayRegion.WinxrayRegion([13, 22, 23], None, [0.2, 0.5, 0.3], None)

        weightFractionsRef = [0.12092, 0.53665, 0.34244]

        weightFractions = regionAlTiV.computeWeightFractions()

        self.assertEquals(len(weightFractionsRef), len(weightFractions))

        for wfRef, wf in zip(weightFractionsRef, weightFractions):
            self.assertAlmostEquals(wfRef, wf, 5)

        # Test with Al
        weightFractionsRef = [1.0]

        weightFractions = self.regionAl.computeWeightFractions()

        self.assertEquals(len(weightFractionsRef), len(weightFractions))

        for wfRef, wf in zip(weightFractionsRef, weightFractions):
            self.assertAlmostEquals(wfRef, wf)

        # Test with MgAl
        weightFractionsRef = [0.25, 0.75]

        weightFractions = self.regionMgAl.computeWeightFractions()

        self.assertEquals(len(weightFractionsRef), len(weightFractions))

        for wfRef, wf in zip(weightFractionsRef, weightFractions):
            self.assertAlmostEquals(wfRef, wf)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

if __name__ == '__main__': #pragma: no cover
    import logging, nose
    logging.getLogger().setLevel(logging.DEBUG)
    nose.runmodule()
