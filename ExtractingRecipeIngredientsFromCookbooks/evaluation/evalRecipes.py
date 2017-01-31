from evaluation.comparator import ingInIngsExactMatch, ingInIngsRoughMatch
from parserForDavidisCookbook.XmlParser import XmlParser, getIngsFromNode
from xml.dom.minidom import parse
import time
from evaluation.metrics import recall, precision

def recallOf2Recipes(ingsOfGoldenStandardRcp, ingsOfIERcp, attris, debug=False):
    relevant = len(ingsOfGoldenStandardRcp)
    relevantAndRetrieved = 0
    
    for ing in ingsOfGoldenStandardRcp:
        if ingInIngsExactMatch(ing, ingsOfIERcp, attris):
            relevantAndRetrieved += 1
        elif debug:
            print("Not retrieved: {}".format(ing))
            
    return relevantAndRetrieved, relevant

def precisionOf2Recipes(ingsOfGoldenStandardRcp, retrievedIngs, attris, debug=False):
    retrieved = len(retrievedIngs)
    retrievedAndRelevant = 0
    
    for ing in retrievedIngs:
        if ingInIngsRoughMatch(ing, ingsOfGoldenStandardRcp, retrievedIngs, attris):
            retrievedAndRelevant += 1
        elif debug:
            print("Not relevant but retrieved: {}".format(ing))
            
    return retrievedAndRelevant, retrieved

def evalFromFiles(pathToGoldenStandardRcps, pathToIERcps, attris, rcpIds=[], debug=False):
    goldenStandardRcps = XmlParser(parse(pathToGoldenStandardRcps))
    iERcps = XmlParser(parse(pathToIERcps))

    relevant, retrieved, relevantAndRetrieved, retrievedAndRelevant = 0, 0, 0, 0
    for rcpId in rcpIds:
        somethingWrong = False
        
        goldenStandardRecipe = goldenStandardRcps.getXmlRecipes([rcpId])[0]
        goldenStandardIngs = getIngsFromNode(goldenStandardRecipe)
        
        iERecipe = iERcps.getXmlRecipes([rcpId])[0]
        iEIngs = getIngsFromNode(iERecipe)
        
        a,b = recallOf2Recipes(goldenStandardIngs, iEIngs, attris, debug)
        if debug and a!=b:
            somethingWrong = True
        relevantAndRetrieved += a
        relevant += b

        a,b = precisionOf2Recipes(goldenStandardIngs, iEIngs, attris, debug)
        if debug and a!=b:
            somethingWrong = True
        retrievedAndRelevant += a
        retrieved += b
        
        if debug and somethingWrong:
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
            
    print("Recall: {}, {}, {}".format(recall(relevantAndRetrieved, relevant), relevantAndRetrieved, relevant)) 
    print("Precision: {}, {}, {}".format(precision(retrievedAndRelevant, retrieved), retrievedAndRelevant, retrieved))
            
if __name__ == '__main__':
    startTime = time.time()    
    
    evalFromFiles("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/recipes extracted.xml",
                  "../erg.xml",
                  rcpIds=["B-{}".format(i) for i in range(1,51)], attris=("ref"), debug=True)
    
    print('--- Needed for evaluating: {} seconds ---'.format(time.time() - startTime)) 
           
            
            
            
            
    