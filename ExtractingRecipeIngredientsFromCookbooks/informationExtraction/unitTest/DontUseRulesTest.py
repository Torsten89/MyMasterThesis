import unittest
from informationExtraction.IngredientExtractor import IngredientExtractor
from xml.dom.minidom import parse
from informationExtraction.UnitExtractor import UnitExtractor
from informationExtraction.dictBasedExtractor import dictBasedEnrichment
from informationExtraction.dontUseRules import dontUseRule
from model.WordProperty import WordProperty
from unitTest.pathToFiles import pathToListIngredients


class DontUseRuleTest(unittest.TestCase):

    def setUp(self):
        self.ingE = IngredientExtractor(parse(pathToListIngredients))
        self.unitE = UnitExtractor()
        
    def testIngredient1(self):
        s = " Es wird dies Alles ohne Ei und Salz in einem tiefen Topf auf sehr starkem Feuer bis vor dem Kochen ohne Aufhören stark gerührt."
        wordProperties = dictBasedEnrichment(s, self.ingE, self.unitE)
        self.assertIsNotNone(wordProperties[5].properties.get(WordProperty.INGREDIENT), "dictbasedEnrichment is already broken")
        wordProperties = dontUseRule(wordProperties, None)
        self.assertIsNone(wordProperties[5].properties.get(WordProperty.INGREDIENT))
        
        


if __name__ == "__main__":
    unittest.main()