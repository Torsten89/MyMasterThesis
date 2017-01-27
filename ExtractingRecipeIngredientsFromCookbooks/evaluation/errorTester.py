from parserForDavidisCookbook.XmlParser import XmlParser
from xml.dom.minidom import parse, parseString
from informationExtraction.IngredientExtractor import IngredientExtractor
from informationExtraction.UnitExtractor import UnitExtractor
import time
from informationExtraction.Extractor import Extractor
from informationExtraction.dictBasedExtractor import dictBasedEnrichment
from informationExtraction.ruleBasedExtractor import applyRulesToWordProperties

   
if __name__ == '__main__':
    startTime = time.time()    
     
    cookbook = XmlParser(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/recipes extracted.xml"))
    ingE = IngredientExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml"))
    unitE = UnitExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/cueML/cueML_v0.5.rng")) 
    extractor = Extractor(ingE, unitE)
    s="Später kann man Spargel oder Blumenkohl, was die Jahreszeit hat, jedoch vorher eben abgekocht, und 10 Minuten vor dem Anrichten Fleisch- oder andere beliebige Klöße darin gahr kochen." 
    
    wps = dictBasedEnrichment(s, ingE, unitE)
    for wp in wps:
        print(wp.word, wp.lemma, wp.properties)
    
    print("-----")
    improvedWps = applyRulesToWordProperties(wps, None)
    for wp in improvedWps:
        print(wp.word, wp.lemma, wp.properties)
        
    for wp in improvedWps:
        print(wp.toXml())




