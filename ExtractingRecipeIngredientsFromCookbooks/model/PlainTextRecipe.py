class PlainTextRecipe:
    
    def __init__(self, rcpId, rcpType, name, sentences):
        """ self.instructionSentences is a list of sentences / strings from the instruction text of the recipe. """
        self.rcpId = rcpId
        self.rcpType = rcpType
        self.name = name
        self.instructionSentences = sentences #
