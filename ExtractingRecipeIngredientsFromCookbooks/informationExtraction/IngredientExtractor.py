from parserForDavidisCookbook.xmlHelper import buildIngredientDict

class IngredientExtractor:
    composedIngs = ("bouillon", "klöße", "kloß", "klößchen", "brühe", "sauce")
    
    def __init__(self, domOfListOfIngredients):
        self.__ingDict__ = buildIngredientDict(domOfListOfIngredients)
        
    def getIngredientCandidates(self, lemma):
        """ If the lemma is not an ingredient, None is returned, otherwise a list of possible model.IngredientCandi. """
        ingCandis = self.__ingDict__.get(lemma)
        if ingCandis:
            return ingCandis
        
        if self.__isComposedIngredient__(lemma):
            return [] # maybe some rule can later guess a target-attri for the composed ingredient
        
        # Mrs. Davidis often uses an "n" in the plural form, which our lemmatisation / TreeTagger cannot handle.
        # E.g.: 2 Eidottern, 2 Saucissen, 2 Pfefferkörnern, ...
        # Only trigger, when word is not an ingredient. Otherwise it would ruin words like 'Thimian' or 'Majoran'
        if lemma[0].isupper() and lemma[-1]=="n":
            return self.getIngredientCandidates(lemma[:-1])

        
        return None
    
    def __isComposedIngredient__(self, lemma):
        lemma2lower = lemma.lower()
        for cI in IngredientExtractor.composedIngs:
            if cI in lemma2lower:
                return True
        
        return False
    