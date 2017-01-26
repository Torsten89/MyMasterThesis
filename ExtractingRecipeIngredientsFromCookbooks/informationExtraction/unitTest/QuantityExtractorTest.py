'''
Created on Jan 26, 2017

@author: torsten
'''
import unittest
from informationExtraction.QuantityExtractor import isQuantity


class Test(unittest.TestCase):

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


if __name__ == "__main__":
    unittest.main()