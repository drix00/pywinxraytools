#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2009 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision$"
__svnDate__ = "$Date$"
__svnId__ = "$Id$"

# Standard library modules.
import os
import zipfile
import os.path
import logging

# Third party modules.

# Local modules.

# Globals and constants variables.
OPTION_FILENAME = "Option.wxc"

def getAllPathsFromFolder(basepath):
    paths = []

    for dirpath, dirnames, filenames in os.walk(basepath):
        if OPTION_FILENAME in filenames:
            paths.append(dirpath)

    return paths

def getAllPathsFromZip(zipPath):
    zipFile = zipfile.ZipFile(zipPath)

    paths = []

    for filename in zipFile.namelist():
        if OPTION_FILENAME in filename:
            path = os.path.dirname(filename)
            path = os.path.normpath(path)
            paths.append(path)
            logging.debug("Added %s from zip.", path)

    return paths

if __name__ == '__main__':    #pragma: no cover
    import DrixUtilities.Runner as Runner
    Runner.Runner().run(runFunction=None)
