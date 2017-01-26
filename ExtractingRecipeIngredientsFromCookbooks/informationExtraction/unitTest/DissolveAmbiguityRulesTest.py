import unittest
from informationExtraction.IngredientExtractor import IngredientExtractor
from informationExtraction.UnitExtractor import UnitExtractor
from xml.dom.minidom import parse
from informationExtraction.dictBasedExtractor import dictBasedEnrichment
from model.WordProperty import WordProperty
from informationExtraction.dissolveAmbiguityRules import dissolveAmbiguity
from model.PlainTextRecipe import PlainTextRecipe

class DissolveAmbiguityRulesTest(unittest.TestCase):
    
    def setUp(self):
        self.ingE = IngredientExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml"))
        self.unitE = UnitExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/cueML/cueML_v0.5.rng"))

        
    def testWein(self):
        s="Zwei Eßlöffel voll Mehl werden mit einem Stich frischer Butter dunkelgelb geschwitzt,\
               mit Zungenbrühe abgerührt, dazu Rosinen, rother Wein, Zitronensaft und Schale,\
               Muskatblüthe, etwas Zucker und Salz."
               
        wordProperties = dictBasedEnrichment(s, self.ingE, self.unitE)    
        self.assertLess(1, len(wordProperties[21].properties.get(WordProperty.ingredient)), "DictBasedExtraction is already broken")
        dissolvedCandis = dissolveAmbiguity(21, wordProperties)[21].properties.get(WordProperty.ingredient)
        self.assertEqual(1, len(dissolvedCandis))
        self.assertEqual("Rotwein", dissolvedCandis[0].xmlID)
        
    def testFleisch(self):
        wordProperties = dictBasedEnrichment("Fleisch", self.ingE, self.unitE)
        rcp = PlainTextRecipe("", "Suppe", "Rindfleischsuppe", "")
        dissolvedCandis = dissolveAmbiguity(0, wordProperties, rcp)[0].properties.get(WordProperty.ingredient)
        self.assertEqual(1, len(dissolvedCandis))
        self.assertEqual("Rindkochfleisch", dissolvedCandis[0].xmlID)         


if __name__ == "__main__":
    unittest.main()