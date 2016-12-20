
def getElems(node, elemName, withAttris={}):
    """ withAttris = {key: iterator with possible values}
    """
    for elem in node.getElementsByTagName(elemName):
        hasAllAttris = True
        for k, possibleValues in withAttris.items():
            if elem.attributes[k].value not in possibleValues:
                hasAllAttris = False
                break
        if hasAllAttris:
            yield elem

def getAllChildText(node):
    if node.nodeType == node.TEXT_NODE:
        return " ".join(node.data.split()) # removes \t and many whitespace
    
    childTexts = [" ".join(getAllChildText(childNode).split()) for childNode in node.childNodes]              
    if not childTexts:
        return ""
    result = childTexts[0]
    for childText in childTexts[1:]:
        if not childText: continue
        if childText[0] in ".,;:": result += childText
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
    