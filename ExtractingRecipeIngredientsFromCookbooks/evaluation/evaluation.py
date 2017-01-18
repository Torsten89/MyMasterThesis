from parserForDavidisCookbook.XmlParser import XmlParser
from xml.dom.minidom import parse
from informationExtraction.IngredientExtractor import IngredientExtractor
from informationExtraction.UnitExtractor import UnitExtractor
from informationExtraction.dictAndRuleBasedExtractor import extract
from informationExtraction.QuantityExtractor import isQuantity

def ingsCorrectExtracter(sentence, extracted, ingsWithPositionInSentence):
    for (ing, start, end) in ingsWithPositionInSentence:
        correct = False
        for (posi, possibleIngRefs, quantity, unit) in extracted:
            if posi in range(start, end+1):
                correct = True
                break
            
        if not correct:
            #continue
            print(sentence)
            print("not extracted:", ing, start, end)
            print("extracted was:", extracted)
            print()
        
if __name__ == '__main__':
    recipeB16 = list(XmlParser(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/recipesExtracted.xml")).getRecipes(["B-16"]))[0]
    plainTextSentences = [s.tokens for s in recipeB16.sentencesWithExtractedIngs]
    
    ingE = IngredientExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml"))
    unitE = UnitExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/cueML/cueML_v0.5.rng"))
     
    extracted = [] # [[ings of sentence]]
    for s in plainTextSentences:
        extracted.append(list(extract(s, ingE, unitE, isQuantity)))
         
     
    for i, s in enumerate(plainTextSentences):
        ingsCorrectExtracter(s, extracted[i], recipeB16.sentencesWithExtractedIngs[i].ings)
        print("------------")
#         print(s)
#         print(recipeB16.sentencesWithExtractedIngs[i].ings)
#         print(extracted[i])
#         print()
