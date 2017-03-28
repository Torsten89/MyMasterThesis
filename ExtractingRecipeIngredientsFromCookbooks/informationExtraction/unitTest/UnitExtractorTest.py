import unittest
from informationExtraction.UnitExtractor import UnitExtractor
from xml.dom.minidom import parse


class UnitExtractorTest(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.uE = UnitExtractor()

    def testPfund(self):
        self.assertEqual("Pfund", self.uE.getUnit("Pfund"))
        
    def testNonUnit(self):   
        self.assertIsNone(self.uE.getUnit("aasdf")) 


if __name__ == "__main__":
    unittest.main()