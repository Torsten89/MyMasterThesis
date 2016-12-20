import string

shortenings = ["Nro.", "No.", "Engl."] + [chapterNumber+"." for chapterNumber in string.ascii_uppercase[:-3]]
punctuation = string.punctuation.replace("-", "") # e.g don't split Kartoffel-Klöße as two chunks
  

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
        
        if word[0] in punctuation: # e.g. (siehe Vorbereitungsregeln)
            tokens.append(word[0])
            word = word[1:]
            
        if "—" in word and len(word) > 1: # 8—10 but nothing to do for 8 — 10
            parts = word.split("—")
            yield parts[0]
            yield "—"
            word = parts[1]
            
        if word:
            if word[-1] in punctuation and word not in shortenings:
                if len(word)>1 and word[-2] in punctuation: # Möhren).
                    tokens += [word[:-2], word[-2], word[-1]]
                else:
                    tokens += [word[:-1], word[-1]]
            else:
                tokens.append(word)
            
        for token in tokens:
            yield token


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
        
    def chunkRecipeForManualTagging(self):
        """Yields each word of the recipe separated by a new line
        """
        for c in chunkSentence(self.name):
            yield "{}\n".format(c)
        yield "\n"
        for c in chunkInstructions(self.instructions):
            yield c 
        yield "\n"   
        
    def mergeIngredients(self):
        for ref, optIng in self.optIngredients.items():
            if ref in self.ingredients:
                self.optIngredients[ref] = self.ingredients[ref] #  assuming first entry provides more information
                del self.ingredients[ref]
                
        for ref, altIng in self.altIngredients.items():
            if ref in self.ingredients:
                self.ingredients[ref].altGrp = self.altIngredients[ref].altGrp # copy altGrp if not already present
                self.altIngredients[ref] = self.ingredients[ref] # assuming first entry provides more information
                del self.ingredients[ref]
                
    def __str__(self):
        result = self.name + "\n\nZutaten:\n"
        
        for ing in self.ingredients.values():
            result += "{}\n".format(str(ing))
        
        result += "\nOptionale Zutaten:\n"
        for ing in self.optIngredients.values():
            result += "{}\n".format(str(ing))
        
        result += "\nAlternative Zutaten:\n"
        alts = {}
        for ing in self.altIngredients.values():
            altGrp = ing.altGrp
            if not altGrp in alts: alts[altGrp]=[ing]
            else: alts[altGrp].append(ing)
        for alt in self.alts:
            altIs = [" und ".join([str(ing) for ing in alts[i]]) for i in alt]
            result += ", oder ".join(altIs)
            
        return result
    
    def getSentences(self):
        """ Yield each sentence of the recipe. The recipe.name is also a sentence
        """
        yield self.name
        
        for paragrah in self.instructions.split("\n"):
            for sentence in getSentencesOfParagraph(paragrah):
                yield sentence
              
                
        
        
