import unittest
from model.Ingredient import Ingredient
from parserForDavidisCookbook.cueML2Json import mergeIngs

class CueML2JsonTest(unittest.TestCase):

    def testMergeIngs2Blut(self):
        i1 = Ingredient({}, "Blut", (0,0))
        i2 = Ingredient({}, "Blut", (1,1))
        self.assertEqual(1, len(mergeIngs([i1, i2])))
        
    def testMergeIngsDif(self):
        i1 = Ingredient({}, "Schweinefleisch", (0,0))
        i2 = Ingredient({}, "Blut", (1,1))
        self.assertEqual(2, len(mergeIngs([i1, i2])))


if __name__ == "__main__":
    unittest.main()