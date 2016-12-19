from xml.dom.minidom import parse
from parserForDavidisCookbook.unitTest.XmlParserTest import getTaggedRecipeB16, createCueMLDom
from parserForDavidisCookbook.XmlParser import XmlParser
from tagger.lemmatization import getLemmas
from tagger.IngredientDict import IngredientDict

class Tagger:
    def __init__(self, ingDict):
        """ ingDict is an instance of tagger.IngredientDict
        """
        self.ingDict = ingDict
        self.recipe = None

    def tagRecipe(self, recipe):
        self.recipe = recipe
        
        for s in recipe.getSentences():
            for word, pos, lemma in getLemmas(s):
                if word[0].isupper():
                    ing = self.ingDict.contains(lemma)
                    if ing: print(ing)
    
    def xmlIdsDispatcher(self, lemma, sentence, xmlIds):
        # if lemma.tolower().find("fleisch")>-1: if self.recipe.type="Suppe" and recipe.name.find("Rind"): take Kochrindfleisch
        # if lemma = Wein and weiß in sentence: take Weißwein
        pass    

if __name__ == '__main__':
    pathToListIngredients = "/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml"
    tagger = Tagger(IngredientDict(parse(pathToListIngredients)))
    
    recipe = XmlParser(createCueMLDom([getTaggedRecipeB16()])).getRecipes().__next__()
    print(recipe)
    
    tagger.tagRecipe(recipe)
    
#     for s in recipe.getSentences():
#         print(s)
#         print(getLemmas(s))
    
    
