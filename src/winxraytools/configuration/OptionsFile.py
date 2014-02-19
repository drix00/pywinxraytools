#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2007 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision: 2892 $"
__svnDate__ = "$Date: 2013-01-28 09:12:37 -0500 (Mon, 28 Jan 2013) $"
__svnId__ = "$Id: OptionsFile.py 2892 2013-01-28 14:12:37Z ppinard $"

# Standard library modules.
import zipfile
import os
try:
    from configparser import ConfigParser
except ImportError: # Python 2
    from ConfigParser import SafeConfigParser as ConfigParser
try:
    from io import StringIO
except ImportError: # Python 3
    from StringIO import StringIO

# Third party modules.
from pkg_resources import resource_string #@UnresolvedImport

# Local modules.
import winxraytools.util.ElementProperties as ElementProperties
import winxraytools.configuration.WinxrayRegion as WinxrayRegion

# Globals and constants variables.
TYPECROSSSECTION = "TypeCrossSection"
TYPEPARTIALCROSSSECTION = "TypePartialCrossSection"
TYPETOTALCROSSSECTION = "TypeTotalCrossSection"
INCIDENTENERGY_KEV = "IncidentEnergy_keV"
ATOMICNUMBER = "AtomicNumber"

def generateZipFile(configurationPath, zipName):
    """
    Generate a zip file with all the configuration file contained in the path.

    """
    configurationZip = zipfile.ZipFile(zipName, 'w', zipfile.ZIP_DEFLATED)

    for filename in os.listdir(configurationPath):
        if os.path.splitext(filename)[1] == '.wxc':
            filepath = os.path.join(configurationPath, filename)
            configurationZip.write(filepath, os.path.basename(filename))
            #print file, os.path.basename(file)

    configurationZip.close()

class OptionsFile(object):
    def __init__(self, filename=None):
        self.configParser = ConfigParser()

        self.filename = filename
        self.read(self.filename)

        self.setFactorB(1.0)
        self.setFactorK(1.0)
        self.setFactorL(1.0)
        self.setFactorM(1.0)

    def read(self, filename):
        if filename:
            self.configParser.read(filename)
        else: # read default.wxc
            data = resource_string(__name__, "default.wxc")
            data = StringIO(data.decode('ascii')) # Ensure unicode

            try:
                self.configParser.read_file(data)
            except:
                self.configParser.readfp(data)

    def write(self, filename=None):
        if not filename:
            filename = self.filename

        filename = self.checkFilename(filename)

        self.checkXray()
        self.checkIncidentEnergy()
        self.checkPosXInit()
        self.checkPosYInit()
        self.checkBSEDistribution()
        self.checkEnergyLossDistribution()
        self.checkElectronDistribution()

