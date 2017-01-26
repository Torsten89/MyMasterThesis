from model.WordProperty import WordProperty
from informationExtraction.QuantityExtractor import isQuantity
from informationExtraction.parseHelper import getWordLemmaTuples

def dictBasedEnrichment(text, ingE, unitE):
    """ Returns a list containing a WordProperty for each word of the given string """
    result = []
    wordLemmaTuples = getWordLemmaTuples(text)
    for (word, lemma) in wordLemmaTuples:
        properties = {}
        if isQuantity(lemma):
            properties[WordProperty.quantity] = lemma
        elif unitE.getUnit(lemma):
            properties[WordProperty.unit] = lemma
        else:
            ingCandis = ingE.getIngredientCandidates(lemma)
            if ingCandis is not None:
                properties[WordProperty.ingredient] = ingCandis
                properties[WordProperty.quantity] = findQuantity(reversed(result))
                properties[WordProperty.unit] = findUnit(reversed(result))
                
        result.append(WordProperty(word, lemma, properties))
    
    return result

def findQuantity(wordProperties):
    for wp in wordProperties:
        if otherEntity(wp):
            return None
        if wp.properties.get(WordProperty.quantity):
            return wp.lemma
    
def findUnit(wordProperties):
    for wp in wordProperties:
        unit = wp.properties.get(WordProperty.unit)
        if otherEntity(wp):
            return None
        if unit:
            return unit
        
otherEntites = ["Person", "Stunde"]
def otherEntity(wordProperty):
    if wordProperty.lemma in otherEntites:
        return True
    
    if wordProperty.properties.get(WordProperty.ingredient):
        return True
    
    return False

            
            