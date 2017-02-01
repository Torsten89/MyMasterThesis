from parserForDavidisCookbook.XmlParser import XmlParser
from xml.dom.minidom import parse
from informationExtraction.IngredientExtractor import IngredientExtractor
from informationExtraction.UnitExtractor import UnitExtractor
import time
from informationExtraction.Extractor import Extractor
from evaluation.evalRecipes import evalFromFiles


debug = True
ergFilePath = "erg.xml"
goldenStandardPath = "/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/recipes extracted.xml"
rcpIds = ["B-{}".format(i) for i in range(1, 51)]
attris=("ref")
ingE = IngredientExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml"))
unitE = UnitExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/cueML/cueML_v0.5.rng"))    
if __name__ == '__main__':
    startTime = time.time()    
    cookbook = XmlParser(parse(goldenStandardPath))
    extractor = Extractor(ingE, unitE)
    extractor.extractRecipes2TEICueML(cookbook.getPlainTextRecipes(rcpIds), ergFilePath)
    print('--- Needed for extracting and writingTo "{}": {} seconds ---'.format(ergFilePath, time.time() - startTime))
    
    startTime = time.time()  
    evalFromFiles(goldenStandardPath, ergFilePath, attris=attris, rcpIds=rcpIds, debug=True)  
    print('--- Needed for evaluating: {} seconds ---'.format(time.time() - startTime)) 

    
    