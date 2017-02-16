import unittest
from informationExtraction.IngredientExtractor import IngredientExtractor
from xml.dom.minidom import parse
from informationExtraction.UnitExtractor import UnitExtractor
from informationExtraction.dictBasedExtractor import dictBasedEnrichment
from informationExtraction.dontUseRules import dontUseRule
from model.WordProperty import WordProperty


class DontUseRuleTest(unittest.TestCase):

    def setUp(self):
        self.ingE = IngredientExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml"))
        self.unitE = UnitExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/cueML/cueML_v0.5.rng"))
        
    def testIngredient1(self):
        s = "Das Kalbfleisch wie in No. 1, nach der Personenzahl, doch etwas reichlicher \
genommen, da solches weniger Kraft gibt, als Rindfleisch."
        wordProperties = dictBasedEnrichment(s, self.ingE, self.unitE)
        self.assertIsNotNone(wordProperties[23].properties.get(WordProperty.INGREDIENT), "dictbasedEnrichment is already broken")
        wordProperties = dontUseRule(wordProperties, None)
        self.assertIsNone(wordProperties[23].properties.get(WordProperty.INGREDIENT))
        
        


if __name__ == "__main__":
    unittest.main()