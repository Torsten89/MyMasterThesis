from recipeModel.Recipe import Recipe
from recipeModel.Ingredient import Ingredient
from parserForDavidisCookbook.xmlHelper import getAllChildText, getAttriOrNone, getElems

rcpIdTagName = "rcp-id"

class XmlParser(object):

    def __init__(self, dom):
        ''' It is assumed that the XML is valid against cueML
        '''
        self.dom = dom

    def getRecipes(self, rcpIds=[]):
        """ When rcpIds is an empty list, all recipes will be parsed.
            Otherwise only recipes, which have a in rcpIds specified rcp-id.
        """ 
        withAttris = {} if not rcpIds else {rcpIdTagName:rcpIds}
        for xmlRecipe in getElems(self.dom, "cue:recipe", withAttris):
            yield self.parseRecipe(xmlRecipe)
    
    def parseRecipe(self, xmlRecipe):
        rcpId = xmlRecipe.attributes[rcpIdTagName].value
        rcpType = xmlRecipe.attributes["type"].value[:-1]  # remove . at the end
        name = getAllChildText(xmlRecipe.getElementsByTagName("head")[0])[:-1]  # remove . at the end
        instructions = self.getInstructions(xmlRecipe)
        ingredients, optIngredients, altIngredients = self.getIngredients(xmlRecipe)
        alts = self.getAlts(xmlRecipe)

        return Recipe(rcpId, rcpType, name, instructions, ingredients, optIngredients, altIngredients, alts=alts)
    
    def getInstructions(self, xmlRecipe):
        return "\n".join([getAllChildText(p) for p in xmlRecipe.getElementsByTagName("p")] \
            + [getAllChildText(note) for note in xmlRecipe.getElementsByTagName("note")] \
        )
        
    def getIngredients(self, xmlRecipe):
        ingredients, optIngredients, altIngredients, ingredientsWithLinks = {}, {}, {}, []
        for ingredientElem in xmlRecipe.getElementsByTagName("cue:recipeIngredient"):
            ref = getAttriOrNone(ingredientElem, "ref")
            target = getAttriOrNone(ingredientElem, "target")
            quantity = getAttriOrNone(ingredientElem, "quantity")
            atLeast = getAttriOrNone(ingredientElem, "atLeast")
            atMost = getAttriOrNone(ingredientElem, "atMost")
            unit = getAttriOrNone(ingredientElem, "unit")
            ingYield = getAttriOrNone(ingredientElem, "yield")
            ingYieldUnit = getAttriOrNone(ingredientElem, "yieldUnit")
            ingredient = Ingredient(ref, target, quantity, atLeast, atMost, unit, ingYield, ingYieldUnit)
            
            if target:
                ref = target
            
            if getAttriOrNone(ingredientElem, "optional"):
                ingredient.optional = True
                optIngredients[ref] = ingredient
                continue
            
            altGrp = getAttriOrNone(ingredientElem, "altGrp")
            if altGrp:
                ingredient.altGrp = altGrp
                altIngredients[ref] = ingredient
                continue
            
            if getAttriOrNone(ingredientElem, "dontUse"):
                ingredient.dontUse = True
            
            ingredients[ref] = ingredient
        
        return ingredients, optIngredients, altIngredients
    
    def getAlts(self, xmlRecipe):
        return [getAttriOrNone(alt, "target").split() for alt in xmlRecipe.getElementsByTagName("cue:alt")]
        
