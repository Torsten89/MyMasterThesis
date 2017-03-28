from xml.dom.minidom import parse
import unittest
from informationExtraction.IngredientExtractor import IngredientExtractor
from unitTest.pathToFiles import pathToListIngredients


class IngredientExtractorTest(unittest.TestCase):
    """Caution: These tests depend on the listIngredients.xml within setUp()"""
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        dom = parse(pathToListIngredients)
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
        
    def testFleisch(self):
        candis = self.ingE.getIngredientCandidates("Fleisch")
        self.assertLess(1, len(candis))
        self.assertIn("Rindfleisch", [candi.basicForm for candi in candis])
        

    def testSchweinefleisch(self):
        candis = self.ingE.getIngredientCandidates("Schweinefleisch")
        self.assertEqual([], candis)


        
        
if __name__ == "__main__":
    unittest.main()