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
            if lemma[0].isupper():
                ingCandis = ingE.getIngredientCandidates(lemma)
                if ingCandis is None:
                    # Mrs. Davidis often uses an "n" in the plural form, which our lemmatisation / TreeTagger could not handle.
                    # E.g.: 2 Eidottern, 2 Saucissen, 2 Pfefferkörnern, ...
                    # Only trigger, when word is not an ingredient. Otherwise it would ruin words like 'Thimian' or 'Majoran'
                    if lemma[-1]=="n": ingCandis = ingE.getIngredientCandidates(lemma[:-1])
                if ingCandis is not None: properties[WordProperty.ingredient] = ingCandis
                
        result.append(WordProperty(word, lemma, properties))
    
    return result
            