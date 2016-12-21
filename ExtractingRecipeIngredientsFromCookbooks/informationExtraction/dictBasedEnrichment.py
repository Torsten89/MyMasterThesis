from informationExtraction.lemmatization import getLemmas
from xml.dom.minidom import parse
from informationExtraction.IngredientExtractor import IngredientExtractor
from informationExtraction.UnitExtractor import UnitExtractor
from informationExtraction.QuantityExtractor import QuantityExtractor

def enrichSentence(sentence, ingE, unitE, quantE):
    return [WordProperties(word, lemma, ingE, unitE, quantE) for (word, lemma) in getLemmas(sentence)]
    

class WordProperties(object):

    def __init__(self, word, lemma, ingredientExtractor, unitExtractor, quantityExtractor):
        self.word = word
        self.lemma = lemma
        
        self.ingredientInfos = ingredientExtractor.getInformation(lemma, False)
        if self.ingredientInfos: return
        self.isUnit = unitExtractor.getInformation(lemma, False)
        if self.isUnit: return
        self.quantitiyInfos = quantityExtractor.getInformation(lemma)
        
    def __str__(self):
        entries = []
        for prop, value in self.__dict__.items():
            if value:
                entries.append("{}={}".format(prop, value))
                
        return ", ".join(entries)
        
    
if __name__ == "__main__":
    ingE = IngredientExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml"), None)
    unitE = UnitExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/cueML/cueML_v0.5.rng"))
    quanE = QuantityExtractor()
#     for k, v in ingD.__ingDict__.items():
#         print(k, v)
    
    s1 = "Es wird hierzu für 24—30 Personen eine kräftige Bouillon von 8—10 Pfund Rindfleisch mit Wurzelwerk gekocht."
    s2 = 'Eine Stunde später gießt man die Brühe durch ein Haarsieb, weil sie nie \
            ganz klar ist, spült das Stück Fleisch eben ab und setzt es mit der Brühe, die man \
            vom Bodensatz langsam abschüttet, in dem ebenfalls umgespülten Topfe wieder zu Feuer \
            nebst einigen Scorzoner-, einer Sellerie- und Petersilienwurzel.'   
    for wp in enrichSentence(s2, ingE, unitE, quanE):
        print(wp)