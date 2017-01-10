'''
Created on Jan 9, 2017

@author: torsten
'''

from informationExtraction.IngredientExtractor import IngredientExtractor
from informationExtraction.UnitExtractor import UnitExtractor
from informationExtraction.lemmatization import getWordLemmaTuples
from xml.dom.minidom import parse
from informationExtraction.QuantityExtractor import isQuantity

def extract(sentence, ingE, unitE, quantE):
    """ yields for each ingredient in the sentence a tuple (position in sentence, [possible xml:ids of ingredient], quantity, unit). """
    enrichedSentence = [WordProperties(lemma, ingE, unitE, quantE) for (_, lemma) in getWordLemmaTuples(sentence)]
    for i, wp in enumerate(enrichedSentence):
        if wp.ingCandis is not None:
            yield (i, wp.ingCandis, __findQuantity__(i, enrichedSentence), __findUnit__(i, enrichedSentence))

def __findQuantity__(i, enrichedSentence):
    for wp in enrichedSentence[i-1::-1]:
        if wp.isQuantity:
            return wp.lemma
        if __otherEntity__(wp):
            return None
    
def __findUnit__(i, enrichedSentence):
    for wp in enrichedSentence[i-1::-1]:
        if wp.unit:
            return wp.unit
        if __otherEntity__(wp):
            return None
        
def __otherEntity__(wordProperty):
    otherEntites = ["Person", "Stunde"]
    if wordProperty.lemma in otherEntites:
        return True
    
    if wordProperty.ingCandis:
        return True
    
    return False


class WordProperties(object):
    """ When self.lemma is an ingredient, self.ingCandis is a list of possible xml:ids, which define the ingredient, otherwise it is None.
    
        When self.lemma is an unit, self.unit is its unit value, otherwise it is None.
        
        When self.lemma is a quantity, it can be something like "1-2" and has to be processed further.
        
        A word can either be an ingredient, an unit, a quantity or none of them, but never be two of them at the same time.
    """

    def __init__(self, lemma, ingredientExtractor, unitExtractor, isQuantityFunc):
        self.lemma = lemma
        self.ingCandis = self.unit = self.isQuantity = None
        
        self.ingCandis = ingredientExtractor.getIngredientCandidates(lemma)
        if self.ingCandis is not None: return
        
        self.unit = unitExtractor.getUnit(lemma)
        if self.unit: return
        
        self.isQuantity = isQuantityFunc(lemma)
        
    def __str__(self):
        entries = []
        for prop, value in self.__dict__.items():
            if value:
                entries.append("{}={}".format(prop, value))
                
        return ", ".join(entries)


if __name__ == '__main__':
    ingE = IngredientExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml"), None)
    unitE = UnitExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/cueML/cueML_v0.5.rng"))
    
    s1 = "Es wird hierzu für 24—30 Personen eine kräftige Bouillon von 8—10 Pfund Rindfleisch mit Wurzelwerk gekocht."
    s2 = 'Eine Stunde später gießt man die Brühe durch ein Haarsieb, weil sie nie \
            ganz klar ist, spült das Stück Fleisch eben ab und setzt es mit der Brühe, die man \
            vom Bodensatz langsam abschüttet, in dem ebenfalls umgespülten Topfe wieder zu Feuer \
            nebst einigen Scorzoner-, einer Sellerie- und Petersilienwurzel.'
    
    extract(s1, ingE, unitE, isQuantity)
        