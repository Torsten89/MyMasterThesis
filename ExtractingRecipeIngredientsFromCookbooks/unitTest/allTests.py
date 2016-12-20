import unittest
from parserForDavidisCookbook.unitTest.RecipeTest import RecipeTest
from parserForDavidisCookbook.unitTest.XmlParserTest import XmlParserTest
from informationExtraction.unitTest.IngredientExtractorTest import IngredientDictTest
from informationExtraction.unitTest.TaggerTest import TaggerTest

def getTests():
    return [unittest.TestLoader().loadTestsFromTestCase(RecipeTest),
            unittest.TestLoader().loadTestsFromTestCase(XmlParserTest),
            unittest.TestLoader().loadTestsFromTestCase(IngredientDictTest),
            unittest.TestLoader().loadTestsFromTestCase(TaggerTest),
            ]

if __name__ == '__main__':
    testSuite = unittest.TestSuite(getTests())
    unittest.TextTestRunner(verbosity=0).run(testSuite)