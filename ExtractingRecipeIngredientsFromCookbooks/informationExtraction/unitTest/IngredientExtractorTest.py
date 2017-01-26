from xml.dom.minidom import parse
import unittest
from informationExtraction.IngredientExtractor import IngredientExtractor


class IngredientExtractorTest(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        dom = parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml")
        self.ingE = IngredientExtractor(dom)
        
    def testWein(self):
        candis = self.ingE.getIngredientCandidates("Wein")
        self.assertLess(1, len(candis))
        self.assertTrue("Rotwein" in [candi.xmlID for candi in candis])

    def testMidder(self):
        candis = self.ingE.getIngredientCandidates("Midder")
        self.assertEqual(1, len(candis))
        self.assertEqual("Midder", candis[0].basicForm)
        self.assertEqual("Midder", candis[0].xmlID)
        
    def testNoIngredient(self):    
        candis = self.ingE.getIngredientCandidates("asfd")
        self.assertIsNone(candis)
        
    def testBouillon(self):
        candis = self.ingE.getIngredientCandidates("Bouillon")
        self.assertIsNotNone(candis)
        self.assertEqual(0, len(candis))
        
        
if __name__ == "__main__":
    unittest.main()