import unittest
from informationExtraction.QuantityExtractor import isQuantity, str2Quantity


class QuantityExtractorTest(unittest.TestCase):

    def testFraction(self):
        self.assertTrue(isQuantity("¾"))
    
    def testNoNumber(self):
        self.assertFalse(isQuantity("asdf"))
    
    def testSimpleNumber(self):
        self.assertTrue(isQuantity("9"))
        
    def testFloatNumber(self):
        self.assertTrue(isQuantity("0.3"))
        
    def testFromTo(self):
        self.assertTrue(isQuantity("1—2"))
    
    def testIngredientIsNoQuantity(self):
        self.assertFalse(isQuantity("Bouillon"))
        
    def testQuantity2String16(self):
        self.assertEqual("16", str2Quantity("16"))
        
    def testQuantity2String1AndHalf(self):
        self.assertEqual("1.5", str2Quantity("1½"))
        
    def testQuantity2StringFloat(self):
        self.assertEqual("2", str2Quantity("2"))
        
    def testQuantity2StringAHalf(self):
        self.assertEqual("0.5", str2Quantity("½"))

if __name__ == "__main__":
    unittest.main()