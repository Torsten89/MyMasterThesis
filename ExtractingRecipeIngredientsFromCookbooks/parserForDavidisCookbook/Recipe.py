from collections import namedtuple

Sentence= namedtuple("Sentence", ["tokens", "ings"]) 

class Recipe:

    def __init__(self, rcpId, rcpType, name, sentencesWithExtractedIngs):
        self.rcpId = rcpId
        self.rcpType = rcpType
        self.name = name
        self.sentencesWithExtractedIngs = sentencesWithExtractedIngs
    
    def getSentences(self):
        for s in self.sentencesWithExtractedIngs:
            yield s.tokens

              
                
         
