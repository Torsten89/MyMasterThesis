'''
Created on Jan 9, 2017

@author: torsten
'''

from informationExtraction.IngredientExtractor import IngredientExtractor
from informationExtraction.UnitExtractor import UnitExtractor
from informationExtraction.QuantityExtractor import QuantityExtractor
from informationExtraction.lemmatization import getWordLemmaTuples
from xml.dom.minidom import parse

def extract(sentence, ingE, unitE, quantE):
    result=[]
    enrichedSentence = [WordProperties(lemma, ingE, unitE, quantE) for (_, lemma) in getWordLemmaTuples(sentence)]
    for i, wp in enumerate(enrichedSentence):
        if wp.ingCandis is not None:
            print(wp.lemma, wp.ingCandis, findQuantity(i, enrichedSentence), findUnit(i, enrichedSentence))
            result.append(i, wp.ingCandis, findQuantity(i, enrichedSentence), findUnit(i, enrichedSentence))
            
    return result

def findQuantity(i, enrichedSentence):
    for wp in enrichedSentence[i-1::-1]:
        if wp.isQuantity:
            return wp.lemma
        if otherEntity(wp):
            return None
    
def findUnit(i, enrichedSentence):
    for wp in enrichedSentence[i-1::-1]:
        if wp.unit:
            return wp.unit
        if otherEntity(wp):
            return None
        
def otherEntity(wordProperty):
    otherEntites = ["Person", "Stunde"]
    if wordProperty.lemma in otherEntites:
        return True
    
    if wordProperty.ingCandis:
        return True
    
    return False


class WordProperties(object):

    def __init__(self, lemma, ingredientExtractor, unitExtractor, quantityExtractor):
        self.lemma = lemma
        self.ingCandis = self.unit = self.isQuantity = None
        
        self.ingCandis = ingredientExtractor.getIngredientCandidates(lemma)
        if self.ingCandis is not None: return
        
        self.unit = unitExtractor.getUnit(lemma, False)
        if self.unit: return
        
        self.isQuantity = quantityExtractor.isQuantity(lemma)
        
    def __str__(self):
        entries = []
        for prop, value in self.__dict__.items():
            if value:
                entries.append("{}={}".format(prop, value))
                
        return ", ".join(entries)


if __name__ == '__main__':
    ingE = IngredientExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml"), None)
    unitE = UnitExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/cueML/cueML_v0.5.rng"))
    quanE = QuantityExtractor()
    
    s1 = "Es wird hierzu für 24—30 Personen eine kräftige Bouillon von 8—10 Pfund Rindfleisch mit Wurzelwerk gekocht."
    s2 = 'Eine Stunde später gießt man die Brühe durch ein Haarsieb, weil sie nie \
            ganz klar ist, spült das Stück Fleisch eben ab und setzt es mit der Brühe, die man \
            vom Bodensatz langsam abschüttet, in dem ebenfalls umgespülten Topfe wieder zu Feuer \
            nebst einigen Scorzoner-, einer Sellerie- und Petersilienwurzel.'
    
    extract(s1, ingE, unitE, quanE)
        