from model.WordProperty import WordProperty

def altGrpRule(wps, rcp):
    for i in range(1, len(wps)):
        if wps[i].properties.get(WordProperty.INGREDIENT) is not None and wps[i-1].lemma=="statt":
            wps[i].properties[WordProperty.ALT_GRP] = "1"
            addAlt2(wps, i)
            wps.append(WordProperty("", "", {WordProperty.ALT_GRP:["1","2"]}))
             
    return wps

def addAlt2(wps, i):
    for j in range(i+1, len(wps)):
        if wps[j].properties.get(WordProperty.INGREDIENT) is not None:
            wps[j].properties[WordProperty.ALT_GRP] = "2"
            if j+1 < len(wps) and wps[j+1].lemma == "und": addAlt2(wps, j)
            break
            