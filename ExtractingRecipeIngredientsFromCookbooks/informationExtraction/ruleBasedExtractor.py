""" Rules are collected in rules-var. A rule has to take the following parameter:
    i: Index of targeted wordProperty,
    wps: List of wordProperties
    rcp: Recipe belonging to the sentences represented by wps 
"""

from model.WordProperty import WordProperty
from informationExtraction.dissolveAmbiguityRules import dissolveAmbiguity

rules = set([dissolveAmbiguity])
#rule for opt
#rule for alt (append WP with alt target="1 2")
#rule for dontUse (set WordProperty.ingredient to empty) 

def applyRulesToWordProperties(wps, rcp):
    newWPs = wps[:]
    for i, _ in enumerate(wps):
        newWPs = applyRules(i, wps, rcp)
        
    return newWPs
                
def applyRules(i, wps, rcp):
    if wps[i].properties.get(WordProperty.ingredient):
        for rule in rules:
            wps = rule(i, wps, rcp)
    
    return wps
        
        
        