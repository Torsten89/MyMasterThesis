from parserForDavidisCookbook.xmlHelper import buildIngredientDict

class IngredientExtractor:
    composedIngs = ("bouillon", "klöße", "kloß", "klößchen", "brühe", "sauce")
    
    def __init__(self, domOfListOfIngredients):
        self.__ingDict__ = buildIngredientDict(domOfListOfIngredients)
        
    def getIngredientCandidates(self, lemma):
        """ If the lemma is not an ingredient, None is returned, otherwise a list of possible model.IngredientCandi. """
        ingCandis = self.__ingDict__.get(lemma)
        if ingCandis is not None:
            return ingCandis
        
        if self.__isComposedIngredient__(lemma):
            return [] # maybe some rule can later guess a target-attri for the composed ingredient
        
        return None
    
    def __isComposedIngredient__(self, lemma):
        lemma2lower = lemma.lower()
        for cI in IngredientExtractor.composedIngs:
            if cI in lemma2lower:
                return True
        
        return False
    