class Recipe(object):

    def __init__(self, recipeType, rcpId, name, instructions, ingredients,
                 optionalIngredients=None, totalTime=None, cookTime=None):
        self.recipeType = recipeType
        self.rcpId = rcpId
        self.name = name
        self.instructions = instructions
        self.ingredients = ingredients
        
        self.optionalIngredients = optionalIngredients
        self.totalTime = totalTime
        self.cookTime = cookTime
        
