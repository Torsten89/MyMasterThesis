from model.WordProperty import WordProperty

def dontUseRule(wps, rcp):
    for i in range(1, len(wps)):
        if wps[i-1].lemma=="als" and wps[i].properties.get(WordProperty.INGREDIENT):
            wps[i].properties[WordProperty.INGREDIENT] = None
             
    return wps