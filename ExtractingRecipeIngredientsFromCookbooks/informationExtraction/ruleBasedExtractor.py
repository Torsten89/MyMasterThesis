""" Rules are collected in "rules"-variable. A rule is a function and has to take the following parameter:
    wps: List of wordProperties
    rcp: Recipe belonging to the sentences represented by wps.
    And returns  altered/improved wps
"""

from informationExtraction.dissolveAmbiguityRules import dissolveAmbiguityRule
from informationExtraction.entityRelationRules import findQuantityAndUnitOfIngredientRule
from informationExtraction.dontUseRules import dontUseRule
from informationExtraction.altGrpRules import altGrpRule
from informationExtraction.optionalRules import optionalRule

rules = (dissolveAmbiguityRule, findQuantityAndUnitOfIngredientRule, dontUseRule, altGrpRule, optionalRule)

def applyRulesToWordProperties(wps, rcp):
    for rule in rules:
        wps = rule(wps, rcp)
        
    return wps
        
        
        