from parserForDavidisCookbook.xmlHelper import buildIngredientDict

class IngredientExtractor:
    composedIngs = ("bouillon", "klöße", "brühe") 
    
    def __init__(self, domOfListOfIngredients):
        self.__ingDict__ = buildIngredientDict(domOfListOfIngredients)
        
    def getIngredientCandidates(self, lemma):
        """ If the lemma is not an ingredient, None is returned, otherwise a list of possible IngredientCandis. """
        ingCandis = self.__ingDict__.get(lemma)
        if ingCandis:
            return ingCandis
        
        if self.__isComposedIngredient__(lemma):
            return [] # maybe some rule can later guess a target-attri of the composed ingredient
        
        return None
    
    def __isComposedIngredient__(self, lemma):
        lemma2lower = lemma.lower()
        for cI in IngredientExtractor.composedIngs:
            if cI in lemma2lower:
                return True
        
        return False
    