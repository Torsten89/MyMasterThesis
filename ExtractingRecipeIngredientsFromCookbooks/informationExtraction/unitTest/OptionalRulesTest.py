import unittest
from informationExtraction.IngredientExtractor import IngredientExtractor
from xml.dom.minidom import parse
from informationExtraction.UnitExtractor import UnitExtractor
from informationExtraction.dictBasedExtractor import dictBasedEnrichment
from model.WordProperty import WordProperty
from informationExtraction.optionalRules import optionalRule


class OptionalRuleTest(unittest.TestCase):

    def setUp(self):
        self.ingE = IngredientExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml"))
        self.unitE = UnitExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/cueML/cueML_v0.5.rng"))
        
    def test1(self):
        s = "Der Soja macht die Suppe gewürzreicher, kann jedoch gut wegbleiben, und \
statt Madeira kann man weißen Franzwein und etwas Rum nehmen"
        wordProperties = dictBasedEnrichment(s, self.ingE, self.unitE)
        self.assertIsNotNone(wordProperties[1].properties.get(WordProperty.ingredient), "dictbasedEnrichment is already broken")
        wordProperties = optionalRule(wordProperties, None)
        self.assertTrue(wordProperties[1].properties.get(WordProperty.optional))
        
        


if __name__ == "__main__":
    unittest.main()