from model.PlainTextRecipe import PlainTextRecipe
from parserForDavidisCookbook.xmlHelper import getElems, getAllChildText,\
    getAttriOrNone
from informationExtraction.textualHelper import splitAndRemovePunctuations
from model.Ingredient import Ingredient

rcpIdTagName = "rcp-id"

class XmlParser(object):

    def __init__(self, dom):
        ''' It is assumed that the XML is valid against cueML
        '''
        self.dom = dom

    def getPlainTextRecipes(self, rcpIds=[]):
        """ When rcpIds is an empty list, all recipes will be parsed, what is the default -
            Otherwise only recipes, which have a rcpId specified in rcpIds
        """ 
        for xmlRecipe in self.getXmlRecipes(rcpIds):
            yield parseXml2PlainTextRecipe(xmlRecipe)
    
    def getXmlRecipes(self, rcpIds=[]):
        """ When rcpIds is an empty list, all recipes will be parsed, what is the default -
            Otherwise only recipes, which have a rcpId specified in rcpIds
        """ 
        withAttris = {} if not rcpIds else {rcpIdTagName:rcpIds}
        return [xmlRecipe for xmlRecipe in getElems(self.dom, "cue:recipe", withAttris)]

def parseXml2PlainTextRecipe(xmlRecipe):
    rcpId = xmlRecipe.attributes[rcpIdTagName].value
    rcpType = xmlRecipe.attributes["type"].value
    name = getAllChildText(list(getElems(xmlRecipe, "head"))[0])
    paragraphs = [getAllChildText(x) for x in getElems(xmlRecipe, "p")] + [getAllChildText(x) for x in getElems(xmlRecipe, "note")]
    return PlainTextRecipe(rcpId, rcpType, name, paragraphs)

def getIngsFromNode(node):
    ings, _ =  parseIngsFromNodeHelper(node, 0)
    return ings

def parseIngsFromNodeHelper(node, wordCount):
    ings = []
    for childNode in node.childNodes:
        if childNode.nodeType == childNode.TEXT_NODE:
            wordCount += len(splitAndRemovePunctuations(getAllChildText(childNode)))
        elif childNode.localName == "recipeIngredient":
            ingStart = wordCount
            ingWords = splitAndRemovePunctuations(getAllChildText(childNode))
            wordCount += len(ingWords)
            ings.append(ingFromXmlIngElem(childNode, ingWords, (ingStart, wordCount-1)))
        else:
            newIngs, newWordCount = parseIngsFromNodeHelper(childNode, wordCount)
            ings += newIngs
            wordCount = newWordCount
            
    return ings, wordCount

def ingFromXmlIngElem(xmlIngElem, ingWords, positionInRecipe):
    return Ingredient({attriName:getAttriOrNone(xmlIngElem, cueMLName) for attriName, cueMLName in Ingredient.allowedAttris.items()}, ingWords, positionInRecipe)
                




