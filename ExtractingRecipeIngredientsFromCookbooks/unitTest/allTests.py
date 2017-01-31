import unittest
from parserForDavidisCookbook.unitTest.XmlParserTest import XmlParserTest
from parserForDavidisCookbook.unitTest.XmlHelperTest import XmlHelperTest
from model.unitTest.WordPropertyTest import WordPropertyTest
from informationExtraction.unitTest.IngredientExtractorTest import IngredientExtractorTest
from informationExtraction.unitTest.DictBasedExtractorTest import DictBasedExtractorTest
from informationExtraction.unitTest.DissolveAmbiguityRulesTest import DissolveAmbiguityRulesTest
from informationExtraction.unitTest.EntityRelationRulesTest import EntityRelationRulesTest
from informationExtraction.unitTest.TextualHelperTest import TextualHelperTest 
from informationExtraction.unitTest.QuantityExtractorTest import QuantityExtractorTest
from informationExtraction.unitTest.UnitExtractorTest import UnitExtractorTest
from informationExtraction.unitTest.ExtractorTest import ExtractorTest
from evaluation.unitTest.EvalRecipesTest import EvalRecipesTest 
from evaluation.unitTest.ComparatorTest import ComparatorTest 

def getTests():
    return [unittest.TestLoader().loadTestsFromTestCase(XmlParserTest),
            unittest.TestLoader().loadTestsFromTestCase(XmlHelperTest),
            unittest.TestLoader().loadTestsFromTestCase(WordPropertyTest),
            unittest.TestLoader().loadTestsFromTestCase(DictBasedExtractorTest),
            unittest.TestLoader().loadTestsFromTestCase(DissolveAmbiguityRulesTest),
            unittest.TestLoader().loadTestsFromTestCase(EntityRelationRulesTest),
            unittest.TestLoader().loadTestsFromTestCase(IngredientExtractorTest),
            unittest.TestLoader().loadTestsFromTestCase(TextualHelperTest),
            unittest.TestLoader().loadTestsFromTestCase(QuantityExtractorTest),
            unittest.TestLoader().loadTestsFromTestCase(UnitExtractorTest),
            unittest.TestLoader().loadTestsFromTestCase(ExtractorTest),
            unittest.TestLoader().loadTestsFromTestCase(EvalRecipesTest),
            unittest.TestLoader().loadTestsFromTestCase(ComparatorTest)
            ]

if __name__ == '__main__':
    testSuite = unittest.TestSuite(getTests())
    unittest.TextTestRunner(verbosity=0).run(testSuite)