#        self.setTypeMac(3)

        self.configParser.write(open(filename, 'w'))

        #print len(files)
        #print files

    def checkFilename(self, filename):
        root, ext = os.path.splitext(filename)

        if ext != ".wxc":
            raise IOError('Invalid extension: %s' % ext)

        return root + ext

    def printSections(self):
        sections = self.configParser.sections()

        sections.sort()

        for section in sections:
            print(section)

    def printOptions(self, section):
        options = self.configParser.options(section)

        options.sort()

        for option in options:
            print(option)

    def printElectricField(self):
        self.printOptions('ElectricField')

    def printOptionAdvanced(self):
        self.printOptions('OptionAdvanced')

    def printOptionResultGeneral(self):
        self.printOptions('OptionResultGeneral')

    def printOptionResultTrajectory(self):
        self.printOptions('OptionResultTrajectory')

    def printOptionSimulation(self):
        self.printOptions('OptionSimulation')

    def printOptionsSpecimen(self):
        self.printOptions('OptionSpecimen')

    def printPhysicsModel(self):
        self.printOptions('PhysicsModel')

    def printRegion(self):
        self.printOptions('Region_1')

    def printResultDistribution(self):
        self.printOptions('ResultDistribution')

    def printXRayDetector(self):
        self.printOptions('XRayDetector')

    def set(self, section, option, value):
        #print section, self.configParser.has_section(section)

        self.configParser.set(section, option, str(value))

    def get(self, section, option):
        return self.configParser.get(section, option)



    def setTOA_deg(self, value):
        self.set('OptionSimulation', 'toa', value)

    def getTOA_deg(self):
        return float(self.get('OptionSimulation', 'toa'))

    def setAngleThetaDetector_deg(self, value):
        self.set('OptionSimulation', 'anglethetadetector', value)

    def getAngleThetaDetector_deg(self):
        return float(self.get('OptionSimulation', 'anglethetadetector'))

    def setAnglePhiDetector_deg(self, value):
        self.set('OptionSimulation', 'AnglePhiDetector', value)

    def getAnglePhiDetector_deg(self):
        return float(self.get('OptionSimulation', 'AnglePhiDetector'))



    def setBeamCurrent_A(self, value):
        self.set('OptionSimulation', 'beamcurrent', value)

    def getBeamCurrent_A(self):
        return float(self.get('OptionSimulation', 'beamcurrent'))

    def setBeamDiameter_nm(self, value):
        self.set('OptionSimulation', 'beamdiameter', value)

    def getBeamDiameter_nm(self):
        return float(self.get('OptionSimulation', 'beamdiameter'))

    def setBeamPhi_deg(self, value):
        self.set('OptionSimulation', 'beamphi', value)

    def getBeamPhi_deg(self):
        return float(self.get('OptionSimulation', 'beamphi'))

    def setBeamTheta_deg(self, value):
        self.set('OptionSimulation', 'beamtheta', value)

    def getBeamTheta_deg(self):
        return float(self.get('OptionSimulation', 'beamtheta'))



    def setMultiEnergy(self, value):
        self.set('OptionSimulation', 'multienergy', int(value))

    def isMultiEnergy(self):
        return bool(int(self.get('OptionSimulation', 'multienergy')))

    def setIncidentEnergy_keV(self, value):
        self.set('OptionSimulation', 'incidentenergy', value)

    def getIncidentEnergy_keV(self):
        return float(self.get('OptionSimulation', 'incidentenergy'))

    def setStartEnergy_keV(self, value):
        self.set('OptionSimulation', 'startenergy', value)

    def getStartEnergy_keV(self):
        return float(self.get('OptionSimulation', 'startenergy'))

    def setEndEnergy_keV(self, value):
        self.set('OptionSimulation', 'endenergy', value)

    def getEndEnergy_keV(self):
        return float(self.get('OptionSimulation', 'endenergy'))

    def setNbStepEnergy(self, value):
        self.set('OptionSimulation', 'nbstepenergy', value)

    def getNbStepEnergy(self):
        return int(self.get('OptionSimulation', 'nbstepenergy'))

    def setStepEnergy_keV(self, value):
        self.set('OptionSimulation', 'stepenergy', value)

    def getStepEnergy_keV(self):
        return float(self.get('OptionSimulation', 'stepenergy'))

    def checkIncidentEnergy(self):
        if not self.isMultiEnergy():
            incidentEnergy = self.getIncidentEnergy_keV()
            #print incidentEnergy
            self.setStartEnergy_keV(incidentEnergy)
            self.setEndEnergy_keV(incidentEnergy)
            self.setNbStepEnergy(1)



    def setMultiPosXInit(self, value):
        self.set('OptionSimulation', 'multiposxinit', int(value))

    def isMultiPosXInit(self):
        return bool(int(self.get('OptionSimulation', 'multiposxinit')))

    def setPosXInit_nm(self, value):
        self.set('OptionSimulation', 'posxinit', value)

    def getPosXInit_nm(self):
        return float(self.get('OptionSimulation', 'posxinit'))

    def setStartPosXInit_nm(self, value):
        self.set('OptionSimulation', 'startposxinit', value)

    def getStartPosXInit_nm(self):
        return float(self.get('OptionSimulation', 'startposxinit'))

    def setEndPosXInit_nm(self, value):
        self.set('OptionSimulation', 'endposxinit', value)

    def getEndPosXInit_nm(self):
        return float(self.get('OptionSimulation', 'endposxinit'))

    def setStepPosXInit_nm(self, value):
        self.set('OptionSimulation', 'stepposxinit', value)

    def getStepPosXInit_nm(self):
        return float(self.get('OptionSimulation', 'stepposxinit'))

    def setNbStepPosXInit(self, value):
        self.set('OptionSimulation', 'nbstepposxinit', value)

    def getNbStepPosXInit(self):
        return int(self.get('OptionSimulation', 'nbstepposxinit'))

    def checkPosXInit(self):
        if not self.isMultiPosXInit():
            posXInit = self.getPosXInit_nm()

            self.setStartPosXInit_nm(posXInit)
            self.setEndPosXInit_nm(posXInit)
            self.setNbStepPosXInit(1)



    def setMultiPosYInit(self, value):
        self.set('OptionSimulation', 'multiposyinit', value)

    def isMultiPosYInit(self):
        return bool(int(self.get('OptionSimulation', 'multiposyinit')))

    def setPosYInit_nm(self, value):
        self.set('OptionSimulation', 'posyinit', value)

    def getPosYInit_nm(self):
        return float(self.get('OptionSimulation', 'posyinit'))

    def setStartPosYInit_nm(self, value):
        self.set('OptionSimulation', 'startposyinit', value)

    def getStartPosYInit_nm(self):
        return float(self.get('OptionSimulation', 'startposyinit'))

    def setEndPosYInit_nm(self, value):
        self.set('OptionSimulation', 'endposyinit', value)

    def getEndPosYInit_nm(self):
        return float(self.get('OptionSimulation', 'endposyinit'))

    def setStepPosYInit_nm(self, value):
        self.set('OptionSimulation', 'stepposyinit', value)

    def getStepPosYInit_nm(self):
        return float(self.get('OptionSimulation', 'stepposyinit'))

    def setNbStepPosYInit(self, value):
        self.set('OptionSimulation', 'nbstepposyinit', value)

    def getNbStepPosYInit(self):
        return int(self.get('OptionSimulation', 'nbstepposyinit'))

    def checkPosYInit(self):
        if not self.isMultiPosYInit():
            posYInit = self.getPosYInit_nm()

            self.setStartPosYInit_nm(posYInit)
            self.setEndPosYInit_nm(posYInit)
            self.setNbStepPosYInit(1)



    def setNbElectron(self, value):
        self.set('OptionSimulation', 'nbelectron', value)

    def getNbElectron(self):
        return int(self.get('OptionSimulation', 'nbelectron'))



    def setXrayCompute(self, value):
        self.set('OptionSimulation', 'xraycompute', int(value))

    def isXrayCompute(self):
        return bool(int(self.get('OptionSimulation', 'xraycompute')))

    def setXrayComputeBackground(self, value):
        self.set('OptionSimulation', 'xraycomputebackground', int(value))

    def isXrayComputeBackground(self):
        return bool(int(self.get('OptionSimulation', 'xraycomputebackground')))

    def setXrayComputeCharacteristic(self, value):
        self.set('OptionSimulation', 'xraycomputecharacteristic', int(value))

    def isXrayComputeCharacteristic(self):
        return bool(int(self.get('OptionSimulation', 'xraycomputecharacteristic')))

    def checkXray(self):
        value = self.isXrayComputeBackground() or \
                self.isXrayComputeCharacteristic()
        self.setXrayCompute(value)



    def setElement(self, atomicNumber):
        raise NotImplementedError

    def setElements(self, atomicNumbers, weightFractions=None,
                    atomicFractions=None, massDensities=None):
        regionSection = 'Region_1'

        if not self.configParser.has_section(regionSection):
            self.printRegion()
            return

        if weightFractions == None and atomicFractions == None:
            weightFractions = [1.0 for index in range(len(atomicNumbers))]

        assert len(atomicNumbers) == len(weightFractions)

        region = WinxrayRegion.WinxrayRegion(atomicNumbers
                                                     , weightFractions
                                                     , atomicFractions
                                                     , massDensities
                                                     )

        atomicNumbers = region.getAtomicnumbers()
        weightFractions = region.getWeightFraction()
        atomicFractions = region.getAtomicFraction()
        massDensities = region.getMassDensities()

        label = region.createLabel()

        option = 'Label'
        self.set(regionSection, option, label)

        option = 'Indice'
        self.set(regionSection, option, 1)

        option = 'NbElement'
        self.set(regionSection, option, len(atomicNumbers))

        totalWeightFraction = region.computeTotalWeightFraction()

        option = 'TotalWeightFraction'
        self.set(regionSection, option, totalWeightFraction)

        totalAtomicFraction = region.computeTotalAtomicFraction()

        option = 'TotalAtomicFraction'
        self.set(regionSection, option, totalAtomicFraction)

        meanDensity = region.computeMeanDensity()

        option = 'TotalDensity'
        self.set(regionSection, option, meanDensity)

        option = 'MeanDensity'
        self.set(regionSection, option, meanDensity)

        meanZ = region.computeMeanZ()

        option = 'MeanZ'
        self.set(regionSection, option, meanZ)

        meanAtomicMass = region.computeMeanAtomicMass()

        option = 'MeanAtomicMass'
        self.set(regionSection, option, meanAtomicMass)

        atomicDensities_atom_cm3 = region.computeAtomicDensities_atom_cm3()

        assert len(atomicNumbers) == len(atomicDensities_atom_cm3)

        for index, atomicNumber in enumerate(atomicNumbers):
            elementID = index + 1

            option = 'Symbol_' + str(elementID)
            self.set(regionSection, option, ElementProperties.getSymbol(atomicNumber))

            option = 'Name_' + str(elementID)
            self.set(regionSection, option, ElementProperties.getName(atomicNumber))

            option = 'Z_' + str(elementID)
            self.set(regionSection, option, atomicNumber)

            option = 'WeightFraction_' + str(elementID)
            self.set(regionSection, option, weightFractions[index])

            option = 'AtomicFraction_' + str(elementID)
            self.set(regionSection, option, atomicFractions[index])

            option = 'Density_' + str(elementID)
            self.set(regionSection, option, massDensities[index])

            #atomicDensity = ElementProperties.computeAtomicDensity_atom_cm3(massDensities[index], atomicMass)

            option = 'AtomicDensity_' + str(elementID)
            self.set(regionSection, option, atomicDensities_atom_cm3[index])

            option = 'AtomicMass_' + str(elementID)
            self.set(regionSection, option, ElementProperties.getAtomicMass_g_mol(atomicNumber))

            option = 'FermiEnergy_' + str(elementID)
            self.set(regionSection, option, ElementProperties.getFermiEnergy_eV(atomicNumber))

            option = 'kFermi_' + str(elementID)
            self.set(regionSection, option, ElementProperties.getKFermi_eV(atomicNumber))

            option = 'PlasmonEenrgy_' + str(elementID)
            self.set(regionSection, option, ElementProperties.getPlasmonEnergy_eV(atomicNumber))

            option = 'J_' + str(elementID)
            self.set(regionSection, option, ElementProperties.getMeanIonizationEnergy_eV(atomicNumber))

            option = 'K_' + str(elementID)
            self.set(regionSection, option, ElementProperties.getKRatioCorrection(atomicNumber))

    def getMeanDensity_g_cm3(self):
        region = 'Region_1'

        option = "MeanDensity"

        if self.configParser.has_option(region, option):
            meanDensity_g_cm3 = float(self.get(region, option))

            return meanDensity_g_cm3

    def setMeanDensity_g_cm3(self, value):
        regionSection = 'Region_1'
        self.set(regionSection, 'TotalDensity', value)
        self.set(regionSection, 'MeanDensity', value)

    def getElements(self, fractionType='weight'):
        region = 'Region_1'

        atomicNumbers = []
        fractions = []

        elementID = 1
        while True:

            option = 'Z_' + str(elementID)
            if self.configParser.has_option(region, option):
                atomicNumber = int(self.get(region, option))

                atomicNumbers.append(atomicNumber)

            if fractionType == 'weight':
                option = 'WeightFraction_' + str(elementID)
            else:
                option = 'AtomicFraction_' + str(elementID)

            if self.configParser.has_option(region, option):
                fraction = float(self.get(region, option))

                fractions.append(fraction)

            if len(atomicNumbers) != elementID and len(fractions) != elementID:
                break

            elementID += 1

        #print atomicNumbers, fractions
        return atomicNumbers, fractions





