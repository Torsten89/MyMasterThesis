""" Rules are collected in "rules"-variable. A rule is a function and has to take the following parameter:
    wps: List of wordProperties
    rcp: Recipe belonging to the sentences represented by wps.
    And returns  altered/improved wps
"""

from informationExtraction.dissolveAmbiguityRules import dissolveAmbiguityRule
from informationExtraction.entityRelationRules import findQuantityAnfUnitOfIngredientRule
from informationExtraction.dontUseRules import dontUseRule
from informationExtraction.altGrpRules import altGrpRule
from informationExtraction.optionalRules import optionalRule

rules = (dissolveAmbiguityRule, findQuantityAnfUnitOfIngredientRule, dontUseRule, altGrpRule, optionalRule)
#rule for opt
#rule for alt (append WP with alt target="1 2")
#rule for dontUse (set WordProperty.ingredient to empty) 

def applyRulesToWordProperties(wps, rcp):
    for rule in rules:
        wps = rule(wps, rcp)
        
    return wps
        
        
        