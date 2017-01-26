from parserForDavidisCookbook.XmlParser import XmlParser
from xml.dom.minidom import parse
from informationExtraction.IngredientExtractor import IngredientExtractor
from informationExtraction.UnitExtractor import UnitExtractor
from informationExtraction.dictAndRuleBasedExtractor import extract
from informationExtraction.QuantityExtractor import isQuantity
from evaluation.metrics import recall, precision
from parserForDavidisCookbook.Ingredient import Ingredient
import time

def ingsFromCueMLRetrieved(sentence, retrieved, ingsInCueML):
    """ returns (number of ings in cueML which got retrieved, number ings in cueML)
        and prints for each ingredient in cueML which got not retrieved some information.
    """
    numberIngsExtractedAndInCueML = 0
    numberIngsInCueML = len(ingsInCueML)
    for (ing, start, end) in ingsInCueML:
        correct = False
        for (posi, possibleIngRefs, quantity, unit) in retrieved:
            if posi in range(start, end+1):
                correct = True
                numberIngsExtractedAndInCueML += 1
                break
            
        if not correct:
            print(sentence)
            print("not retrieved:", ing, start, end)
            print("retrieved was:", retrieved)
            print()
    
    return (numberIngsExtractedAndInCueML, numberIngsInCueML)

def ingsRetrievedInCueML(sentence, retrieved, ingsInCueMLSentence, ingsInCueMLRecipe):
    numberRetievedAndInCuML = 0    
    numberRetrieved = len(retrieved)
    for (posi, possibleRefs, quantity, unit) in retrieved:
        correct = False
        for (ing, start, end) in ingsInCueMLSentence:
            if posi in range(start, end+1) or refOrTargetInIngsInCueMLRecipe(possibleRefs, ingsInCueMLRecipe):
                correct = True
                numberRetievedAndInCuML += 1
                break
        
        if not correct:
            print(sentence)
            print("retrieved was", (posi, possibleRefs, quantity, unit))
            print()

    return (numberRetievedAndInCuML, numberRetrieved)

def refOrTargetInIngsInCueMLRecipe(possibleRefs, ingsInCueMLRecipe):       
    if not possibleRefs:
        return False
    
    for (ing, start, end) in ingsInCueMLRecipe:
        if hasattr(ing, "ref") and ing.ref[1:] in possibleRefs:
            return True
        if hasattr(ing, "target") and ing.target[1:] in possibleRefs:
            return True
        
    return False
        
def getAllIngsInCueMLRecipe(recipe):
    return [ingInSentence for (sentence, ingsInSentence) in recipe.sentencesWithExtractedIngs for ingInSentence in ingsInSentence]

def extractRecipes(recipes, ingE, unitE, ):
    numberIngsExtractedAndInCueML = numberIngsInCueML = 0
    numberRetievedAndInCuML = numberRetrieved = 0
    
    for recipe in recipes:
        ingsInCueMLRecipe = getAllIngsInCueMLRecipe(recipe)
        plainTextSentences = [s.tokens for s in recipe.sentencesWithExtractedIngs]
        
        extracted = [] # [[ings of sentence]]
        for s in plainTextSentences:
            extracted.append(list(extract(s, ingE, unitE, isQuantity)))
                
        for i, s in enumerate(plainTextSentences):
            a, b = ingsFromCueMLRetrieved(s, extracted[i], recipe.sentencesWithExtractedIngs[i].ings)
            numberIngsExtractedAndInCueML += a
            numberIngsInCueML += b
             
            a, b = ingsRetrievedInCueML(s, extracted[i], recipe.sentencesWithExtractedIngs[i].ings, ingsInCueMLRecipe)
            numberRetievedAndInCuML += a
            numberRetrieved += b
                 
    print("Recall:", recall(numberIngsExtractedAndInCueML, numberIngsInCueML), "{}/{}".format(numberIngsExtractedAndInCueML, numberIngsInCueML))
    print("Precision:", precision(numberRetievedAndInCuML, numberRetrieved), "{}/{}".format(numberRetievedAndInCuML, numberRetrieved))    
            



if __name__ == '__main__':
    startTime = time.time()    
    
    cookbook = XmlParser(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/recipes extracted.xml"))
    ingE = IngredientExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml"))
    unitE = UnitExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/cueML/cueML_v0.5.rng"))  
        
    rcpIds = ["B-{}".format(i) for i in range(1,51)]
    recipes = cookbook.getRecipes(rcpIds)
    print("--- For reading Files: %s seconds ---" % (time.time() - startTime))  
    startTime = time.time()
    
    extractRecipes(recipes, ingE, unitE)
    
    print("--- For extracting and calculating metrics: %s seconds ---" % (time.time() - startTime))
        

