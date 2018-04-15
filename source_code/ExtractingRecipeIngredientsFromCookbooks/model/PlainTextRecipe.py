class PlainTextRecipe:
    
    def __init__(self, rcpId, rcpType, name, paragraphs):
        """ self.paragraphs contains a str for each paragraph of the recipes instruction text. """
        self.rcpId = rcpId
        self.rcpType = rcpType
        self.name = name
        self.paragraphs = paragraphs
