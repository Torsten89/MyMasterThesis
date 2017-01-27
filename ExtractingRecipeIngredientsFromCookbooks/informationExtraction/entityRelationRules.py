from model.WordProperty import WordProperty

def findQuantityAnfUnitOfIngredientRule(wps, rcp):
    for i in range(len(wps)):
        wps = findQuantityAndUnitOfIngredient(i, wps)
        
    return wps

def findQuantityAndUnitOfIngredient(i, wps):
    """ Searches the left closest quantity and unit of an ingredient."""
    if wps[i].properties.get(WordProperty.ingredient) is not None:
        wps[i].properties[WordProperty.quantity] = findQuantity(reversed(wps[:i]))
        wps[i].properties[WordProperty.unit] = findUnit(reversed(wps[:i]))
    
    return wps

def findQuantity(wordProperties):
    for wp in wordProperties:
        if otherEntity(wp):
            return None
        if wp.properties.get(WordProperty.quantity):
            return wp.lemma
    
def findUnit(wordProperties):
    for wp in wordProperties:
        unit = wp.properties.get(WordProperty.unit)
        if otherEntity(wp):
            return None
        if unit:
            return unit
        
otherEntites = ["Person", "Stunde", "Minute"]
def otherEntity(wordProperty):
    if wordProperty.lemma in otherEntites:
        return True
    
    if wordProperty.properties.get(WordProperty.ingredient) is not None:
        return True
    
    return False