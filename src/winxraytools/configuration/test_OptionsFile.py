#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2007 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision: 2704 $"
__svnDate__ = "$Date: 2012-04-01 09:26:17 -0400 (Sun, 01 Apr 2012) $"
__svnId__ = "$Id: test_OptionsFile.py 2704 2012-04-01 13:26:17Z ppinard $"

# Standard library modules.
import unittest
import logging
import os
import tempfile

# Third party modules.

# Local modules.
import OptionsFile
import winxrayTools.Configuration.ElectronElasticCrossSection as eecs
import DrixUtilities.Files as Files
from DrixUtilities.Testings import ignore

# Globals and constants variables.

@ignore()
class TestOptionsFile(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.pathname = Files.getCurrentModulePath(__file__, "../testData/configurations/default.wxc")

        self.optionsFile = OptionsFile.OptionsFile(self.pathname)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testInitNoFilename(self):
        ops = OptionsFile.OptionsFile()
        self.assertEqual(None, ops.filename)

    def testIncidentenergy(self):
        incidentEnergy = self.optionsFile.getIncidentEnergy_keV()

        self.assertEquals(10.0, incidentEnergy)

        self.optionsFile.setIncidentEnergy_keV(20.0)

        incidentEnergy = self.optionsFile.getIncidentEnergy_keV()

        self.assertEquals(20.0, incidentEnergy)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testWrite(self):
        incidentEnergy = self.optionsFile.getIncidentEnergy_keV()

        self.assertEquals(10.0, incidentEnergy)

        self.optionsFile.setIncidentEnergy_keV(20.0)

        fd, filename = tempfile.mkstemp(".wxc")

        self.optionsFile.write(filename)

        optionsFile = OptionsFile.OptionsFile(filename)

        incidentEnergy = optionsFile.getIncidentEnergy_keV()

        self.assertEquals(20.0, incidentEnergy)

        os.close(fd)
        os.remove(filename)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testGetElements(self):
        atomicNumbers, fractions = self.optionsFile.getElements()

        self.assertEquals(1, len(atomicNumbers))
        self.assertEquals(1, len(fractions))

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testSetElements(self):
        atomicNumbers = [12, 13]
        weightFractions = [0.25, 0.75]

        self.optionsFile.setElements(atomicNumbers, weightFractions)

        fd, filename = tempfile.mkstemp(".wxc")

        self.optionsFile.write(filename)

        os.close(fd)
        os.remove(filename)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testPhysicsModel(self):
        #self.optionsFile.printPhysicsModel()

        self.optionsFile.setTypeTotalCrossSection(eecs.TYPE_RUTHERFORD)

        self.optionsFile.setTypePartialCrossSection(eecs.TYPE_RUTHERFORD)

        totalEECS = self.optionsFile.getTypeTotalCrossSection()

        partialEECS = self.optionsFile.getTypePartialCrossSection()

        self.assertEquals(eecs.TYPE_RUTHERFORD, totalEECS)

        self.assertEquals(eecs.TYPE_RUTHERFORD, partialEECS)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testXRayDetector(self):
        #self.optionsFile.printXRayDetector()

        NbChannelReference = 1000
        TypeeVChannelReference = 2
        TypeWindowReference = 3 # User
        TypeCrystalReference = 2
        DistanceDetectorReference = 5.7
        TimeReference = 100.0
        WindowThicknessReference = 8.0
        CrystalThicknessReference = 3.5
        CrystalRadiusReference = 1.784
        CarbonThicknessReference = 0.0
        DeadLayerThicknessReference = 85.0
        GoldThicknessReference = 8.0
        UserDefineSolidAngleReference = 0
        SolidAngleReference = 0.00308

        value = self.optionsFile.getCarbonThickness_um()
        self.assertAlmostEquals(CarbonThicknessReference, value, 1)

        value = self.optionsFile.getCrystalRadius_mm()
        self.assertAlmostEquals(CrystalRadiusReference, value, 1)

        value = self.optionsFile.getCrystalThickness_mm()
        self.assertAlmostEquals(CrystalThicknessReference, value, 1)

        value = self.optionsFile.getDeadLayerThickness_nm()
        self.assertAlmostEquals(DeadLayerThicknessReference, value, 1)

        value = self.optionsFile.getDistanceDetector_cm()
        self.assertAlmostEquals(DistanceDetectorReference, value, 1)

        value = self.optionsFile.getGoldThickness_nm()
        self.assertAlmostEquals(GoldThicknessReference, value, 1)

        value = self.optionsFile.getNumberChannel()
        self.assertAlmostEquals(NbChannelReference, value, 1)

        value = self.optionsFile.getSolidAngle_sr()
        self.assertAlmostEquals(SolidAngleReference, value, 1)

        value = self.optionsFile.getTime_s()
        self.assertAlmostEquals(TimeReference, value, 1)

        value = self.optionsFile.getTypeCrystal()
        self.assertEquals(TypeCrystalReference, value)

        value = self.optionsFile.getTypeEVChannel()
        self.assertEquals(TypeeVChannelReference, value)

        value = self.optionsFile.getTypeWindow()
        self.assertEquals(TypeWindowReference, value)

        value = self.optionsFile.isUserDefineSolidAngle()
        self.assertEquals(bool(UserDefineSolidAngleReference), value)

        value = self.optionsFile.getWindowThickness_um()
        self.assertAlmostEquals(WindowThicknessReference, value, 1)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testOptionAdvanced(self):
        #self.optionsFile.printOptionAdvanced()

        ThrowWarningReference = 1
        NbFilmReference = 100
        NbWindowReference = 100
#        FactorBReference = 0.55
#        FactorKReference = 0.75
#        FactorLReference = 1.2
#        FactorMReference = 14
        FactorBReference = 1.0
        FactorKReference = 1.0
        FactorLReference = 1.0
        FactorMReference = 1.0

        value = self.optionsFile.getFactorB()
        self.assertAlmostEquals(FactorBReference, value, 1)

        value = self.optionsFile.getFactorK()
        self.assertAlmostEquals(FactorKReference, value, 1)

        value = self.optionsFile.getFactorL()
        self.assertAlmostEquals(FactorLReference, value, 1)

        value = self.optionsFile.getFactorM()
        self.assertAlmostEquals(FactorMReference, value, 1)

        value = self.optionsFile.getNumberFilm()
        self.assertEquals(NbFilmReference, value)

        value = self.optionsFile.getNumberWindow()
        self.assertEquals(NbWindowReference, value)

        value = self.optionsFile.isThrowWarning()
        self.assertEquals(ThrowWarningReference, value)

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    def testPath(self):
        self.optionsFile.setResultsPath("/path/to/results")
        self.assertEqual('/path/to/results', self.optionsFile.getResultsPath())

if __name__ == '__main__': #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    os.chdir("../")
    unittest.main()
