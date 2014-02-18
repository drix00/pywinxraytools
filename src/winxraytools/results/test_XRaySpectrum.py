#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Philippe T. Pinard"
__email__ = "philippe.pinard@gmail.com"
__version__ = "0.1"
__copyright__ = "Copyright (c) 2012 Philippe T. Pinard"
__license__ = "GPL v3"

# Standard library modules.
import unittest
import os

# Third party modules.
from pkg_resources import resource_filename #@UnresolvedImport
from nose.plugins.attrib import attr

# Local modules.
from winxraytools.results.XRaySpectrum import XRaySpectrum

# Globals and constants variables.

@attr('ignore')
class TestXRaySpectrum(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        relativePath = os.path.join('..', 'testData', 'prz Cu 5_001')
        path = resource_filename(__name__, relativePath)

        self.r = XRaySpectrum(path)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testskeleton(self):
        self.assertTrue(True)

    def testGetTotal(self):
        energies, intensities = self.r.getTotal()
        self.assertEqual(500, len(energies))
        self.assertEqual(500, len(intensities))

        self.assertAlmostEqual(5, energies[0], 4)
        self.assertAlmostEqual(0.074746, intensities[0], 4)

        self.assertAlmostEqual(855, energies[85], 4)
        self.assertAlmostEqual(363.618, intensities[85], 4)

        self.assertAlmostEqual(4995, energies[-1], 4)
        self.assertAlmostEqual(0.683547, intensities[-1], 4)

    def testGetBackground(self):
        energies, intensities = self.r.getBackground()
        self.assertEqual(500, len(energies))
        self.assertEqual(500, len(intensities))

        self.assertAlmostEqual(5, energies[0], 4)
        self.assertAlmostEqual(0.074746, intensities[0], 4)

        self.assertAlmostEqual(855, energies[85], 4)
        self.assertAlmostEqual(277.606, intensities[85], 4)

        self.assertAlmostEqual(4995, energies[-1], 4)
        self.assertAlmostEqual(0.683547, intensities[-1], 4)

    def testGetCharacteristic(self):
        energies, intensities = self.r.getCharacteristic()
        self.assertEqual(500, len(energies))
        self.assertEqual(500, len(intensities))

        self.assertAlmostEqual(5, energies[0], 4)
        self.assertAlmostEqual(0.0, intensities[0], 4)

        self.assertAlmostEqual(855, energies[85], 4)
        self.assertAlmostEqual(86.0113, intensities[85], 4)

        self.assertAlmostEqual(4995, energies[-1], 4)
        self.assertAlmostEqual(0.0, intensities[-1], 4)

if __name__ == '__main__': #pragma: no cover
    import logging, nose
    logging.getLogger().setLevel(logging.DEBUG)
    nose.runmodule()
