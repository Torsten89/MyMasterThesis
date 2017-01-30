from model.WordProperty import WordProperty
from informationExtraction.QuantityExtractor import isQuantity
from informationExtraction.textualHelper import getWordLemmaTuples

def dictBasedEnrichment(text, ingE, unitE):
    """ Returns a list containing a WordProperty for each word of the given string """
    result = []
    for (word, lemma) in getWordLemmaTuples(text):
        properties = {}
        if isQuantity(lemma):
            properties[WordProperty.quantity] = lemma
        elif unitE.getUnit(lemma):
            properties[WordProperty.unit] = lemma
        else:
            ingCandis = ingE.getIngredientCandidates(lemma)
            if ingCandis is not None: properties[WordProperty.ingredient] = ingCandis
                
        result.append(WordProperty(word, lemma, properties))
    
    return result
            