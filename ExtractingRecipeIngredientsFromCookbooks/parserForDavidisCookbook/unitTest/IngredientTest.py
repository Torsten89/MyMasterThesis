import unittest
from xml.dom.minidom import parseString
from parserForDavidisCookbook.Ingredient import Ingredient

class IngredientTest(unittest.TestCase):

    def testIngFromXmlIngElem(self):
        ing = Ingredient.ingFromXmlIngElem(parseString('<recipeIngredient ref="#SpargelGekocht" optional="True">Spargel</recipeIngredient>').childNodes[0])
        self.assertEqual(ing.ref, "#SpargelGekocht")
        with self.assertRaises(AttributeError):
            ing.target

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()