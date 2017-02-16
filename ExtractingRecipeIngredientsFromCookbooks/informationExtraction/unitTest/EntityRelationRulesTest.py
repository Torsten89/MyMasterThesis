from xml.dom.minidom import parse
import unittest
from informationExtraction.UnitExtractor import UnitExtractor
from informationExtraction.IngredientExtractor import IngredientExtractor
from informationExtraction.dictBasedExtractor import dictBasedEnrichment
from model.WordProperty import WordProperty
from informationExtraction.entityRelationRules import findQuantityAndUnitOfIngredientRule


class EntityRelationRulesTest(unittest.TestCase):
    """ These tests make only sense, when all DictBasedExtractorTests are passed. """
    
    def setUp(self):
        self.ingE = IngredientExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml"))
        self.unitE = UnitExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/cueML/cueML_v0.5.rng"))
        
    def testIngredient1(self):
        s = "Es wird hierzu für 24—30 Personen eine kräftige Bouillon von 8—10 Pfund Rindfleisch mit Wurzelwerk gekocht."
        wordProperties = dictBasedEnrichment(s, self.ingE, self.unitE)
        wordProperties = findQuantityAndUnitOfIngredientRule(wordProperties, None)
        
        self.assertIsNotNone(wordProperties[8].properties.get(WordProperty.INGREDIENT))
        self.assertIsNone(wordProperties[8].properties.get(WordProperty.UNIT))
        self.assertEqual("eine", wordProperties[8].properties.get(WordProperty.QUANTITY))
        
    def testIngredient2(self):
        s = "Es wird hierzu für 24—30 Personen eine kräftige Bouillon von 8—10 Pfund Rindfleisch mit Wurzelwerk gekocht."
        wordProperties = dictBasedEnrichment(s, self.ingE, self.unitE)
        wordProperties = findQuantityAndUnitOfIngredientRule(wordProperties, None)
        
        self.assertIsNotNone(wordProperties[12].properties.get(WordProperty.INGREDIENT))
        self.assertEqual("Rindfleisch", wordProperties[12].properties.get(WordProperty.INGREDIENT)[0].basicForm)
        self.assertEqual("8—10", wordProperties[12].properties.get(WordProperty.QUANTITY))
        self.assertEqual("Pfund", wordProperties[12].properties.get(WordProperty.UNIT))
    
    def testIngredient3(self):
        s = "Es wird hierzu für 24—30 Personen eine kräftige Bouillon von 8—10 Pfund Rindfleisch mit Wurzelwerk gekocht."
        wordProperties = dictBasedEnrichment(s, self.ingE, self.unitE)
        wordProperties = findQuantityAndUnitOfIngredientRule(wordProperties, None)
        
        self.assertIsNotNone(wordProperties[14].properties.get(WordProperty.INGREDIENT))
        self.assertIsNone(wordProperties[14].properties.get(WordProperty.UNIT))
        self.assertIsNone(wordProperties[14].properties.get(WordProperty.QUANTITY))


if __name__ == "__main__":
    unittest.main()