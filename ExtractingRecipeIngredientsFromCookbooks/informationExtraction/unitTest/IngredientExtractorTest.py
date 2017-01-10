from xml.dom.minidom import parse
import unittest
from informationExtraction.IngredientExtractor import IngredientExtractor


class IngredientExtractorTest(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        dom = parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml")
        self.ingE = IngredientExtractor(dom)

    def testWein(self):
        self.assertLess(1, len(self.ingE.getIngredientCandidates("Wein")))
        
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