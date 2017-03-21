from model.IngredientCandi import IngredientCandi
from parserForDavidisCookbook.getManualCreatedListOfDavidisIngredientsTxt import getManualCreatedListOfDavidisIngredients

def getElems(node, elemName, withAttris={}):
    """ withAttris = {key: iterator with possible values}
    """
    for elem in node.getElementsByTagName(elemName):
        hasAllAttris = True
        for attriName, possibleValues in withAttris.items():
            if getAttriOrNone(elem, attriName) not in possibleValues:
                hasAllAttris = False
                break
        if hasAllAttris:
            yield elem

def getTextOfNode(node):
    """ Removes \t, \n and many whitespace from the text node. """
    return " ".join(node.data.split())
    
def getAllChildText(node):
    if node.nodeType == node.TEXT_NODE:
        return getTextOfNode(node)
    
    childTexts = [" ".join(getAllChildText(childNode).split()) for childNode in node.childNodes]              
    if not childTexts:
        return ""
    result = childTexts[0]
    for childText in childTexts[1:]:
        if not childText: continue
        if childText[0] in ".,;:": result += childText # handle whitespaces at sentence endings
        else: result += " {}".format(childText)
    return result

def getAttriOrNone(node, attriName):
    try:
        return node.attributes[attriName].value
    except KeyError:
        return None
    
def getUnitValuesFromCueML(cueMLRngDom):
    unitForIngredientElem = list(getElems(cueMLRngDom, "define", {"name":["tei_att.unitForIngredient"]}))[0]
    for valueElem in unitForIngredientElem.getElementsByTagName("value"):
        yield getAllChildText(valueElem)
     
def buildIngredientDict(dom):
    """ Returns dictionary of ingredients from a cue:listIngredient-element. The key is the noun of an ingredient (e.g. Wein for weißer Wein)
        and the value is a list of possible IngredientCandis.
        Additional adds all manual written out ingredients from manualCreatedListOfDavidisIngredients.txt
    """
    ingDict = {}
    
    for ingElem in dom.getElementsByTagName("cue:listIngredient")[0].getElementsByTagName("cue:ingredient"):
        xmlID = ingElem.attributes["xml:id"].value
        basicForms = [getAllChildText(ingElem.getElementsByTagName("cue:prefBasicForm")[0])] \
            + [getAllChildText(altBasicForm) for altBasicForm in ingElem.getElementsByTagName("cue:altBasicForm")]
        for basicForm in basicForms:
            for word in basicForm.split():
                if word[0].isupper():
                    __addAllToDict__(ingDict, word, [IngredientCandi(xmlID, basicForm)])
    
    # add candidates for verbose ingredients like Fleisch
    verboseIngs = ["Fleisch"] 
    for verboseIng in verboseIngs:
        ingDict[verboseIng] = []
    for key in ingDict:
        for verboseIng in verboseIngs:
            if verboseIng == "Fleisch" and "brühe" in key: continue
            if verboseIng.lower() in key: ingDict[verboseIng] += ingDict[key]
    
    # add ingredients from manualCreatedListOfDavidisIngredients.txt
    for ing in getManualCreatedListOfDavidisIngredients():
        if ing not in ingDict: ingDict[ing] = []
    
    return ingDict

def __addAllToDict__(d, key, values):
    try: d[key] += values
    except KeyError: d[key] = values
    