import string
import chunk

shortenings = ["Nro.", "No.", "A.", "Engl."]
punctuation = string.punctuation.replace("-", "")
  

def chunkInstructions(instructions):
        chunksOfSentences = []
        for paragrah in instructions.split("\n"):
            for sentence in getSentencesOfParagraph(paragrah):
                chunksOfSentences.append(list(chunkSentence(sentence)))
                
        # per line one token and two sentences are separated through an empty line
        return "\n\n".join(["\n".join(chunks) for chunks in chunksOfSentences])

def getSentencesOfParagraph(paragraph):
    """ Man kocht solche nach Nro. 22 und richtet sie mit einer Capern-Sauce an."""
    guessSentences = paragraph.split(".")
    sentence = ""
    for g in guessSentences:
        if not g.strip(): # empty word / only spaces
            continue
        sentence += g +"."
        if "{}.".format(g.split()[-1]) in shortenings:
            continue
        else:
            yield sentence.strip()
            sentence = ""
              
def chunkSentence(sentence):
    for word in sentence.split():
        tokens = []
        
        if word[0] in punctuation:
            tokens.append(word[0])
            word = word[1:]
            
        if "—" in word and len(word) > 1: # 8—10 but nothing to do for 8 — 10
            parts = word.split("—")
            yield parts[0]
            yield "—"
            word = parts[1]
            
        if word and word[-1] in punctuation and word not in shortenings:
            if word[-2] in punctuation: # (Möhren).
                tokens += [word[:-2], word[-2], word[-1]]
            else:
                tokens += [word[:-1], word[-1]]
        elif word:
            tokens.append(word)
            
        for token in tokens:
            yield token

class Recipe(object):

    def __init__(self, rcpId, recipeType, name, instructions,
                 ingredients=None, optionalIngredients=None, alternativeIngredients=None,
                 totalTime=None, cookTime=None):
        self.recipeType = recipeType
        self.rcpId = rcpId
        self.name = name
        self.instructions = instructions

        self.ingredients = ingredients        
        self.optionalIngredients = optionalIngredients
        self.alternativeIngredients = alternativeIngredients
        self.totalTime = totalTime
        self.cookTime = cookTime
        
    def chunksWithNewlines(self):
        for c in chunkSentence(self.name):
            yield "{}\n".format(c)
        yield "\n"
        for c in chunkInstructions(self.instructions):
            yield c 
        yield "\n"   
        
        
