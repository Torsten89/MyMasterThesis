from informationExtraction.lemmatization import getLemmas
from xml.dom.minidom import parse
from informationExtraction.IngredientExtractor import IngredientExtractor

def enrichSentence(sentence, ingredientExtractor):
    return [WordProperties(word, lemma, ingE) for (word, lemma) in getLemmas(sentence)]
    

class WordProperties(object):

    def __init__(self, word, lemma, ingredientExtractor):
        self.word = word
        self.lemma = lemma
        
        self.ingredientInfos = ingredientExtractor.getInformation(lemma, None)
        self.quantitiyInfos = None
        self.isUnit = None
        
    def __str__(self):
        entries = []
        for prop, value in self.__dict__.items():
            if value:
                entries.append("{}={}".format(prop, value))
                
        return ", ".join(entries)
        
    
if __name__ == "__main__":
    dom = parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml")
    ingE = IngredientExtractor(dom, None)
#     for k, v in ingD.__ingDict__.items():
#         print(k, v)
    
    s = "Es wird hierzu für 24—30 Personen eine kräftige Bouillon von 8—10 Pfund Rindfleisch mit Wurzelwerk gekocht."
    s = 'Eine Stunde später gießt man die Brühe durch ein Haarsieb, weil sie nie \
            ganz klar ist, spült das Stück Fleisch eben ab und setzt es mit der Brühe, die man \
            vom Bodensatz langsam abschüttet, in dem ebenfalls umgespülten Topfe wieder zu Feuer \
            nebst einigen Scorzoner-, einer Sellerie- und Petersilienwurzel.'   
    for wp in enrichSentence(s, ingE):
        print(wp)