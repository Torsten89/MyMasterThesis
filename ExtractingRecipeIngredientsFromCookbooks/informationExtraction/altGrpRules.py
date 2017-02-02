from model.WordProperty import WordProperty
from informationExtraction.entityRelationRules import otherEntity

def altGrpRule(wps, rcp):
    for i in range(1, len(wps)):
        if wps[i].properties.get(WordProperty.ingredient) is not None and wps[i-1].lemma=="statt":
            wps[i].properties[WordProperty.altGrp] = "1"
            addAlt2(wps, i)
             
    return wps

def addAlt2(wps, i):
    for j in range(i+1, len(wps)):
        if wps[j].properties.get(WordProperty.ingredient) is not None:
            wps[j].properties[WordProperty.altGrp] = "2"
            if j+1 < len(wps) and wps[j+1].lemma == "und": addAlt2(wps, j)
            break
            