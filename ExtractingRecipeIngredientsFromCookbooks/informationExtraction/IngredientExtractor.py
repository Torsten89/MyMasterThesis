from xml.dom.minidom import parse
from parserForDavidisCookbook.xmlHelper import getAllChildText
from collections import namedtuple

BFormId = namedtuple("BasisFormAndXmlId", ["bform", "xmlId"])

class IngredientExtractor:
    def __init__(self, domOfListOfIngredients, domCookBook=None):
        """ self.__ingDict__ contains ingredients like pepper, eggs...
            Key is lemmatized name of the noun (e.g Franzwein for weißer Franzwein)
            and value is a list of tuples (full name, xml:id of corresponding cue_ingredient-element)
            (e.g. [(weißer Franzwein, weisser_Franzwein), (rother Franzwein, roter_Franzwein)]
        """
        self.__ingDict__ = buildIngDict(domOfListOfIngredients)
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
            if lemma.lower() in composedIngs:
                return composedIng
        
        return default

def buildIngDict(dom):
    """ Returns dictionary of ingredients from a cue:listIngredient-element. The key is the noun of an ingredient (e.g. Wein for weißer Wein)
        and the value is a list of tuples (full name, possible xml:id) (e.g. [("weißer Wein", "weißer_Wein"), ("roter Wein", "roter_Wein")])
    """
    ingDict = {}
    
    for ingElem in dom.getElementsByTagName("cue:listIngredient")[0].getElementsByTagName("cue:ingredient"):
        xmlId = ingElem.attributes["xml:id"].value
        basicForms = [getAllChildText(ingElem.getElementsByTagName("cue:prefBasicForm")[0])] \
            + [getAllChildText(altBasicForm) for altBasicForm in ingElem.getElementsByTagName("cue:altBasicForm")]
        for basicForm in basicForms:
            for word in basicForm.split():
                if word[0].isupper():
                    __addAllToDict__(ingDict, word, [BFormId(basicForm, xmlId)])
    
    #add verbose ingredients like Fleisch
    verboseIngs = ["Fleisch", "Ohr"]
    for verboseIng in verboseIngs:
        ingDict[verboseIng] = []
    for key in ingDict.keys():
        for verboseIng in verboseIngs:
            if verboseIng.lower() in key: ingDict[verboseIng] += ingDict[key]
    
    return ingDict

def __addAllToDict__(d, key, values):
    try: d[key] += values
    except KeyError: d[key] = values


if __name__ == '__main__':
    dom = parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml")
    ingD = IngredientExtractor(dom, None)
    for k, v in ingD.__ingDict__.items():
        print(k, v)
    
    
    