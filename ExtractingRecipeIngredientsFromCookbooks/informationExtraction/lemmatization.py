from treetagger import TreeTagger #Environment variable TREETAGGER_HOME=/path/to/TreeTagger/cmd has to be set for TreeTaggers nltk
import string 

treeTagger = TreeTagger(language='german')
unknownTag = "<unknown>"
truncTag = "TRUNC"
nNTag ="NN"

truncatedEndings = ("wurzel", )
shortenings = ("Nro.", "No.", "Engl.") + tuple(chapterNumber+"." for chapterNumber in string.ascii_uppercase[:-3])
punctuations =  string.punctuation.replace("-","")

def getWordLemmaTuples(sentence):
    treeTaggerTags = treeTagger.tag(sentence)
            
    for i, [word, pos, lemma] in enumerate(treeTaggerTags):
        if lemma == unknownTag:
            treeTaggerTags[i][2] = word # take the word as lemma when its lemma is unknown
        if pos == truncTag: # e.g. Sellerie- und Petersilienwurzeln -> Selleriewurzel
            treeTaggerTags[i][2] = word.replace("-", findTruncatedEnd(i, treeTaggerTags))
    
    return [(word, lemma) for [word, _, lemma] in treeTaggerTags]
            
def findTruncatedEnd(i, tags):
    """ i is the position of the truncated word in the sentence,
        and each tag in tags is a "tuple" of [word, PoS, lemma] for each word
    """
    for [word, pos, lemma] in tags[i+1:]: #search next normal nomina
        if pos == nNTag:
            for truncatedEnd in truncatedEndings:
                if lemma.find(truncatedEnd) > -1:
                    return truncatedEnd
    
    return ""

def tokenise(word):
    if not word: raise StopIteration()
    
    if word[0] in punctuations:
        yield word[0]
        word = word[1:]
       
    if word and word[-1] in punctuations and word not in shortenings:
        yield from tokenise(word[:-1])
        yield word[-1]
    else:
        yield word    
    
def tokeniseWords(words):
    return [token for word in words for token in tokenise(word) if token]
    
            
if __name__ == "__main__":
    print(treeTagger.tag("Irgendwas , (etwas) ."))