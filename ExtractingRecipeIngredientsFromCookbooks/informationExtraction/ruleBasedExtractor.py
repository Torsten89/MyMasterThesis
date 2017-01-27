""" Rules are collected in "rules". A rule is a function, has to take the following parameter:
    wps: List of wordProperties
    rcp: Recipe belonging to the sentences represented by wps.
    And returns  altered/improved wps
"""

from informationExtraction.dissolveAmbiguityRules import dissolveAmbiguityRule
from informationExtraction.entityRelationRules import findQuantityAnfUnitOfIngredientRule

rules = set([dissolveAmbiguityRule, findQuantityAnfUnitOfIngredientRule])
#rule for opt
#rule for alt (append WP with alt target="1 2")
#rule for dontUse (set WordProperty.ingredient to empty) 

def applyRulesToWordProperties(wps, rcp):
    for rule in rules:
        wps = rule(wps, rcp)
        
    return wps
        
        
        