import string
import chunk

def chunkInstructions(instructions):
        chunksOfSentences = []
        for paragrah in instructions.split("\n"):
            for sentence in getSentencesOfParagraph(paragrah):
                chunksOfSentences.append(list(chunkSentence(sentence)))
                
        # per line one token and two sentences are separated through an empty line
        return "\n\n".join(["\n".join(chunks) for chunks in chunksOfSentences])

def getSentencesOfParagraph(paragraph):
    """ Man kocht solche nach Nro. 22 und richtet sie mit einer Capern-Sauce an."""
    guesses = paragraph.split(".")
    sentence = ""
    for g in guesses:
        if not g.strip():
            continue
        sentence += g +"."
        if g[-3:]=="Nro":
            continue
        else:
            yield sentence.strip()
            sentence = ""
        
def chunkSentence(sentence):
    for word in sentence.split():
        tokens = []
        
        if word[0] in string.punctuation:
            tokens.append(word[0])
            word = word[1:]
            
        if "—" in word: # 8—10
            parts = word.split("—")
            yield parts[0]
            yield "—"
            word = parts[1]
            
        if word and word[-1] in string.punctuation and word!="Nro.":
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
        
    def chunk(self):
        yield "#{}\n".format(self.rcpId)
        for c in chunkSentence(self.name):
            yield "{}\n".format(c)
        yield "\n"
        for c in chunkInstructions(self.instructions):
            yield c 
        yield "\n"   
        
        
