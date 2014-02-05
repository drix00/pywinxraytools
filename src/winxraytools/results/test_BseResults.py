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
__svnId__ = "$Id: test_BseResults.py 2364 2011-05-30 11:15:15Z hdemers $"

# Standard library modules.
import unittest
import logging
import os.path

# Third party modules.

# Local modules.
import BseResults
import DrixUtilities.Files as Files
from DrixUtilities.Testings import ignore

# Globals and constants variables.

class TestBseResults(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.path = Files.getCurrentModulePath(__file__, "../testData/ana 644_001")

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    @ignore()
    def test_ReadFile(self):
        bseResult = BseResults.BseResults(self.path)

        self.assertAlmostEquals(0.301, bseResult.getBseYield())
        self.assertAlmostEquals(0.0137608, bseResult.getBseYieldError())

        #self.fail("Test if the TestCase is working.")
        self.assertTrue(True)

    @ignore()
    def test_extractData(self):
        lines = open(os.path.join(self.path, BseResults.FILENAME)).readlines()

        results = BseResults.BseResults()._extractData(lines)

        self.assertTrue(BseResults.BSE_YIELD in results)

        bseValue, bseError = results[BseResults.BSE_YIELD]

        self.assertAlmostEquals(0.301, bseValue)
        self.assertAlmostEquals(0.0137608, bseError)

        #self.fail("Test if the testcase is working.")
        self.assert_(True)

if __name__ == '__main__': #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    unittest.main()
