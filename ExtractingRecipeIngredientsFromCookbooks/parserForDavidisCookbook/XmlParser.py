from parserForDavidisCookbook.xmlHelper import getAllChildText, getAttriOrNone, getElems,\
    getTextOfNode
from parserForDavidisCookbook.Recipe import Recipe
from parserForDavidisCookbook.Ingredient import Ingredient
from xml.dom.minidom import parse
from informationExtraction.lemmatization import truncatedEndings

rcpIdTagName = "rcp-id"

class XmlParser(object):

    def __init__(self, dom):
        ''' It is assumed that the XML is valid against cueML
        '''
        self.dom = dom

    def getXmlRecipes(self, rcpIds=[]):
        """ When rcpIds is an empty list, all recipes will be parsed.
            Otherwise only recipes, which have a in rcpIds specified rcp-id.
        """ 
        withAttris = {} if not rcpIds else {rcpIdTagName:rcpIds}
        for xmlRecipe in getElems(self.dom, "cue:recipe", withAttris):
            yield xmlRecipe
    
    def parseXmlRecipe(self, xmlRecipe):
        rcpId = xmlRecipe.attributes[rcpIdTagName].value
        rcpType = xmlRecipe.attributes["type"].value[:-1]  # remove . at the end
        alts = self.getAlts(xmlRecipe)
        sentences = self.getSentenecsFromNode(xmlRecipe)
        for s in sentences:
            print("SENTENCE: ", s)

    def getSentenecsFromNode(self, node):
        sentence = []
        for w in self.getWords(node):
            sentence.append(w)
            
            if w.endswith(".") and w not in truncatedEndings: # ingredient tag end gefolgt von . !!!
                yield " ".join(sentence)
                sentence = []
                
        #yield "BYE"
                
    def getWords(self, node):
        for childNode in node.childNodes:
            if childNode.nodeType == childNode.TEXT_NODE:
                for w in childNode.data.split():
                    yield w
            elif childNode.localName == "recipeIngredient":
                for w in getAllChildText(childNode).split():
                    yield w
                # parse Ingredient Object
            else:
                yield from self.getWords(childNode)
    
    def getInstructions(self, xmlRecipe):
        return "\n".join([getAllChildText(p) for p in xmlRecipe.getElementsByTagName("p")] \
            + [getAllChildText(note) for note in xmlRecipe.getElementsByTagName("note")] \
        )
        
    
    def getAlts(self, xmlRecipe):
        return [getAttriOrNone(alt, "target").split() for alt in xmlRecipe.getElementsByTagName("cue:alt")]
        
        
if __name__ == "__main__":
    # /home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/
    # cookbook = parse("../recipesExtracted.xml")
    cookbook = XmlParser(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/recipesExtracted.xml"))
    for xmlRecipe in cookbook.getXmlRecipes(["B-1"]):
        cookbook.parseXmlRecipe(xmlRecipe)
