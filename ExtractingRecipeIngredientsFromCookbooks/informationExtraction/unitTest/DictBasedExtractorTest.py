from xml.dom.minidom import parse
import unittest
from informationExtraction.IngredientExtractor import IngredientExtractor
from informationExtraction.dictBasedExtractor import extract
from informationExtraction.QuantityExtractor import isQuantity
from informationExtraction.UnitExtractor import UnitExtractor


class DictBasedExtractorTest(unittest.TestCase):
    
    def setUp(self):
        self.ingE = IngredientExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml"))
        self.unitE = UnitExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/cueML/cueML_v0.5.rng"))


    def testSentence1(self):
        s = "Es wird hierzu für 24—30 Personen eine kräftige Bouillon von 8—10 Pfund Rindfleisch mit Wurzelwerk gekocht."
        ingredients = list(extract(s, self.ingE, self.unitE, isQuantity))
        self.assertEqual(3, len(ingredients))
        self.assertEqual((8, set(), "eine", None), ingredients[0])
        self.assertEqual((12, {"Rindkochfleisch"}, "8—10", "Pfund"), ingredients[1])
        self.assertEqual((14, {"Wurzelwerk"}, None, None), ingredients[2])
        
    def testShortening(self):
        s = 'Eine Stunde später gießt man die Brühe durch ein Haarsieb, weil sie nie \
             ganz klar ist, spült das Stück Fleisch eben ab und setzt es mit der Brühe, die man \
             vom Bodensatz langsam abschüttet, in dem ebenfalls umgespülten Topfe wieder zu Feuer \
             nebst einigen Scorzoner-, einer Sellerie- und Petersilienwurzel.'
        ingredients = list(extract(s, self.ingE, self.unitE, isQuantity))
        self.assertEqual(6, len(ingredients))
        self.assertEqual((51, {"Knollensellerie"}, "eine", None), ingredients[4])
        
    def testDissolveRotWein(self):
        xmlId = "Rotwein"
        sentence="Zwei Eßlöffel voll Mehl werden mit einem Stich frischer Butter dunkelgelb geschwitzt,\
               mit Zungenbrühe abgerührt, dazu Rosinen, rother Wein, Zitronensaft und Schale,\
               Muskatblüthe, etwas Zucker und Salz."
        candis = self.ingE.getIngredientCandidates("Wein", recipe=None, sentence=sentence)

        self.assertEqual(1, len(candis))
        self.assertTrue(xmlId in candis)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()