from xml.dom.minidom import parse
from parserForDavidisCookbook.xmlHelper import buildIngredientDict
from parserForDavidisCookbook.BFormId import BFormId

class IngredientExtractor:
    
    def __init__(self, domOfListOfIngredients, domCookBook=None):
        """ self.__ingDict__ contains ingredients like pepper, eggs...
            Key is lemmatized name of the noun (e.g Franzwein for weißer Franzwein)
            and value is a list of tuples (full name, xml:id of corresponding cue_ingredient-element)
            (e.g. [(weißer Franzwein, weisser_Franzwein), (rother Franzwein, roter_Franzwein)]
        """
        self.__ingDict__ = buildIngredientDict(domOfListOfIngredients)
        self.__composedIngDict__ = None
        
    def getInformation(self, lemma, default=None):
        ingredientInformation = self.__ingDict__.get(lemma, False)
        if ingredientInformation:
            return ingredientInformation
        
        composedIngredientInformation = self.getComposedIngredientInformation(lemma, False)
        if composedIngredientInformation:
            return composedIngredientInformation
        
        return default
    
    # <cue:ingredient target="#Bouillon" ... 
    def getComposedIngredientInformation(self, lemma, default=False):
        composedIngs = ["bouillon", "klöße", "brühe"]
        for composedIng in composedIngs:
            if composedIng in lemma.lower():
                return composedIng
        
        return default
    
    def getRefFromInformation(self, infos, sentence=None, recipe=None):
        if len(infos) == 1 and isinstance(infos[0], BFormId):
            return infos[0].xmlId
        #else some smart stuff


if __name__ == '__main__':
    dom = parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml")
    ingE = IngredientExtractor(dom, None)
    for k, v in ingE.__ingDict__.items():
        print(k, v)
    
    
    