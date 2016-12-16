import unittest
from recipeModel.unitTest.RecipeTest import RecipeTest
from parserForDavidisCookbook.unitTest.XmlParserTest import XmlParserTest

def getTests():
    return [unittest.TestLoader().loadTestsFromTestCase(RecipeTest),
            unittest.TestLoader().loadTestsFromTestCase(XmlParserTest)
            ]

if __name__ == '__main__':
    testSuite = unittest.TestSuite(getTests())
    unittest.TextTestRunner(verbosity=0).run(testSuite)