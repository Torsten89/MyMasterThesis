import unittest
from informationExtraction.IngredientExtractor import IngredientExtractor
from xml.dom.minidom import parse
from informationExtraction.UnitExtractor import UnitExtractor
from informationExtraction.dictBasedExtractor import dictBasedEnrichment
from model.WordProperty import WordProperty
from informationExtraction.optionalRules import optionalRule
from unitTest.pathToFiles import pathToListIngredients


class OptionalRuleTest(unittest.TestCase):

    def setUp(self):
        self.ingE = IngredientExtractor(parse(pathToListIngredients))
        self.unitE = UnitExtractor()
        
    def test1(self):
        s = "Der Soja macht die Suppe gewürzreicher, kann jedoch gut wegbleiben, und \
statt Madeira kann man weißen Franzwein und etwas Rum nehmen"
        wordProperties = dictBasedEnrichment(s, self.ingE, self.unitE)
        self.assertIsNotNone(wordProperties[1].properties.get(WordProperty.INGREDIENT), "dictbasedEnrichment is already broken")
        wordProperties = optionalRule(wordProperties, None)
        self.assertTrue(wordProperties[1].properties.get(WordProperty.OPTIONAL))
        
        


if __name__ == "__main__":
    unittest.main()