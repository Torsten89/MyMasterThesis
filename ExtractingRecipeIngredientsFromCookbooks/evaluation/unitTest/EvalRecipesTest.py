import unittest
from xml.dom.minidom import parseString, parse
from parserForDavidisCookbook.XmlParser import parseXml2PlainTextRecipe,\
    XmlParser, getIngsFromNode
from informationExtraction.IngredientExtractor import IngredientExtractor
from informationExtraction.UnitExtractor import UnitExtractor
from informationExtraction.Extractor import Extractor
from evaluation.evalRecipes import recallOf2Recipes, precisionOf2Recipes
from evaluation.metrics import recall, precision


class EvalRecipesTest(unittest.TestCase):

    def testPrecisionOf2Recipes(self):
        b50 = '<cue:recipe type="Suppen." rcp-id="B-50" xmlns:cue="cueML"> \
<head>Suppe von echtem Sago mit Milch.</head> \
<p>Wird wie Suppe von feiner <cue:recipeIngredient ref="#Gerste" \
>Gerste</cue:recipeIngredient><ref target="B-49">(Nro. 49)</ref> gekocht.</p> \
</cue:recipe>'
#Milch sollte extrahiret werden -> ein "nicht relevantes extrahiert"

        ingE = IngredientExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml"))
        unitE = UnitExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/cueML/cueML_v0.5.rng")) 
        extractor = Extractor(ingE, unitE)
        
        attris = ("ref")
        goldenStandardIngs = getIngsFromNode(parseString(b50))
        iEIngs = getIngsFromNode(extractor.extractRecipe(parseXml2PlainTextRecipe(parseString(b50)))) # get recipe akutell ganzes document
        
        retrievedAndRelevantRecall, relevant = recallOf2Recipes(goldenStandardIngs, iEIngs, attris)
        print(recall(retrievedAndRelevantRecall, relevant), retrievedAndRelevantRecall, relevant)
        retrievedAndRelevantPrecision, retrieved = precisionOf2Recipes(goldenStandardIngs, iEIngs, attris)
        print(precision(retrievedAndRelevantPrecision, retrieved), retrievedAndRelevantPrecision, relevant)

        print("Golden Standard:")
        for ing in goldenStandardIngs:
            print(ing)
        print("----")
        print("Retrieved:")
        for ing in iEIngs:
            print(ing)
        print("----")
        print()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPrecisionOf2Recipes']
    unittest.main()