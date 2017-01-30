import unittest
from model.WordProperty import WordProperty

class WordPropertyTest(unittest.TestCase):

    def testIngWithNoRefToHtml(self):
        wp = WordProperty("Klöße", "Kloß", {WordProperty.ingredient:[]})
        self.assertEqual("<recipeIngredient >Klöße</recipeIngredient>", wp.toXml(""))


if __name__ == "__main__":
    unittest.main()