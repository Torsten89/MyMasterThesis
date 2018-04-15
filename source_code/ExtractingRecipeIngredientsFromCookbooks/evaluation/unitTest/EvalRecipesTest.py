import unittest
from xml.dom.minidom import parseString, parse
from parserForDavidisCookbook.XmlParser import parseXml2PlainTextRecipe,\
    XmlParser, getIngsFromNode
from informationExtraction.IngredientExtractor import IngredientExtractor
from informationExtraction.UnitExtractor import UnitExtractor
from informationExtraction.Extractor import Extractor
from evaluation.evalRecipes import recallOf2Recipes, precisionOf2Recipes
from evaluation.metrics import recall, precision
from unitTest.pathToFiles import pathToListIngredients


class EvalRecipesTest(unittest.TestCase):
    ingE = IngredientExtractor(parse(pathToListIngredients))
    unitE = UnitExtractor() 
    extractor = Extractor(ingE, unitE)

    def testPrecisionOf2Recipes(self):
        iEIngs, goldenStandardIngs = getIEIngsAndGoldenStandardIngs()
        attris = set(("ref",))
        retrievedAndRelevant, relevant = recallOf2Recipes(goldenStandardIngs, iEIngs, attris)
        self.assertEqual(1, retrievedAndRelevant)
        self.assertEqual(1, relevant)

    def testRecallOf2Recipes(self):
        iEIngs, goldenStandardIngs = getIEIngsAndGoldenStandardIngs()
        attris = set(("ref",))
        retrievedAndRelevant, retrieved = precisionOf2Recipes(goldenStandardIngs, iEIngs, attris)
        self.assertEqual(1, retrievedAndRelevant)
        self.assertEqual(3, retrieved)

iEIngs = None
goldenStandardIngs = None
def getIEIngsAndGoldenStandardIngs():
    global iEIngs, goldenStandardIngs
    if iEIngs:
        return iEIngs, goldenStandardIngs
    
    b50 = getB50XMLRecipe()
    goldenStandardIngs = getIngsFromNode(b50)
    extractedXMLString = EvalRecipesTest.extractor.extractRecipe(parseXml2PlainTextRecipe(b50))                                          
    iEIngs = getIngsFromNode(parseString(extractedXMLString).getElementsByTagName("cue:recipe")[0])
    return getIEIngsAndGoldenStandardIngs()
    
def getB50XMLRecipe():
    return parseString('<cue:recipe type="Suppen." rcp-id="B-50" xmlns:cue="cueML" xml:id="b50"> \
<head>Suppe von echtem Sago mit Milch.</head> \
<p>Wird wie Suppe von feiner <cue:recipeIngredient ref="#Gerste" \
>Gerste</cue:recipeIngredient><ref target="B-49">(Nro. 49)</ref> gekocht.</p> \
</cue:recipe>').getElementsByTagName("cue:recipe")[0]


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPrecisionOf2Recipes']
    unittest.main()