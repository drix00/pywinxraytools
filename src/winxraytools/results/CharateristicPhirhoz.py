#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2007 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision: 2916 $"
__svnDate__ = "$Date: 2013-10-13 21:11:26 -0400 (Sun, 13 Oct 2013) $"
__svnId__ = "$Id: CharateristicPhirhoz.py 2916 2013-10-14 01:11:26Z hdemers $"

# Standard library modules.
import warnings
import os.path

# Third party modules.

# Local modules.

# Globals and constants variables.

class CharateristicPhirhoz(object):
    """
    Read the results file "XCharIntensity_Reg1.txt" generated by winxray program.

    """
    def __init__(self, path=None):
        """
        Constructor.

         path - folder where the file could be found.

        """
        self.path = path
        self.filenameList = {"Emitted": "XCharPRZEm_Reg1.txt"
                                                 , "Generated": "XCharPRZGen_Reg1.txt"}

        self.data = {}

        if self.path:
            if os.path.exists(self.path):
                for xrayType in self.filenameList:
                    self.readFile(os.path.join(self.path, self.filenameList[xrayType]), xrayType)
            else:
                raise ValueError("Path does not exists: " + path)

    def readFile(self, filename, xrayType):
        """
        Read all lines of the file and extract data.

        """
        lines = open(filename, 'r').readlines()

        self.extractData(lines, xrayType)

    def extractData(self, lines, xrayType):
        headers = self.extractHeader(lines[0])

        data = {}

        for value in headers:
            data.setdefault(value, [])

        for line in lines[1:]:
            values = line.split("\t")

            if values[-1].isspace() or len(values[-1]) == 0:
                #print "isspace: %s" % values[-1]
                del values[-1]

            if len(values) > 1:
                assert len(headers) == len(values)

                for index, key in enumerate(headers):
                    data[key].append(float(values[index]))

        # Change the order of the data.
