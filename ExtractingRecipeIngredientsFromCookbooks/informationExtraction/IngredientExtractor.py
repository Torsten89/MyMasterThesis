from xml.dom.minidom import parse
from parserForDavidisCookbook.xmlHelper import buildIngredientDict
from informationExtraction.BFormId import BFormId

class IngredientExtractor:
    composedIngs = ["bouillon", "klöße", "brühe"]
    
    def __init__(self, domOfListOfIngredients, domCookBook=None):
        """ self.__ingDict__ contains ingredients like pepper, eggs...
            Key is lemmatized name of the noun (e.g Franzwein for weißer Franzwein)
            and value is a list of tuples (full name, xml:id of corresponding cue_ingredient-element)
            (e.g. [(weißer Franzwein, weisser_Franzwein), (rother Franzwein, roter_Franzwein)]
        """
        self.__ingDict__ = buildIngredientDict(domOfListOfIngredients)
        
    def getIngredientCandidates(self, lemma, recipe=None, sentence=None):
        """ Returns a list of possible xml:ids, which each point to an cue:ingredient definition.
        
            If the lemma is not an ingredient, None is returned.

            An empty list means, that the lemma is an ingredient, but no xml:id could be found.
            
            A list with more than one element states, that there are several possibilities (e.g. Whine could be red or white whine).
            When there are several possibilities the ambiguity can maybe be resolved through providing the sentences of the lemma
            and/or its recipe.
        """
        ingrCandis = self.__ingDict__.get(lemma, False)
        if ingrCandis:
            return self.__dissolveAmbiguity__(lemma, ingrCandis, recipe, sentence)
        
        if self.isComposedIngredient(lemma):
            return []
        
        return None
    
    def isComposedIngredient(self, lemma):
        for cI in IngredientExtractor.composedIngs:
            if cI in lemma.lower():
                return True
        
        return False
    
    def __dissolveAmbiguity__(self, lemma, candidates, recipe=None, sentence=None):
        if len(candidates) == 1:
            return [candidates[0].xmlId]
        
        # some smart stuff to pick viewer candidates
        return [candi.xmlId for candi in candidates]

if __name__ == '__main__':
    dom = parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml")
    ingE = IngredientExtractor(dom, None)
    for k, v in ingE.__ingDict__.items():
        print(k, v)
    print("hier", ingE.__ingDict__.__contains__("Wein"))
    print("hier", ingE.__ingDict__["Wein"])
    
    
    