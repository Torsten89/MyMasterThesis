from xml.dom.minidom import parse
from parserForDavidisCookbook.xmlHelper import buildIngredientDict


class IngredientExtractor:
    composedIngs = ("bouillon", "klöße", "brühe")
    
    
    def __init__(self, domOfListOfIngredients):
        """ self.__ingDict__ contains ingredients like pepper, eggs...
            Key is lemmatized name of the noun (e.g Franzwein for weißer Franzwein)
            and value is a list of tuples (full name, xml:id of corresponding cue:ingredient-element)
            
            E.g.: {Franzwein: [(weißer Franzwein, weisser_Franzwein), (rother Franzwein, roter_Franzwein)]}
        """
        self.__ingDict__ = buildIngredientDict(domOfListOfIngredients)
        
    def getIngredientCandidates(self, lemma, recipe=None, sentence=None):
        """ If the lemma is not an ingredient, None is returned, otherwise a set of possible xml:ids, which each point to an cue:ingredient-element.

            An empty set means, that the lemma is an ingredient, but no xml:id/cue:ingredient-element could be found (e.g. with Kalbsklöße).
            
            A set with more than one element states, that there are several possibilities (e.g. Whine could be red or white whine).
            When there are several possibilities the ambiguity can maybe be resolved through providing the sentences of the lemma
            and/or its recipe. E.g. Fleisch can be resolved to "Rindkochfleisch", when the recipe type is Suppe and Rind is in the recipe name.
        """
        ingrCandis = self.__ingDict__.get(lemma, False)
        if ingrCandis:
            return self.__dissolveAmbiguity__(lemma, ingrCandis, recipe, sentence)
        
        if self.__isComposedIngredient__(lemma):
            return set()
        
        return None
    
    def __isComposedIngredient__(self, lemma):
        lemma2lower = lemma.lower()
        for cI in IngredientExtractor.composedIngs:
            if cI in lemma2lower:
                return True
        
        return False
    
    def __dissolveAmbiguity__(self, lemma, candidates, recipe=None, sentence=None):
        if len(candidates) == 1: # there is no ambiguity :)
            return {candidates[0].xmlId}
        
        lemma2lowercase = lemma.lower()
        
        if "fleisch" in lemma2lowercase:
            return self.__dissolveAmbiguityFleisch__(lemma, candidates, recipe, sentence)
        
        if "wein" in lemma2lowercase:
            return self.__dissolveAmbiguityWein__(lemma, candidates, recipe, sentence) # also dissolves Franzwein
        
        # just return all remaining xml:ids because end of wisdom is reached
        return set(candi.xmlId for candi in candidates)

    def __dissolveAmbiguityFleisch__(self, lemma, candidates, recipe, sentence):
        if not recipe: return set(c.xmlId for c in candidates)
        
        if recipe.type=="Suppe":
            if "rind" in recipe.name.lower():
                return set("Rindkochfleisch")
            if "kalb" in recipe.name.lower():
                return set("Kalbkochfleisch")

        return set(c.xmlId for c in candidates)
    
    def __dissolveAmbiguityWein__(self, lemma, candidates, recipe, sentence):
        if not sentence: return set(c.xmlId for c in candidates)

        for lemma in sentence.split():
            lemma2lowercase = lemma.lower()
            if "weiß" in lemma2lowercase:
                return set(c.xmlId for c in candidates if c.bform.startswith("weiß"))
            if "rot" in lemma2lowercase:
                return set(c.xmlId for c in candidates if c.bform.startswith("rot"))

        return set(c.xmlId for c in candidates)
    
    
if __name__ == '__main__':
    dom = parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml")
    ingE = IngredientExtractor(dom, None)
    for k, v in ingE.__ingDict__.items():
        print(k, v)
    
    
    