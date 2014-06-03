#!/usr/bin/env python
"""Get all winxray simulation results from a zip file."""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2007 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision: 2364 $"
__svnDate__ = "$Date: 2011-05-30 07:15:15 -0400 (Mon, 30 May 2011) $"
__svnId__ = "$Id: ZipResults.py 2364 2011-05-30 11:15:15Z hdemers $"

# Standard library modules.
import zipfile
import tempfile
import os.path
import shutil
import warnings

# Third party modules.

# Local modules.
import winxraytools.results.Results as Results

# Globals and constants variables.

class ZipResults(object):
    def __init__(self, zipFilename):
        self.zipFilename = zipFilename

        self.folderList = self.extractFolderList(self.zipFilename)


    def extractFolderList(self, zipFilename):
        zipFile = zipfile.ZipFile(zipFilename, 'r')

        folderList = []

        for pathname in zipFile.namelist():
            folderpath, filename = os.path.split(pathname)

            if filename == 'Option.wxc':
                if not folderpath in folderList:
                    folderList.append(folderpath)

        return folderList

    def getAvailableSimulations(self):
        return self.folderList

    def getResults(self, folderName):
        results = None

        for folder in self.folderList:
            if folderName in folder:
                resultsPath = tempfile.mkdtemp()
                try:
                    with zipfile.ZipFile(self.zipFilename, 'r') as zipFile:
                        for pathname in zipFile.namelist():
                            if folderName in pathname:
                                filename = os.path.split(pathname)[1]

                                if filename != '':
                                    lines = zipFile.read(pathname)

                                    filePath = os.path.join(resultsPath, filename)
                                    with open(filePath, 'wb') as resultsFile:
                                        resultsFile.write(lines)

                    results = Results.Results(resultsPath)
                finally:
                    shutil.rmtree(resultsPath)

                break
        else:
            message = "Folder name (%s) not found in the zip file (%s)." % (folderName, self.zipFilename)
            warnings.warn(message)

        return results
