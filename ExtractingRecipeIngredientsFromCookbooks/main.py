from parserForDavidisCookbook.XmlParser import XmlParser
from xml.dom.minidom import parse
from informationExtraction.IngredientExtractor import IngredientExtractor
from informationExtraction.UnitExtractor import UnitExtractor
import time
from informationExtraction.Extractor import Extractor
from evaluation.evalRecipes import evalFromFiles
from model.PlainTextRecipe import PlainTextRecipe
from informationExtraction.dictBasedExtractor import dictBasedEnrichment
from informationExtraction.ruleBasedExtractor import applyRulesToWordProperties

evalAttris=set(["quantity", "atLeast", "atMost", "unit"]) #["quantity", "atLeast", "atMost", "unit", "optional", "altGrp"]) #attris which should be relevant in evaluation
ingE = IngredientExtractor(parse("/home/torsten/Desktop/MyMasterThesis/docs/DavidisesKochbuch/listIngredients.xml"))
unitE = UnitExtractor()    
goldenStandardPath = "/home/torsten/Desktop/MyMasterThesis/docs/DavidisesKochbuch/GoldenStandard.xml" # contains B-1 to B-68 labeled and the rest unlabeled
defaultErgFilePath = "erg.xml"

def evalRecipes(rcpIds=["B-{}".format(i) for i in range(1, 51)], debug=True, attris=evalAttris, ergFilePath=defaultErgFilePath):    
    startTime = time.time()    
    cookbook = XmlParser(parse(goldenStandardPath))
    extractor = Extractor(ingE, unitE)
    extractor.extractRecipes2TEICueML(cookbook.getPlainTextRecipes(rcpIds), ergFilePath)
    print('--- Needed for extracting and writingTo "{}": {} seconds ---'.format(ergFilePath, time.time() - startTime))
       
    startTime = time.time()  
    evalFromFiles(goldenStandardPath, ergFilePath, attris=attris, rcpIds=rcpIds, debug=True)  
    print('--- Needed for evaluating: {} seconds ---'.format(time.time() - startTime))    

def myPlaygroundTest():
    """Just a random test function for me"""
    rcp = PlainTextRecipe("B-16", "Suppen", "Mock Turtle Suppe", ["Sowohl die Bouillon als \
Kalbskopf können schon am vorhergehenden Tage, ohne Nachtheil der Suppe, gekocht werden."])
    extractor = Extractor(ingE, unitE)
    print(extractor.extractRecipe(rcp))

    s = "Schweinemagen"
    print(ingE.__ingDict__["Schweinemagen"])
    wps = dictBasedEnrichment(s, ingE, unitE)
    wps = applyRulesToWordProperties(wps, None)
    for wp in wps:
        print(wp)
        
def extractAllRecipes(pathToCookbook, ergFilePath=defaultErgFilePath):
    extractor = Extractor(ingE, unitE)
    cookbook = XmlParser(parse(pathToCookbook))
    extractor.extractRecipes2TEICueML(cookbook.getPlainTextRecipes(), ergFilePath)
    

if __name__ == '__main__':
#     myPlaygroundTest()
#     evalRecipes()
    extractAllRecipes("/home/torsten/Desktop/MyMasterThesis/docs/DavidisesKochbuch/recipes extracted (original).xml", 
                     ergFilePath="/home/torsten/Desktop/MyMasterThesis/docs/DavidisesKochbuch/Rezepte automatisch mit cueML ausgezeichnet.xml")
     
    