import unittest
from informationExtraction.IngredientExtractor import IngredientExtractor
from xml.dom.minidom import parse
from informationExtraction.UnitExtractor import UnitExtractor
from informationExtraction.dictBasedExtractor import dictBasedEnrichment
from model.WordProperty import WordProperty
from informationExtraction.altGrpRules import altGrpRule
from unitTest.pathToFiles import pathToListIngredients


class AltGrpRuleTest(unittest.TestCase):

    def setUp(self):
        self.ingE = IngredientExtractor(parse(pathToListIngredients))
        self.unitE = UnitExtractor()
        
    def test1(self):
        s = "Der Soja macht die Suppe gewürzreicher, kann jedoch gut wegbleiben, und \
statt Madeira kann man weißen Franzwein und etwas Rum nehmen"
        wordProperties = dictBasedEnrichment(s, self.ingE, self.unitE)
        wordProperties = altGrpRule(wordProperties, None)
        self.assertEqual("1", wordProperties[14].properties.get(WordProperty.ALT_GRP))
        self.assertEqual("2", wordProperties[18].properties.get(WordProperty.ALT_GRP))
        self.assertEqual("2", wordProperties[21].properties.get(WordProperty.ALT_GRP))
        
        
    def test2(self):
        s = "Der Soja macht die Suppe gewürzreicher, kann jedoch gut wegbleiben, und \
statt Madeira kann man weißen Franzwein nehmen, desweiteren Rum rein tun"
        wordProperties = dictBasedEnrichment(s, self.ingE, self.unitE)
        wordProperties = altGrpRule(wordProperties, None)
        self.assertEqual("1", wordProperties[14].properties.get(WordProperty.ALT_GRP))
        self.assertEqual("2", wordProperties[18].properties.get(WordProperty.ALT_GRP))
        self.assertIsNone(wordProperties[22].properties.get(WordProperty.ALT_GRP))
        


if __name__ == "__main__":
    unittest.main()