#        for key in data:
#            data[key].reverse()

        self.data.setdefault(xrayType, {})

        for key in data:
            xrayLine, atomicNumber, dataType = self.extractInfo(key)

            if dataType == 'Z (nm)':
                self.data[xrayType]['Z (nm)'] = data[key]

            if dataType == 'value':
                self.data[xrayType].setdefault('phirhoz', {})
                self.data[xrayType]['phirhoz'].setdefault(atomicNumber, {})
                self.data[xrayType]['phirhoz'][atomicNumber][xrayLine] = data[key]

            if dataType == 'error':
                self.data[xrayType].setdefault('phirhoz error', {})
                self.data[xrayType]['phirhoz error'].setdefault(atomicNumber, {})
                self.data[xrayType]['phirhoz error'][atomicNumber][xrayLine] = data[key]

    def extractHeader(self, line):
        headers = line.split("\t")

        if headers[-1].isspace() or len(headers[-1]) == 0:
            #print "isspace: %s" % headers[-1]
            #print headers[-1]
            del headers[-1]

        #print headers
        return headers

    def extractInfo(self, key):
        if 'Error' in key:
            dataType = 'error'
        elif 'Z (nm)' in key:
            dataType = 'Z (nm)'
        else:
            dataType = 'value'

        if dataType == 'value':
            pos = key.rfind('PRZ')
            #print pos, key[pos-2:pos]
        elif dataType == 'error':
            pos = key.rfind('Error')
            #print pos, key[:pos-2], key[pos-2:pos]
        else:
            return None, None, dataType

        lineZ = key[:pos]

        if 'Ka1' in lineZ:
            xrayLine = 'Ka1'
        elif 'Ka2' in lineZ:
            xrayLine = 'Ka2'
        elif 'Kb1' in lineZ:
            xrayLine = 'Kb1'
        elif 'Kb2' in lineZ:
            xrayLine = 'Kb2'
        elif 'La' in lineZ:
            xrayLine = 'La'
        elif 'Lb1' in lineZ:
            xrayLine = 'Lb1'
        elif 'Lb2' in lineZ:
            xrayLine = 'Lb2'
        elif 'Lg' in lineZ:
            xrayLine = 'Lg'
        elif 'Ma' in lineZ:
            xrayLine = 'Ma'
        elif 'K' in lineZ:
            xrayLine = 'K'
        elif 'L' in lineZ:
            xrayLine = 'L'
        elif 'M' in lineZ:
            xrayLine = 'M'

        pos = key.find(xrayLine) + len(xrayLine)
        atomicNumber = int(lineZ[pos:])

        assert atomicNumber != None

        return xrayLine, atomicNumber, dataType

    def computeMaximumDepth(self, data, limit=0.9973):
        for atomicNumber in data['phirhoz']:
            for xrayLine in data['phirhoz'][atomicNumber]:
                data.setdefault('maxZ (nm)', {})
                data['maxZ (nm)'].setdefault(atomicNumber, {})

                #print key, dataType
                total = sum(data['phirhoz'][atomicNumber][xrayLine])

                #print total

                cumulative = []
                cumulativeValue = 0.0

                tmpData = data['phirhoz'][atomicNumber][xrayLine][:]
                tmpData.reverse()

                for value in tmpData:
                    cumulativeValue += value
                    cumulative.append(cumulativeValue / total)

                cumulative.reverse()
                for index, value in enumerate(cumulative):
                    if value <= limit:
                        #print index, value, data['Z (nm)'][index]
                        data['maxZ (nm)'][atomicNumber][xrayLine] = data['Z (nm)'][index]
                        break

    def getMaximumDepth(self, xrayType, atomicNumber=None, xrayLine=None):
        key = 'maxZ (nm)'

        if not key in self.data[xrayType]:
            self.computeMaximumDepth(self.data[xrayType])

        if atomicNumber != None:
            if atomicNumber in self.data[xrayType][key]:
                if xrayLine != None:
                    if xrayLine in self.data[xrayType][key][atomicNumber]:
                        return self.data[xrayType][key][atomicNumber][xrayLine]
                else:
                    return self.data[xrayType][key][atomicNumber]
        else:
            return self.data[xrayType][key]

    def computeIntegral(self, data):
        key = 'F'
        if 'phirhoz' in data:
            for atomicNumber in data['phirhoz']:
                for xrayLine in data['phirhoz'][atomicNumber]:

                    step = data['Z (nm)'][1] - data['Z (nm)'][0]

                    data.setdefault(key, {})
                    data[key].setdefault(atomicNumber, {})

                    total = sum(data['phirhoz'][atomicNumber][xrayLine])

                    integral = total * step

                    data[key][atomicNumber][xrayLine] = integral
        else:
            message = "No phirhoz data."
            warnings.warn(message)

    def getIntegral(self, xrayType, atomicNumber=None, xrayLine=None):
        # TODO: Check if it work correctly when no data is available.

        key = 'F'

        if not key in self.data[xrayType]:
            self.computeIntegral(self.data[xrayType])

        if not key in self.data[xrayType]:
            return 0.0

        if atomicNumber != None:
            if atomicNumber in self.data[xrayType][key]:
                if xrayLine != None:
                    if xrayLine in self.data[xrayType][key][atomicNumber]:
                        return self.data[xrayType][key][atomicNumber][xrayLine]
                else:
                    return self.data[xrayType][key][atomicNumber]
        else:
            return self.data[xrayType][key]

    def correctXRayLine(self, xrayLine):
        if len(xrayLine) == 1:
            return xrayLine

        if xrayLine[:2] == 'Ka':
            xrayLine = 'Ka1'

        if xrayLine[:2] == 'Kb':
            xrayLine = 'Kb1'

        if xrayLine[:2] == 'La':
            xrayLine = 'La'

        if xrayLine[:2] == 'Lb':
            xrayLine = 'Lb1'

        if xrayLine[:2] == 'Lg':
            xrayLine = 'Lg'

        if xrayLine[:2] == 'Ma':
            xrayLine = 'Ma'

        if xrayLine[:2] == 'Mb':
            xrayLine = 'Ma'

        return xrayLine

    def getPhirhozs(self, xrayType, atomicNumber=None, xrayLine=None):
        phirhozs = {}

        depth_nm = []
        for value in self.data[xrayType]['Z (nm)']:
            depth_nm.append(-value)

        if atomicNumber != None:
            if atomicNumber in self.data[xrayType]['phirhoz']:
                if xrayLine != None:
                    xrayLine = self.correctXRayLine(xrayLine)

                    if xrayLine in self.data[xrayType]['phirhoz'][atomicNumber]:
                        #print xrayLine, self.data[xrayType]['phirhoz'][atomicNumber].keys()

                        phirhoz = self.data[xrayType]['phirhoz'][atomicNumber][xrayLine]

                        phirhozError = self.data[xrayType]['phirhoz error'][atomicNumber][xrayLine]

                        return depth_nm, phirhoz, phirhozError
                    else:
                        message = "No line %s for element %i" % (xrayLine, atomicNumber)
                        warnings.warn(message)

                        return [], [], []

                else:
                    for xrayLine in self.data[xrayType]['phirhoz'][atomicNumber]:
                        phirhoz = self.data[xrayType]['phirhoz'][atomicNumber][xrayLine]

                        phirhozError = self.data[xrayType]['phirhoz error'][atomicNumber][xrayLine]

                        phirhozs[xrayLine] = (depth_nm, phirhoz, phirhozError)

                    return phirhozs
        else:
            if 'phirhoz' in self.data[xrayType]:
                for atomicNumber in self.data[xrayType]['phirhoz']:
                    phirhozs.setdefault(atomicNumber, {})

                    for xrayLine in self.data[xrayType]['phirhoz'][atomicNumber]:
                        phirhoz = self.data[xrayType]['phirhoz'][atomicNumber][xrayLine]

                        phirhozError = self.data[xrayType]['phirhoz error'][atomicNumber][xrayLine]

                        phirhozs[atomicNumber][xrayLine] = (depth_nm, phirhoz, phirhozError)

                return phirhozs
            else:
                return [], [], []

