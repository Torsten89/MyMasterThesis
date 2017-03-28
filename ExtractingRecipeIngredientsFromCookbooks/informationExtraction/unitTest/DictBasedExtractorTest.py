from xml.dom.minidom import parse
import unittest
from informationExtraction.QuantityExtractor import isQuantity
from informationExtraction.UnitExtractor import UnitExtractor
from informationExtraction.IngredientExtractor import IngredientExtractor
from informationExtraction.dictBasedExtractor import dictBasedEnrichment
from model.WordProperty import WordProperty
from unitTest.pathToFiles import pathToListIngredients


class DictBasedExtractorTest(unittest.TestCase):
    
    def setUp(self):
        self.ingE = IngredientExtractor(parse(pathToListIngredients))
        self.unitE = UnitExtractor()

    def testWP0(self):
        s = "Es wird hierzu für 24—30 Personen eine kräftige Bouillon von 8—10 Pfund Rindfleisch mit Wurzelwerk gekocht."
        wordProperties = dictBasedEnrichment(s, self.ingE, self.unitE)     
        self.assertIsNone(wordProperties[0].properties.get(WordProperty.INGREDIENT))
        self.assertIsNone(wordProperties[0].properties.get(WordProperty.UNIT))
        self.assertIsNone(wordProperties[0].properties.get(WordProperty.QUANTITY))

    def testQuantity1(self):
        s = "Es wird hierzu für 24—30 Personen eine kräftige Bouillon von 8—10 Pfund Rindfleisch mit Wurzelwerk gekocht."
        wordProperties = dictBasedEnrichment(s, self.ingE, self.unitE)
        self.assertEqual("24—30", wordProperties[4].properties.get(WordProperty.QUANTITY))
        
    def testQuantity2(self):
        s = "Es wird hierzu für 24—30 Personen eine kräftige Bouillon von 8—10 Pfund Rindfleisch mit Wurzelwerk gekocht."
        wordProperties = dictBasedEnrichment(s, self.ingE, self.unitE)
        self.assertEqual("8—10", wordProperties[10].properties.get(WordProperty.QUANTITY))
        
    def testIngredient1(self):
        s = "Es wird hierzu für 24—30 Personen eine kräftige Bouillon von 8—10 Pfund Rindfleisch mit Wurzelwerk gekocht."
        wordProperties = dictBasedEnrichment(s, self.ingE, self.unitE)
        self.assertIsNotNone(wordProperties[8].properties.get(WordProperty.INGREDIENT))
        self.assertEqual(0, len(wordProperties[8].properties.get(WordProperty.INGREDIENT)))
        
    def testIngredient2(self):
        s = "Es wird hierzu für 24—30 Personen eine kräftige Bouillon von 8—10 Pfund Rindfleisch mit Wurzelwerk gekocht."
        wordProperties = dictBasedEnrichment(s, self.ingE, self.unitE)
        self.assertIsNotNone(wordProperties[12].properties.get(WordProperty.INGREDIENT))
        self.assertIn("Rindkochfleisch", [candi.xmlID for candi in wordProperties[12].properties.get(WordProperty.INGREDIENT)])
    
    def testIngredient3(self):
        s = "Es wird hierzu für 24—30 Personen eine kräftige Bouillon von 8—10 Pfund Rindfleisch mit Wurzelwerk gekocht."
        wordProperties = dictBasedEnrichment(s, self.ingE, self.unitE)
        self.assertIsNotNone(wordProperties[14].properties.get(WordProperty.INGREDIENT))
        
    def testAbbrühen(self):
        s = "Das Fleisch abbrühen."
        wordProperties = dictBasedEnrichment(s, self.ingE, self.unitE)
        self.assertIsNone(wordProperties[2].properties.get(WordProperty.INGREDIENT))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()