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
__svnId__ = "$Id: WinxrayRegion.py 2364 2011-05-30 11:15:15Z hdemers $"

# Standard library modules.

# Third party modules.

# Local modules.
import DatabasesTools.ElementProperties as ElementProperties

# Globals and constants variables.

class WinxrayRegion(object):
    def __init__(self, atomicNumbers, weightFractions, atomicFractions, massDensities):
        self.atomicNumbers = atomicNumbers
        self.weightFractions = weightFractions
        self.atomicFractions = atomicFractions
        self.massDensities = massDensities

        if self.massDensities == None:
            self.massDensities = []

            for atomicNumber in self.atomicNumbers:
                self.massDensities.append(ElementProperties.getMassDensity_g_cm3(atomicNumber))

        if self.weightFractions == None and self.atomicFractions == None:
            raise ValueError, "Need to set weight fraction or atomic fraction"

        if self.weightFractions == None:
            self.weightFractions = self.computeWeightFractions()

        if self.atomicFractions == None:
            self.atomicFractions = self.computeAtomicFractions()

        self.checkElements()

        assert len(self.atomicNumbers) == len(self.weightFractions)
        assert len(self.atomicNumbers) == len(self.atomicFractions)
        assert len(self.atomicNumbers) == len(self.massDensities)

    def getAtomicnumbers(self):
        return self.atomicNumbers

    def getWeightFraction(self):
        return self.weightFractions

    def getAtomicFraction(self):
        return self.atomicFractions

    def getMassDensities(self):
        return self.massDensities

    def computeWeightFractions(self):
        """
         * Compute the weight fraction for all elements in this region.
         *
         * \f[
         *     f_{i}^{w} = \frac{f_{i}^{A} \cdot A_{i}}{\sum_{j} f_{j}^{A} \cdot A_{j}}
         * \f]
        """
        total = 0.0
        for index,atomicNumber in enumerate(self.atomicNumbers):
            total += self.atomicFractions[index]*ElementProperties.getAtomicMass_g_mol(atomicNumber)

        weightFractions = []

        for index,atomicNumber in enumerate(self.atomicNumbers):
            value = self.atomicFractions[index]*ElementProperties.getAtomicMass_g_mol(atomicNumber)
            value /= total

            weightFractions.append(value)

        return weightFractions

    def computeAtomicFractions(self):
        """
         * Compute the atomic fraction for all elements in this region.
         *
         * \f[
         *     f_{i}^{A} = \frac{ \frac{f_{i}^{w}}{A_{i}} } {\sum_{j} \frac{f_{j}^{w}}{A_{j}}}
         * \f]
         *
         * @param[in] elementList Element list.
        """
        total = 0.0

        for index,atomicNumber in enumerate(self.atomicNumbers):
            total += self.weightFractions[index]/ElementProperties.getAtomicMass_g_mol(atomicNumber)

        atomicFractions = []

        for index,atomicNumber in enumerate(self.atomicNumbers):
            value = self.weightFractions[index]/ElementProperties.getAtomicMass_g_mol(atomicNumber)
            value /= total

            atomicFractions.append(value)

        return atomicFractions

    def createLabel(self):
        """
         * Generate a label for the region from all elements in this region.
         *
         * @param[in] elementList Element list.
        """
        label = ""

        for atomicNumber in self.atomicNumbers:
            label += ElementProperties.getSymbol(atomicNumber)

        return label

    def computeTotalWeightFraction(self):
        return sum(self.weightFractions)

    def computeTotalAtomicFraction(self):
        return sum(self.atomicFractions)

    def computeMeanDensity(self):
        """
         * Compute the mean density of the region from all elements in this region.
         *
         * \f[
         * \overline{\rho} = \frac{1}{\sum_{i} \frac{f_{i}^{w}}{\rho_{i}}}
         * \f]
         *
         * \f[
         * \overline{\rho}^{-1} =\sum_{i} \frac{f_{i}^{w}}{\rho_{i}}
         * \f]
         * @param[in] elementList Element list.
        """
        total = 0.0

        for index,atomicNumber in enumerate(self.atomicNumbers):
            if self.massDensities[index] <= 0.0:
                print atomicNumber

            total += self.weightFractions[index]/self.massDensities[index]

        if total <= 0.0:
            print self.atomicNumbers

        total = 1.0/total

        return total

    def computeMeanZ(self):
        """
         * Compute the mean atomic mass of the region from all elements in this region.
         *
         * \f[
         *     \overline{Z} = f_{i}^{w} \cdot Z_{i}
         * \f]
         *
         * @param[in] elementList Element list.
        """
        total = 0.0

        for index,atomicNumber in enumerate(self.atomicNumbers):
            total += self.weightFractions[index]*atomicNumber

        return total

    def computeMeanAtomicMass(self):
        """
         * Compute the mean atomic mass of the region from all elements in this region.
         *
         * \f[
         *     \overline{A} = f_{i}^{w} \cdot A_{i}
         * \f]
         *
         * @param[in] elementList Element list.
        """
        total = 0.0

        for index,atomicNumber in enumerate(self.atomicNumbers):
            total += self.weightFractions[index]*ElementProperties.getAtomicMass_g_mol(atomicNumber)

        return total

    def computeAtomicDensities_atom_cm3(self):
        """
         * Compute the mean atomic mass of the region from all elements in this region.
         *
         * \f[
         *     \overline{A} = f_{i}^{w} \cdot A_{i}
         * \f]
         *
         * @param[in] elementList Element list.
        """
        atomicDensities_atom_cm3 = []

        meanDensity_g_cm3 = self.computeMeanDensity()

        for index,atomicNumber in enumerate(self.atomicNumbers):
            atomicDensity_atom_cm3 = self.weightFractions[index]
            atomicDensity_atom_cm3 *= ElementProperties.g_AvogadroNumber_atom_mol
            atomicDensity_atom_cm3 *= meanDensity_g_cm3
            atomicDensity_atom_cm3 /= ElementProperties.getAtomicMass_g_mol(atomicNumber)

            atomicDensities_atom_cm3.append(atomicDensity_atom_cm3)

        return atomicDensities_atom_cm3

    def checkElements(self):
        atomicNumbers = self.atomicNumbers[:]
        weightFractions = self.weightFractions[:]
        atomicFractions = self.atomicFractions[:]
        massDensities = self.massDensities[:]

        self.atomicNumbers = []
        self.weightFractions = []
        self.atomicFractions = []
        self.massDensities = []

        for index,atomicNumber in enumerate(atomicNumbers):
            if weightFractions[index] > 0.0:
                #print atomicNumber, weightFractions[index]
                self.atomicNumbers.append(atomicNumber)
                self.weightFractions.append(weightFractions[index])
                self.atomicFractions.append(atomicFractions[index])
                self.massDensities.append(massDensities[index])

if __name__ == '__main__': #pragma: no cover
    import DrixUtilities.Runner as Runner
    Runner.Runner().run(runFunction=None)
