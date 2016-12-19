from xml.dom.minidom import parseString, parse
from parserForDavidisCookbook.xmlHelper import getAllChildText, getAttriOrNone
from recipeModel.Ingredient import Ingredient

class IngredientDict:
    def __init__(self, domOfListOfIngredients, domOfRecipes):
        self.__ingDict__ = buildIngDict(domOfListOfIngredients)
        self.__composedIngDict__ = None # (e.g. Boullion or Kalbfleischklöße)
        
    def contains(self, word):
        return self.__ingDict__.get(word, False)
        
        # if word in multipleWordIngredient
        
        return False

def buildIngDict(dom):
    """ Returns dictionary of ingredients from a cue:listIngredient-element. The key is the noun of an ingredient (e.g. Wein for weißer Wein)
        and the value is a list of tuples (possible xml:id, full name) (e.g. [("weißer_Wein", "weißer Wein"), ("roter_Wein", "roter Wein")])
    """
    ingDict = {}
    
    for ingElem in dom.getElementsByTagName("cue:listIngredient")[0].getElementsByTagName("cue:ingredient"):
        xmlId = ingElem.attributes["xml:id"].value
        basicForms = [getAllChildText(ingElem.getElementsByTagName("cue:prefBasicForm")[0])] \
            + [getAllChildText(altBasicForm) for altBasicForm in ingElem.getElementsByTagName("cue:altBasicForm")]
        for basicForm in basicForms:
            for word in basicForm.split():
                if word[0].isupper():
                    __addAllToDict__(ingDict, word, [(xmlId, basicForm),])
    
    #add verbose ingredients like Fleisch
        ingDict["Fleisch"]=[]
        for key in ingDict.keys():
            if "fleisch" in key: ingDict["Fleisch"] += ingDict[key]
    
    return ingDict

def __addAllToDict__(d, key, values):
    try: d[key] += values
    except KeyError: d[key] = values


if __name__ == '__main__':
#     dom = parseString('<cue:listIngredient xmlns="http://www.tei-c.org/ns/1.0" xmlns:cue="http://cueML/ns"> \
#     <cue:ingredient xml:id="Rindkochfleisch" BLSref="U180100"> \
#         <cue:prefBasicForm>Rindfleisch</cue:prefBasicForm> \
#     </cue:ingredient> \
#     <cue:ingredient xml:id="Wurzelwerk" BLSref="G600000"> \
#         <cue:prefBasicForm>Wurzelwerk</cue:prefBasicForm> \
#         <cue:note>Another possible value for BLSref is "X560003"</cue:note> \
#     </cue:ingredient> \
#     <cue:ingredient xml:id="Midder" BLSref="V582100"> \
#         <cue:prefBasicForm>Midder</cue:prefBasicForm> \
#         <cue:altBasicForm>Kalbsmidder</cue:altBasicForm> \
#         <cue:altBasicForm>Bries</cue:altBasicForm> \
#         <cue:altBasicForm>Kalbsmilch</cue:altBasicForm> \
#         <cue:note>"Kalbsmidder ist auch unter dem Synonym: Bries, Kalbsmilch bekannt. Kalbsmilch ist die Thymusdrüse des Kalbes. 100 g frische Kalbsmilch enthalten 99,8 kcal, 3,4 g Fett, 17,2 g Eiweiß, 77,8 g Wasser, 1,91 mg Eisen, 268 mg Cholesterin und 0,42 g Purine. Dieses Organ ist bei Jungtieren voll entwickelt. Bei erwachsenen Tieren bildet sich das Organ zurück. Kalbsmilch wird zur Herstellung von Spezialitäten, wie Suppen, Klöße und Ragout, verwendet." (http://www.cosmiq.de/qa/show/70827/was-ist-kalbsmidder/)</cue:note> \
#         <cue:note>2asfd asdf</cue:note> \
#     </cue:ingredient> \
# </cue:listIngredient>')


    dom = parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml")
    ingD = IngredientDict(dom, None)
    for k, v in ingD.__ingDict__.items():
        print(k, v)
    
    
    