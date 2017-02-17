from model.WordProperty import WordProperty

def findQuantityAndUnitOfIngredientRule(wps, rcp):
    for i in range(len(wps)):
        wps = findQuantityAndUnitOfIngredient(i, wps)
        
    return wps

def findQuantityAndUnitOfIngredient(i, wps):
    """ Searches the left closest quantity and unit of an ingredient."""
    if wps[i].properties.get(WordProperty.INGREDIENT) is not None:
        wps[i].properties[WordProperty.QUANTITY] = findQuantity(wps[:i])
        wps[i].properties[WordProperty.UNIT] = findUnit(wps[:i])
    
    return wps

def findQuantity(wps):
    for i in range(len(wps)-1, -1, -1):
        if otherEntity(wps[i]):
            return None
        if wps[i].properties.get(WordProperty.QUANTITY):
            if i==0 or wps[i-1].lemma not in ("Nro.", "No."): return wps[i].lemma # nach No. 2 <- 2 is not quantity!
    
def findUnit(wps):
    for i in range(len(wps)-1, -1, -1):
        if otherEntity(wps[i]):
            return None
        unit = wps[i].properties.get(WordProperty.UNIT)
        if unit:
            return unit
        
otherEntites = ["Person", "Stunde", "Stündchen", "Minute", "Wasser"]
def otherEntity(wordProperty):
    if wordProperty.lemma in otherEntites:
        return True
    
    if wordProperty.properties.get(WordProperty.INGREDIENT) is not None:
        return True
    
    return False