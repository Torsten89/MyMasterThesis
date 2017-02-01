import unittest
from evaluation.comparator import isBetween, ingInIngsExactMatch,\
    ingInIngsRoughMatch, compare
from model.Ingredient import Ingredient


class ComparatorTest(unittest.TestCase):

    def testIsBetween1(self):
        self.assertTrue(isBetween((0,0), (0,0)))
         
    def testIsBetween2(self):
        self.assertTrue(isBetween((0,2), (1,3)))
         
    def testIsBetween3(self):
        self.assertTrue(isBetween((1,2), (0,1)))
         
    def testIsBetween4(self):
        self.assertFalse(isBetween((0,2), (3,3)))
     
    def testIsBetween5(self):
        self.assertFalse(isBetween((4,6), (3,3)))
        
    def testCompare1(self):
        i1 = Ingredient({"ref":"#Knollenselerie", "quantity":"1"}, ['Sellerieknolle'], (0,0))
        i2 = Ingredient({"ref":"#Knollenselerie", "quantity":"8"}, ['Sellerieknolle'], (0,0))
        self.assertTrue(compare(i1, i2, attris=("ref")))
        
    def testCompare2(self):
        i1 = Ingredient({"ref":"#Knollenselerie", "quantity":"1"}, ['Sellerieknolle'], (0,0))
        i2 = Ingredient({"ref":"#Knollenselerie", "quantity":"8"}, ['Sellerieknolle'], (0,0))
        self.assertFalse(compare(i1, i2, attris=("ref", "quantity")))
         
    def testIngInIngsExactMatch1(self):
        ing = Ingredient({"ref":"#Mehl"}, ["Mehl"], (3,3))
        self.assertTrue(ingInIngsExactMatch(ing, getIngs(), ("ref",)))
         
    def testIngInIngsExactMatch2(self):
        ing = Ingredient({"ref":"#Mehl"}, ["Mehl"], (4,4))
        self.assertFalse(ingInIngsExactMatch(ing, getIngs(), ("ref",)))
       
    def testIngInIngsExactMatch3(self):
        ing = Ingredient({"ref":"#Mehl", "quantity":"2"}, ["Mehl"], (3,3))
        self.assertTrue(ingInIngsExactMatch(ing, getIngs(), ("ref",)))
           
    def testIngInIngsExactMatch4(self):
        ing = Ingredient({"ref":"#Mehl", "quantity":"2"}, ["Mehl"], (3,3))
        self.assertFalse(ingInIngsExactMatch(ing, getIngs(), ("ref", "quantity")))
         
    def testIngInIngsRoughMatch1(self):
        ing = Ingredient({"ref":"#Zucker", "quantity":"1", "unit":"EL"}, ["Zucker"], (0,0))
        self.assertTrue(ingInIngsRoughMatch(ing, getIngs(), getIngs(), ("ref", "quantity", "unit")))
         
    def testIngInIngsRoughMatch2(self):
        ing = Ingredient({"ref":"#Zucker"}, ["Zucker"], (0,0))
        self.assertTrue(ingInIngsRoughMatch(ing, getIngs(), getIngs(), ("ref", "quantity", "unit")))
         
    def testIngInIngsRoughMatch3(self):
        ing = Ingredient({"ref":"#Zucker"}, ["Zucker"], (0,0))
        ingsExtracted = [ing]
        self.assertFalse(ingInIngsRoughMatch(ing, getIngs(), ingsExtracted, ("ref", "quantity", "unit")))
         
    def testIngInIngsRoughMatch4(self):
        ing = Ingredient({"ref":"#Kalsbrühe"}, ["Kalbsbrühe"], (0,0))
        self.assertTrue(ingInIngsRoughMatch(ing, getIngs(), getIngs(), ("ref", "quantity", "unit")))
         
    def testIngInIngsRoughMatch5(self):
        ing = Ingredient({"ref":"#asf"}, ["Biokleidung"], (0,0))
        self.assertFalse(ingInIngsRoughMatch(ing, getIngs(), getIngs(), ("ref", "quantity", "unit")))
        
    def testIngInIngsRoughMatch6(self):
        ing = Ingredient({"ref":"#Knollensellerie #Sellerieblätter"}, ["Sellerie"], (17,17))
        goldenStandardIngs = [Ingredient({"ref":"#Knollensellerie"}, ["Knollensellerie"], (0,0))]
        self.assertTrue(ingInIngsRoughMatch(ing, goldenStandardIngs, [ing]+goldenStandardIngs, ("ref")))
        
        
def getIngs():
    i1 = Ingredient({"ref":"#Mehl"}, ["Mehl"], (3,3))
    i2 = Ingredient({"ref":"#Zucker", "quantity":"1", "unit":"EL"}, ["Zucker"], (0,0))
    i3 = Ingredient({"ref":"#Weißwein"}, ["weißer", "Wein"], (6,7))
    return [i1, i2, i3]

if __name__ == "__main__":
    unittest.main()