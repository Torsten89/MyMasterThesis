from informationExtraction.IngredientExtractor import IngredientExtractor
def ingInGoldenStandardIngsExactMatch(ing, goldenStandardIngs, attris):
    """ Ing must have an exact match in ings """
    for i in getPossibleMatchesBasedOnWordPosition(ing, goldenStandardIngs):
        if compare(ing, i, attris):
            return True
       
    return False 


def ingInGoldenStandardIngsRoughMatch(ing, goldenStandardIngs, retrievedIngs, attris):
    """ Ing must have an exact match in ings """
    
    # Fleisch ok wenn irgendein Fleisch ingredient
    if ingInGoldenStandardIngsExactMatch(ing, goldenStandardIngs, attris):
        return True
    
    for composedIng in IngredientExtractor.composedIngs:
        if composedIng in ing.words[0].lower(): return True
    
    # Butter ohne quantity ok wenn butter vorher exact match hatte
    possibleRefs = ing.__dict__.get("ref")
    if not possibleRefs: return
    for possibleRef in possibleRefs:
        for retrievedIng in retrievedIngs:
            refs = retrievedIng.__dict__.get("ref")
            if not refs: continue
            if possibleRef in refs and ingInGoldenStandardIngsExactMatch(retrievedIng, goldenStandardIngs, attris):
                return True
    
    


def getPossibleMatchesBasedOnWordPosition(ing, ings):
    return [i for i in ings if isBetween(i, ing)]

def isBetween(i1, i2):
    if i1.positionInRecipe[0]>i2.positionInRecipe[1] or i2.positionInRecipe[0]>i1.positionInRecipe[1]:
        return False # start posi is behind end posi
    if i1.positionInRecipe[1]<i2.positionInRecipe[0] or i2.positionInRecipe[1]<i1.positionInRecipe[0]:
        return False # end posi is before start posi
    return True


def compare(i1, i2, attris):
    """ Compares 2 model.Ingriedent objects based on the given attri-set. """
    for attriName in attris:
        if i1.__dict__.get(attriName) != i2.__dict__.get(attriName):
            return False
        
    return True