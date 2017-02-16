from model.WordProperty import WordProperty
from informationExtraction.entityRelationRules import otherEntity

def optionalRule(wps, rcp):
    for i in range(len(wps)):
        if wps[i].properties.get(WordProperty.INGREDIENT) is not None and testOptional(wps, i):
            wps[i].properties[WordProperty.OPTIONAL] = True
             
    return wps

def testOptional(wps, i):
    """ Searches for following "kann" and "wegbleiben". """
    foundKann = False
    foundWegbleiben = False
    for j in range(i+1, len(wps)):
        #print(wps[j].lemma, foundKann, foundWegbleiben)
        if otherEntity(wps[j]):
            return foundKann and foundWegbleiben
        
        if wps[j].lemma == "können":
            foundKann = True
        elif wps[j].lemma == "wegbleiben":
            foundWegbleiben = True
            
    return False