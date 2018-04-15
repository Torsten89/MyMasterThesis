from informationExtraction.IngredientExtractor import IngredientExtractor

def ingInIngsExactMatch(ing, goldenStandardIngs, attris):
    for i in getPossibleMatchesBasedOnWordPosition(ing, goldenStandardIngs):
        if compare(ing, i, attris):
            return True
       
    return False 


def ingInIngsRoughMatch(ing, goldenStandardIngs, retrievedIngs, attris):
    """ An ing is assumed to be relevant, when it is in IngredientExtractor.composedIngs.
        It is also relevant, when it was mentioned at another place in the recipe and that was an exact match - 
        e.g. in "Man nehme 1-2 Pfund <recipeIngredient>Rindfleisch</recipeIngredient>. [...]
        Das Fleisch wird 2h gekocht." "Fleisch" should not be assumed as false match.
    """
    
    # composed ing is OK
    for composedIng in IngredientExtractor.composedIngs:
        # ing.words[0] is good enough, because we need the roughMatch only for recipes extracted by this program
        # and this program tags only one noun of an ingredient. Therefore words is something like ["Kalbfleischbrühe"]
        if composedIng in ing.words[0].lower(): return True
    
    # Mention of an ing at another place
    possibleRefs = ing.__dict__.get("ref")
    if not possibleRefs: return False
    for possibleRef in possibleRefs.split():
        for goldenStandardIng in goldenStandardIngs:
            refs = goldenStandardIng.__dict__.get("ref")
            if not refs: continue
            if possibleRef in refs.split() and ingInIngsExactMatch(goldenStandardIng, retrievedIngs, attris):
                return True
            
    return False

def getPossibleMatchesBasedOnWordPosition(ing, ings):
    return [i for i in ings if isBetween(i.positionInRecipe, ing.positionInRecipe)]

def isBetween(t1, t2):
    if t1[0]>t2[1] or t2[0]>t1[1]:
        return False # start posi is behind end posi
    if t1[1]<t2[0] or t2[1]<t1[0]:
        return False # end posi is before start posi
    return True

def compare(i1, i2, attris):
    global eineEineMist;
    """ Compares 2 model.Ingriedent objects based on the given attri-set. """
    if "ref" in attris:
        #when many possible refs are given, it is assumed to be correct, when they share a common one
        i1refs = i1.__dict__.get("ref").split()
        i2refs = i2.__dict__.get("ref").split()
        if not (i1refs == i2refs or any([i1ref in i2refs for i1ref in i1refs])):
            return False
        attris.remove("ref")
        
    for attriName in attris:
        if i1.__dict__.get(attriName) != i2.__dict__.get(attriName):
            return False
        
    return True