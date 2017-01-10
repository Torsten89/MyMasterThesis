class Recipe:

    def __init__(self, rcpId, rcpType, name, instructions,
                 ingredients={}, optIngredients={}, altIngredients={},
                 totalTime=[], cookTime=[], rcpYield=None, refs=[], alts=[]):
        self.rcpId = rcpId
        self.rcpType = rcpType
        self.name = name
        self.instructions = instructions

        self.ingredients = ingredients        
        self.optIngredients = optIngredients
        self.altIngredients = altIngredients
        self.totalTime = totalTime
        self.cookTime = cookTime
        self.rcpYield = rcpYield
        self.refs = refs
        self.alts = alts
    
    def yieldParagraphes(self):
        """ Yield each sentence of the recipe. The recipe.name is also a sentence
        """
        yield self.name
        
        for paragraph in self.instructions.split("\n"):
            yield paragraph

              
                
        
        
