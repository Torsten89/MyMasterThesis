from parserForDavidisCookbook.xmlHelper import getAllChildText, getAttriOrNone, getElems,\
    getTextOfNode
from parserForDavidisCookbook.Recipe import Recipe, Sentence
from parserForDavidisCookbook.Ingredient import Ingredient
from xml.dom.minidom import parse
from informationExtraction.lemmatization import truncatedEndings, shortenings,\
    tokenise, tokeniseWords
import string

rcpIdTagName = "rcp-id"

class XmlParser(object):

    def __init__(self, dom):
        ''' It is assumed that the XML is valid against cueML
        '''
        self.dom = dom

    def getRecipes(self, rcpIds=[]):
        """ When rcpIds is an empty list, all recipes will be parsed, what is the default -
            Otherwise only recipes, which have a rcpId specified in rcpIds
        """ 
        withAttris = {} if not rcpIds else {rcpIdTagName:rcpIds}
        for xmlRecipe in getElems(self.dom, "cue:recipe", withAttris):
            yield self.__parseXmlRecipe__(xmlRecipe)
    
    def __parseXmlRecipe__(self, xmlRecipe):
        rcpId = xmlRecipe.attributes[rcpIdTagName].value
        rcpType = xmlRecipe.attributes["type"].value[:-1]  # remove . at the end
        sentencesWithExtractedIngs = list(self.__getSentenecsWithExtractedIngsFromNode__(xmlRecipe))
        name = sentencesWithExtractedIngs[0].tokens[:-1] # remove . at the end
        return Recipe(rcpId, rcpType, name, sentencesWithExtractedIngs)

    def __getSentenecsWithExtractedIngsFromNode__(self, node):
        """ Yields namedtuple Sentence(tokens of sentence, (Ingredient, start of ing in sentence, end of ing in sentence)).
            For example "1 EL <recipeIngredient ref='#abc'>Engl. Soja</recipeIngredient>."
            yields (["1 kg Fleisch ."], (Ingredient({'ref':'#abc'}), 3, 4))
        """
        sentence = []
        ingsOfSentence = [] # [(ing, startIndex, endIndex)]
        for (tokens, ing) in self.__getTokensWithExtractedIngs__(node):
            #print(sentence, tokens)
            if ing: ingsOfSentence.append((ing, len(sentence), len(sentence)+len(tokens)-1))
            sentence += tokens
            sentenceCopy = sentence[:]
            i = 0
            for w in sentenceCopy:
                i += 1
                if w.endswith(".") and w not in shortenings:
                    yield Sentence(" ".join(sentence[:i]), ingsOfSentence)
                    sentence = sentence[i:]
                    if sentence and sentence[0] in string.whitespace:
                        sentence = sentence[1:]
                    ingsOfSentence = []
                    i = 0
             
    def __getTokensWithExtractedIngs__(self, node):
        """ Yields ([words of text], Ingredient) for each childNode .
            If there is no Ingredient within a childNode Ingredient is None
        """
        for childNode in node.childNodes:
            if childNode.nodeType == childNode.TEXT_NODE:
                yield (tokeniseWords(childNode.data.split()), None)
            elif childNode.localName == "recipeIngredient":
                yield (tokeniseWords(getAllChildText(childNode).split()), Ingredient.ingFromXmlIngElem(childNode))
            else:
                yield from self.__getTokensWithExtractedIngs__(childNode)

               
if __name__ == "__main__":
    # /home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/
    # cookbook = parse("../recipesExtracted.xml")
    cookbook = XmlParser(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/recipesExtracted.xml"))
    for recipe in cookbook.getRecipes(["B-1"]):
        print(recipe.sentencesWithExtractedIngs)
