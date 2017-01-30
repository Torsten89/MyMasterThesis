from parserForDavidisCookbook.XmlParser import XmlParser, getIngsFromNode
from xml.dom.minidom import parse, parseString
from informationExtraction.IngredientExtractor import IngredientExtractor
from informationExtraction.UnitExtractor import UnitExtractor
import time
from informationExtraction.Extractor import Extractor
from informationExtraction.dictBasedExtractor import dictBasedEnrichment
from informationExtraction.ruleBasedExtractor import applyRulesToWordProperties
from evaluation.evalRecipes import recallOf2Recipes, precisionOf2Recipes
from evaluation.metrics import recall, precision
from evaluation.comparator import ingInGoldenStandardIngsRoughMatch

ergFilePath = "erg.xml" 
   
if __name__ == '__main__':
    startTime = time.time()    
    cookbook = XmlParser(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/recipes extracted.xml"))
    ingE = IngredientExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml"))
    unitE = UnitExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/cueML/cueML_v0.5.rng")) 
     
    extractor = Extractor(ingE, unitE)
    rcpIds = ["B-{}".format(i) for i in range(1,51)] # IDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
    extractor.extractRecipesToXml(cookbook.getPlainTextRecipes(rcpIds), ergFilePath)
    
    print('--- Needed for extracting and writingTo "{}": {} seconds ---'.format(ergFilePath, time.time() - startTime))
    
    startTime = time.time()  
    iECookbook = XmlParser(parse(ergFilePath))
    attris = ("ref")
    for rcpId in rcpIds:
        goldenStandardRecipe = cookbook.getXmlRecipes([rcpId])[0]
        goldenStandardIngs = getIngsFromNode(goldenStandardRecipe)
        iERecipe = iECookbook.getXmlRecipes([rcpId])[0]
        iEIngs = getIngsFromNode(iERecipe)
        
        retrievedAndRelevantRecall, relevant = recallOf2Recipes(goldenStandardIngs, iEIngs, attris)
        print(recall(retrievedAndRelevantRecall, relevant), retrievedAndRelevantRecall, relevant)
        retrievedAndRelevantPrecision, retrieved = precisionOf2Recipes(goldenStandardIngs, iEIngs, attris)
        print(precision(retrievedAndRelevantPrecision, retrieved), retrievedAndRelevantPrecision, relevant)
        
        if retrievedAndRelevantRecall != relevant or retrievedAndRelevantPrecision!= retrieved:
            print(rcpId)
            print("Golden Standard:")
            for ing in goldenStandardIngs:
                print(ing)
            print("----")
            print("Retrieved:")
            for ing in iEIngs:
                print(ing)
            print("----")
            print()
        
    print('--- Needed for evaluating: {} seconds ---'.format(time.time() - startTime))    
    
    
    
    
    
    
    
    
    
# if __name__ == '__main__':
#     startTime = time.time()    
#      
#     cookbook = XmlParser(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/recipes extracted.xml"))
#     ingE = IngredientExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml"))
#     unitE = UnitExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/cueML/cueML_v0.5.rng")) 
#     extractor = Extractor(ingE, unitE)
#     s="Später kann man Spargel oder Blumenkohl, was die Jahreszeit hat, jedoch vorher eben abgekocht, und 10 Minuten vor dem Anrichten Fleisch- oder andere beliebige Klöße darin gahr kochen." 
#     
#     wps = dictBasedEnrichment(s, ingE, unitE)
#     for wp in wps:
#         print(wp.word, wp.lemma, wp.properties)
#     
#     print("-----")
#     improvedWps = applyRulesToWordProperties(wps, None)
#     for wp in improvedWps:
#         print(wp.word, wp.lemma, wp.properties)
#         
#     for wp in improvedWps:
#         print(wp.toXml())