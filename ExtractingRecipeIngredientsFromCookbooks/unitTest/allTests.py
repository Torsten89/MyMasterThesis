import unittest
from parserForDavidisCookbook.unitTest.XmlParserTest import XmlParserTest
from parserForDavidisCookbook.unitTest.XmlHelperTest import XmlHelperTest
from parserForDavidisCookbook.unitTest.IngredientTest import IngredientTest
from informationExtraction.unitTest.IngredientExtractorTest import IngredientExtractorTest
from informationExtraction.unitTest.DictBasedExtractorTest import DictBasedExtractorTest
from informationExtraction.unitTest.DissolveAmbiguityRulesTest import DissolveAmbiguityRulesTest
from informationExtraction.unitTest.EntityRelationRulesTest import EntityRelationRulesTest
from informationExtraction.unitTest.ParseHelperTest import ParseHelperTest
from informationExtraction.unitTest.QuantityExtractorTest import QuantityExtractorTest
from informationExtraction.unitTest.UnitExtractorTest import UnitExtractorTest
from informationExtraction.unitTest.ExtractorTest import ExtractorTest

def getTests():
    return [unittest.TestLoader().loadTestsFromTestCase(XmlParserTest),
            unittest.TestLoader().loadTestsFromTestCase(XmlHelperTest),
            unittest.TestLoader().loadTestsFromTestCase(IngredientTest),
            unittest.TestLoader().loadTestsFromTestCase(DictBasedExtractorTest),
            unittest.TestLoader().loadTestsFromTestCase(DissolveAmbiguityRulesTest),
            unittest.TestLoader().loadTestsFromTestCase(EntityRelationRulesTest),
            unittest.TestLoader().loadTestsFromTestCase(IngredientExtractorTest),
            unittest.TestLoader().loadTestsFromTestCase(ParseHelperTest),
            unittest.TestLoader().loadTestsFromTestCase(QuantityExtractorTest),
            unittest.TestLoader().loadTestsFromTestCase(UnitExtractorTest),
            unittest.TestLoader().loadTestsFromTestCase(ExtractorTest)
            ]

if __name__ == '__main__':
    testSuite = unittest.TestSuite(getTests())
    unittest.TextTestRunner(verbosity=0).run(testSuite)