import unittest
from parserForDavidisCookbook.unitTest.XmlParserTest import XmlParserTest
from parserForDavidisCookbook.unitTest.XmlHelperTest import XmlHelperTest
from informationExtraction.unitTest.IngredientExtractorTest import IngredientExtractorTest
from informationExtraction.unitTest.DictBasedExtractorTest import DictBasedExtractorTest
from informationExtraction.unitTest.LemmatizationTest import  LemmatizationTest

def getTests():
    return [unittest.TestLoader().loadTestsFromTestCase(XmlParserTest),
            unittest.TestLoader().loadTestsFromTestCase(XmlHelperTest),
            unittest.TestLoader().loadTestsFromTestCase(LemmatizationTest),
            unittest.TestLoader().loadTestsFromTestCase(IngredientExtractorTest),
            unittest.TestLoader().loadTestsFromTestCase(DictBasedExtractorTest),
            ]

if __name__ == '__main__':
    testSuite = unittest.TestSuite(getTests())
    unittest.TextTestRunner(verbosity=0).run(testSuite)