# TODO: OptionSimulation check if complete.
# TODO: Region_1 check if complete.
# TODO: OptionSpecimen check if complete.
# TODO: OptionResultTrajectory (5).

    def getCarbonThickness_um(self):
        return float(self.get('XRayDetector', 'carbonthickness'))

    def setCarbonThickness_um(self, value):
        self.set('XRayDetector', 'carbonthickness', value)

    def getCrystalRadius_mm(self):
        return float(self.get('XRayDetector', 'crystalradius'))

    def setCrystalRadius_mm(self, value):
        self.set('XRayDetector', 'crystalradius', value)

    def getCrystalThickness_mm(self):
        return float(self.get('XRayDetector', 'crystalthickness'))

    def setCrystalThickness_mm(self, value):
        self.set('XRayDetector', 'crystalthickness', value)

    def getDeadLayerThickness_nm(self):
        return float(self.get('XRayDetector', 'deadlayerthickness'))

    def setDeadLayerThickness_nm(self, value):
        self.set('XRayDetector', 'deadlayerthickness', value)

    def getDistanceDetector_cm(self):
        return float(self.get('XRayDetector', 'distancedetector'))

    def setDistanceDetector_cm(self, value):
        self.set('XRayDetector', 'distancedetector', value)

    def getGoldThickness_nm(self):
        return float(self.get('XRayDetector', 'goldthickness'))

    def setGoldThickness_nm(self, value):
        self.set('XRayDetector', 'goldthickness', value)

    def getNumberChannel(self):
        return int(self.get('XRayDetector', 'nbchannel'))

    def setNumberChannel(self, value):
        self.set('XRayDetector', 'nbchannel', int(value))

    def setUserDefineSolidAngle(self, value):
        self.set('XRayDetector', 'userdefinesolidangle', int(value))

    def isUserDefineSolidAngle(self):
        return bool(int(self.get('XRayDetector', 'userdefinesolidangle')))

    def getSolidAngle_sr(self):
        return float(self.get('XRayDetector', 'solidangle'))

    def setSolidAngle_sr(self, value):
        self.set('XRayDetector', 'solidangle', value)

    def getTime_s(self):
        return float(self.get('XRayDetector', 'time'))

    def setTime_s(self, value):
        self.set('XRayDetector', 'time', value)

    def getTypeCrystal(self):
        return int(self.get('XRayDetector', 'typecrystal'))

    def setTypeCrystal(self, value):
        """
        Sets type of crystal.
        Use:

            * :const:`CRYSTAL_GE`
            * :const:`CRYSTAL_SI`
        """
        self.set('XRayDetector', 'typecrystal', value)

    def getTypeEVChannel(self):
        return int(self.get('XRayDetector', 'typeevchannel'))

    def setTypeEVChannel(self, value):
        """
        Sets type of eV/channel.
        Use:

            * :const:`EV_PER_CHANNEL_5`
            * :const:`EV_PER_CHANNEL_10`
            * :const:`EV_PER_CHANNEL_20`
            * :const:`EV_PER_CHANNEL_40`
        """
        self.set('XRayDetector', 'typeevchannel', value)

    def getTypeWindow(self):
        return int(self.get('XRayDetector', 'typewindow'))

    def setTypeWindow(self, value):
        """
        Sets type of detector window.
        Use:

            * :const:`WINDOW_BE`
            * :const:`WINDOW_NONE`
            * :const:`WINDOW_USER`
        """
        self.set('XRayDetector', 'typewindow', value)

    def getWindowThickness_um(self):
        return float(self.get('XRayDetector', 'windowthickness'))

    def setWindowThickness_um(self, value):
        self.set('XRayDetector', 'windowthickness', value)



    def setIdum(self, value):
        self.set('PhysicsModel', 'idum', value)

    def getIdum(self):
        return int(self.get('PhysicsModel', 'idum'))

    def setIdumFixed(self, value):
        self.set('PhysicsModel', 'idumfixed', int(value))

    def isIdumFixed(self):
        return bool(int(self.get('PhysicsModel', 'idumfixed')))

    def setMinimumElectronEnergy_eV(self, value):
        self.set('PhysicsModel', 'minimumelectronenergy', value)

    def getMinimumElectronEnergy_eV(self):
        return float(self.get('PhysicsModel', 'minimumelectronenergy'))



    def setTypeAtomicPotentialMott(self, value):
        self.set('PhysicsModel', 'typeatomicpotentialmott', value)

    def getTypeAtomicPotentialMott(self):
        return int(self.get('PhysicsModel', 'typeatomicpotentialmott'))

    def setTypeDirectionCosines(self, value):
        """
        Sets direction cosines.
        See :mod:`DirectionCosine <winxrayTools.Configuration.DirectionCosine>`
        """
        self.set('PhysicsModel', 'typedirectioncosines', value)

    def getTypeDirectionCosines(self):
        return int(self.get('PhysicsModel', 'typedirectioncosines'))

    def setTypeEnergyLoss(self, value):
        """
        Sets energy loss.
        See :mod:`EnergyLoss <winxrayTools.Configuration.EnergyLoss>`
        """
        self.set('PhysicsModel', 'typeenergyloss', value)

    def getTypeEnergyLoss(self):
        return int(self.get('PhysicsModel', 'typeenergyloss'))

    def setTypeIonisationPotential(self, value):
        """
        Sets ionization potential.
        See :mod:`IonizationPotential <winxrayTools.Configuration.IonizationPotential>`
        """
        self.set('PhysicsModel', 'typeionisationpotential', value)

    def getTypeIonisationPotential(self):
        return int(self.get('PhysicsModel', 'typeionisationpotential'))

    def setTypeMac(self, value):
        """
        Sets mass absorption coefficients.
        See :mod:`MassAbsorptionCoefficient <winxrayTools.Configuration.MassAbsorptionCoefficient>`
        """
        self.set('PhysicsModel', 'typemac', value)

    def getTypeMac(self):
        return int(self.get('PhysicsModel', 'typemac'))

    def setTypeElectronElasticCrossSection(self, type):
        """
        Sets elastic cross section.
        See :mod:`ElasticCrossSection <winxrayTools.Configuration.ElasticCrossSection>`
        """
        self.set('PhysicsModel', 'typepartialcrosssection', type)
        self.set('PhysicsModel', 'typetotalcrosssection', type)

    def setTypePartialCrossSection(self, type):
        """
        Sets partial elastic cross section.
        See :mod:`ElasticCrossSection <winxrayTools.Configuration.ElasticCrossSection>`
        """
        self.set('PhysicsModel', 'typepartialcrosssection', type)

    def setTypeTotalCrossSection(self, type):
        """
        Sets total cross section.
        See :mod:`ElasticCrossSection <winxrayTools.Configuration.ElasticCrossSection>`
        """
        self.set('PhysicsModel', 'typetotalcrosssection', type)

    def getTypePartialCrossSection(self):
        return int(self.get('PhysicsModel', 'typepartialcrosssection'))

    def getTypeTotalCrossSection(self):
        return int(self.get('PhysicsModel', 'typetotalcrosssection'))

    def setTypeRandomGenerator(self, value):
        """
        Sets random number generator.
        See :mod:`RandomNumberGenerator <winxrayTools.Configuration.RandomNumberGenerator>`
        """
        self.set('PhysicsModel', 'typerandomgenerator', value)

    def getTypeRandomGenerator(self):
        return int(self.get('PhysicsModel', 'typerandomgenerator'))

    def setTypeIonizationCrossSection(self, value):
        """
        Sets ionization cross section.
        See :mod:`IonizationCrossSection <winxrayTools.Configuration.IonizationCrossSection>`
        """
        self.set('PhysicsModel', 'typexraycrosssectionbremsstrahlung', value)
        self.set('PhysicsModel', 'typexraycrosssectioncharacteristic', value)

    def setTypeXrayCrossSectionBremsstrahlung(self, value):
        """
        Sets ionization cross section.
        See :mod:`IonizationCrossSection <winxrayTools.Configuration.IonizationCrossSection>`
        """
        self.set('PhysicsModel', 'typexraycrosssectionbremsstrahlung', value)

    def getTypeXrayCrossSectionBremsstrahlung(self):
        return int(self.get('PhysicsModel', 'typexraycrosssectionbremsstrahlung'))

    def setTypeXrayCrossSectionCharacteristic(self, value):
        """
        Sets ionization cross section.
        See :mod:`IonizationCrossSection <winxrayTools.Configuration.IonizationCrossSection>`
        """
        self.set('PhysicsModel', 'typexraycrosssectioncharacteristic', value)

    def getTypeXrayCrossSectionCharacteristic(self):
        return int(self.get('PhysicsModel', 'typexraycrosssectioncharacteristic'))




    def setComputeBSEDistribution(self, value):
        self.set('ResultDistribution', 'ComputeBSEDistribution', int(value))

    def isComputeBSEDistribution(self):
        return bool(int(self.get('ResultDistribution', 'ComputeBSEDistribution')))

    def checkBSEDistribution(self):
        value = self.isComputeBSEAngular() or \
                self.isComputeBSEDepth() or \
                self.isComputeBSEEnergy() or \
                self.isComputeBSELateral() or \
                self.isComputeBSERadial() or \
                self.isComputeBSESpatial()
        self.setComputeBSEDistribution(value)

    def setComputeBSEDepth(self, value):
        self.set('ResultDistribution', 'ComputeBSEDepth', int(value))

    def isComputeBSEDepth(self):
        return bool(int(self.get('ResultDistribution', 'ComputeBSEDepth')))

    def setNbBSEDepth(self, value):
        self.set('ResultDistribution', 'NbBSEDepth', value)

    def getNbBSEDepth(self):
        return int(self.get('ResultDistribution', 'NbBSEDepth'))

    def setComputeBSERadial(self, value):
        self.set('ResultDistribution', 'ComputeBSERadial', int(value))

    def isComputeBSERadial(self):
        return bool(int(self.get('ResultDistribution', 'ComputeBSERadial')))

    def setNbBSERadial(self, value):
        self.set('ResultDistribution', 'NbBSERadial', value)

    def getNbBSERadial(self):
        return int(self.get('ResultDistribution', 'NbBSERadial'))

    def setComputeBSESpatial(self, value):
        self.set('ResultDistribution', 'ComputeBSESpatial', int(value))

    def isComputeBSESpatial(self):
        return bool(int(self.get('ResultDistribution', 'ComputeBSESpatial')))

    def setNbBSESpatial(self, value):
        self.set('ResultDistribution', 'NbBSESpatial', value)

    def getNbBSESpatial(self):
        return int(self.get('ResultDistribution', 'NbBSESpatial'))

    def setComputeBSELateral(self, value):
        self.set('ResultDistribution', 'ComputeBSELateral', int(value))

    def isComputeBSELateral(self):
        return bool(int(self.get('ResultDistribution', 'ComputeBSELateral')))

    def setNbBSELateral(self, value):
        self.set('ResultDistribution', 'NbBSELateral', value)

    def getNbBSELateral(self):
        return int(self.get('ResultDistribution', 'NbBSELateral'))

    def setComputeBSEEnergy(self, value):
        self.set('ResultDistribution', 'ComputeBSEEnergy', int(value))

    def isComputeBSEEnergy(self):
        return bool(int(self.get('ResultDistribution', 'ComputeBSEEnergy')))

    def setNbBSEEnergy(self, value):
        self.set('ResultDistribution', 'NbBSEEnergy', value)

    def getNbBSEEnergy(self):
        return int(self.get('ResultDistribution', 'NbBSEEnergy'))

    def setComputeBSEAngular(self, value):
        self.set('ResultDistribution', 'ComputeBSEAngular', int(value))

    def isComputeBSEAngular(self):
        return bool(int(self.get('ResultDistribution', 'ComputeBSEAngular')))

    def setNbBSEAngular(self, value):
        self.set('ResultDistribution', 'NbBSEAngular', value)

    def getNbBSEAngular(self):
        return int(self.get('ResultDistribution', 'NbBSEAngular'))



    def setComputeSEDistribution(self, value):
        self.set('ResultDistribution', 'ComputeSEDistribution', int(value))

    def isComputeSEDistribution(self):
        return bool(int(self.get('ResultDistribution', 'ComputeSEDistribution')))



    def setComputeEnergyLossDistribution(self, value):
        self.set('ResultDistribution', 'ComputeEnergyLossDistribution', int(value))

    def isComputeEnergyLossDistribution(self):
        return bool(int(self.get('ResultDistribution', 'ComputeEnergyLossDistribution')))

    def checkEnergyLossDistribution(self):
        value = self.isComputeEnergyLossDepth() or \
                self.isComputeEnergyLossLateral() or \
                self.isComputeEnergyLossRadial() or \
                self.isComputeEnergyLossSpatial()
        self.setComputeEnergyLossDistribution(value)

    def setComputeEnergyLossDepth(self, value):
        self.set('ResultDistribution', 'ComputeEnergyLossDepth', int(value))

    def isComputeEnergyLossDepth(self):
        return bool(int(self.get('ResultDistribution', 'ComputeEnergyLossDepth')))

    def setNbEnergyLossDepth(self, value):
        return self.set('ResultDistribution', 'NbEnergyLossDepth', value)

    def getNbEnergyLossDepth(self):
        return int(self.set('ResultDistribution', 'NbEnergyLossDepth'))

    def setComputeEnergyLossLateral(self, value):
        self.set('ResultDistribution', 'ComputeEnergyLossLateral', int(value))

    def isComputeEnergyLossLateral(self):
        return bool(int(self.get('ResultDistribution', 'ComputeEnergyLossLateral')))

    def setNbEnergyLossLateral(self, value):
        return self.set('ResultDistribution', 'NbEnergyLossLateral', value)

    def getNbEnergyLossLateral(self):
        return int(self.set('ResultDistribution', 'NbEnergyLossLateral'))

    def setComputeEnergyLossSpatial(self, value):
        self.set('ResultDistribution', 'ComputeEnergyLossSpatial', int(value))

    def isComputeEnergyLossSpatial(self):
        return bool(int(self.get('ResultDistribution', 'ComputeEnergyLossSpatial')))

    def setNbEnergyLossSpatial(self, value):
        return self.set('ResultDistribution', 'NbEnergyLossSpatial', value)

    def getNbEnergyLossSpatial(self):
        return int(self.set('ResultDistribution', 'NbEnergyLossSpatial'))

    def setComputeEnergyLossRadial(self, value):
        self.set('ResultDistribution', 'ComputeEnergyLossRadial', int(value))

    def isComputeEnergyLossRadial(self):
        return bool(int(self.get('ResultDistribution', 'ComputeEnergyLossRadial')))

    def setNbEnergyLossRadial(self, value):
        return self.set('ResultDistribution', 'NbEnergyLossRadial', value)

    def getNbEnergyLossRadial(self):
        return int(self.set('ResultDistribution', 'NbEnergyLossRadial'))



    def setComputeElectronDistribution(self, value):
        self.set('ResultDistribution', 'ComputeElectronDistribution', int(value))

    def isComputeElectronDistribution(self):
        return bool(int(self.get('ResultDistribution', 'ComputeElectronDistribution')))

    def checkElectronDistribution(self):
        value = self.isComputeElectronDepth() or \
                self.isComputeElectronLateral() or \
                self.isComputeElectronRadial() or \
                self.isComputeElectronSpatial()
        self.setComputeElectronDistribution(value)

    def setComputeElectronDepth(self, value):
        self.set('ResultDistribution', 'ComputeElectronDepth', int(value))

    def isComputeElectronDepth(self):
        return bool(int(self.get('ResultDistribution', 'ComputeElectronDepth')))

    def setNbElectronDepth(self, value):
        return self.set('ResultDistribution', 'NbElectronDepth', value)

    def getNbElectronDepth(self):
        return int(self.set('ResultDistribution', 'NbElectronDepth'))

    def setComputeElectronRadial(self, value):
        self.set('ResultDistribution', 'ComputeElectronRadial', int(value))

    def isComputeElectronRadial(self):
        return bool(int(self.get('ResultDistribution', 'ComputeElectronRadial')))

    def setNbElectronRadial(self, value):
        return self.set('ResultDistribution', 'NbElectronRadial', value)

    def getNbElectronRadial(self):
        return int(self.set('ResultDistribution', 'NbElectronRadial'))

    def setComputeElectronSpatial(self, value):
        self.set('ResultDistribution', 'ComputeElectronSpatial', int(value))

    def isComputeElectronSpatial(self):
        return bool(int(self.get('ResultDistribution', 'ComputeElectronSpatial')))

    def setNbElectronSpatial(self, value):
        return self.set('ResultDistribution', 'NbElectronSpatial', value)

    def getNbElectronSpatial(self):
        return int(self.set('ResultDistribution', 'NbElectronSpatial'))

    def setComputeElectronLateral(self, value):
        self.set('ResultDistribution', 'ComputeElectronLateral', int(value))

    def isComputeElectronLateral(self):
        return bool(int(self.get('ResultDistribution', 'ComputeElectronLateral')))

    def setNbElectronLateral(self, value):
        return self.set('ResultDistribution', 'NbElectronLateral', value)

    def getNbElectronLateral(self):
        return int(self.set('ResultDistribution', 'NbElectronLateral'))



    def getFactorB(self):
        return float(self.get('OptionAdvanced', 'factorb'))

    def setFactorB(self, value):
        self.set('OptionAdvanced', 'factorb', value)

    def getFactorK(self):
        return float(self.get('OptionAdvanced', 'factork'))

    def setFactorK(self, value):
        self.set('OptionAdvanced', 'factork', value)

    def getFactorL(self):
        return float(self.get('OptionAdvanced', 'factorl'))

    def setFactorL(self, value):
        self.set('OptionAdvanced', 'factorl', value)

    def getFactorM(self):
        return float(self.get('OptionAdvanced', 'factorm'))

    def setFactorM(self, value):
        self.set('OptionAdvanced', 'factorm', value)



    def getNumberFilm(self):
        return int(self.get('OptionAdvanced', 'nbfilm'))

    def setNumberFilm(self, value):
        self.set('OptionAdvanced', 'nbfilm', value)

    def getNumberWindow(self):
        return int(self.get('OptionAdvanced', 'nbwindow'))

    def setNumberWindow(self, value):
        self.set('OptionAdvanced', 'nbwindow', value)

    def isThrowWarning(self):
        return bool(int(self.get('OptionAdvanced', 'throwwarning')))

    def setThrowWarning(self, value):
        self.set('OptionAdvanced', 'throwwarning', int(value))



    def setSaveFile(self, value):
        """
        Whether to automatically save the results.
        """
        self.set('OptionResultGeneral', 'SaveFile', int(value))

    def isSaveFile(self):
        return bool(int(self.get('OptionResultGeneral', 'SaveFile')))

    def setDisplayGeneral(self, value):
        self.set('OptionResultGeneral', 'DisplayGeneral', int(value))

    def isDisplayGeneral(self):
        return bool(int(self.get('OptionResultGeneral', 'DisplayGeneral')))



    def setResultsPath(self, path):
        """
        Sets the location where the simulation results are saved.
        """
        self.set('Path', 'ResultsPath', path)

    def getResultsPath(self):
        """
        Gets the location where the simulation results are saved.
        """
        return self.get('Path', 'ResultsPath')

# TODO: ElectricField

    def setExperiment(self, experiment):
        if ATOMICNUMBER in experiment:
            atomicNumber = experiment[ATOMICNUMBER]
            #self.setElement(atomicNumber)
            atomicNumbers = [atomicNumber]
            weightFractions = [1.0]
            self.setElements(atomicNumbers, weightFractions)

        if TYPECROSSSECTION in experiment:
            type = experiment[TYPECROSSSECTION]
            self.setTypeElectronElasticCrossSection(type)

        if TYPETOTALCROSSSECTION in experiment:
            type = experiment[TYPETOTALCROSSSECTION]
            self.setTypeTotalCrossSection(type)

        if TYPEPARTIALCROSSSECTION in experiment:
            type = experiment[TYPEPARTIALCROSSSECTION]
            self.setTypePartialCrossSection(type)

        if INCIDENTENERGY_KEV in experiment:
            energy_keV = experiment[INCIDENTENERGY_KEV]
            self.setIncidentenergy(energy_keV)

