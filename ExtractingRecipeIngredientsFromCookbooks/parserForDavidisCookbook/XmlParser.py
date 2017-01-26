from model.PlainTextRecipe import PlainTextRecipe
from informationExtraction.parseHelper import getSentences
from parserForDavidisCookbook.xmlHelper import getElems, getAllChildText

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
        withAttris = {} if not rcpIds else {rcpIdTagName:rcpIds}
        for xmlRecipe in getElems(self.dom, "cue:recipe", withAttris):
            yield self.__parseXmlPlainTextRecipe__(xmlRecipe)
    
    def __parsePlainTextRecipe__(self, xmlRecipe):
        rcpId = xmlRecipe.attributes[rcpIdTagName].value
        rcpType = xmlRecipe.attributes["type"].value[:-1]  # remove . at the end
        sentences = list(getSentences(getAllChildText(xmlRecipe)))
        name = sentences[0]
        return PlainTextRecipe(rcpId, rcpType, name, sentences[1:])

