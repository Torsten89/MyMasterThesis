from model.IngredientCandi import IngredientCandi
from model.WordProperty import WordProperty

def dissolveAmbiguityRule(wps, rcp):
    for i in range(len(wps)):
        if wps[i].properties.get(WordProperty.INGREDIENT): wps = dissolveAmbiguity(i, wps, rcp)

    return wps

def dissolveAmbiguity(i, wps, rcp):
    oldCandis = wps[i].properties[WordProperty.INGREDIENT]
    if len(oldCandis) == 1: # there is no ambiguity :)
        return wps
    
    lemma2lowercase = wps[i].lemma.lower()
    if "fleisch" in lemma2lowercase:
        wps[i].properties[WordProperty.INGREDIENT] = dissolveAmbiguityFleisch(rcp, oldCandis)
    elif "wein" in lemma2lowercase:
        wps[i].properties[WordProperty.INGREDIENT] = dissolveAmbiguityWein(wps, oldCandis)
    
    return wps

def dissolveAmbiguityFleisch(rcp, candis):
    if not rcp: return candis # nothing there which helps guessing :(
    
    if rcp.rcpType == "Suppen":
        if "rind" in rcp.name.lower():
            return [IngredientCandi("Rindkochfleisch", "Rindkochfleisch")]
        if "kalb" in rcp.name.lower():
            return [IngredientCandi("Kalbkochfleisch", "Kalbkochfleisch")]

    return candis # end of wisdom is reached, so just return

def dissolveAmbiguityWein(wps, oldCandis):
    for wp in wps:
        lemma2lowercase = wp.lemma.lower()
        if "weiß" in lemma2lowercase:
            return [candi for candi in oldCandis if candi.basicForm.startswith("weiß")]
        if "rot" in lemma2lowercase:
            return [candi for candi in oldCandis if candi.basicForm.startswith("rot")]
        
    return oldCandis # end of wisdom is reached, so return oldCandis
