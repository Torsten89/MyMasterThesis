from treetagger import TreeTagger #Environment variable TREETAGGER_HOME=/path/to/TreeTagger/cmd has to be set for TreeTaggers nltk
import string 

treeTagger = TreeTagger(language='german')
unknownTag = "<unknown>"
truncTag = "TRUNC"
nNTag ="NN"

truncatedEndings = ("wurzel", "klöße", "kloß")
shortenings = ("Nro.", "No.", "Engl.") + tuple(chapterNumber+"." for chapterNumber in string.ascii_uppercase[:-3])

def getWordLemmaTuples(sentence):
    treeTaggerTags = treeTagger.tag(sentence)
            
    for i, [word, pos, lemma] in enumerate(treeTaggerTags):
        if lemma == unknownTag:
            treeTaggerTags[i][2] = word # take the word as lemma, when its lemma is unknown
        if pos == truncTag: # e.g. Sellerie- und Petersilienwurzeln -> Selleriewurzel
            treeTaggerTags[i][2] = word.replace("-", findTruncatedEnd(i, treeTaggerTags))
    
    return [(word, lemma) for [word, _, lemma] in treeTaggerTags]
            
def findTruncatedEnd(i, tags):
    """ i is the position of the truncated word in the sentence.
    """
    for [_, pos, lemma] in tags[i+1:]: #search next normal nomina
        if pos == nNTag:
            for truncatedEnd in truncatedEndings:
                if lemma.find(truncatedEnd) > -1:
                    return truncatedEnd
    
    return ""

def splitIntoSentences(text):
    guessSentences = text.split(".") # guessed because e.g.: " Man kocht solche nach Nro. 22 und richtet sie mit einer Capern-Sauce an."
    sentence = ""
    for g in guessSentences:
        if not g.strip(): # empty word / only spaces
            continue
        sentence += g + "."
        if "{}.".format(g.split()[-1]) in shortenings:
            continue
        else:
            yield sentence.strip()
            sentence = ""


def splitAndRemovePunctuations(s):
    return [removePunctuations(word) for word in s.split() if removePunctuations(word)]

def removePunctuations(word):
    if word[0] in string.punctuation:
        word = word[1:]
       
    if word and word[-1] in string.punctuation:
        return word[:-1]
    else:
        return word    
    
    
if __name__ == "__main__":
    s = "Zugleich gibt man feine Gerste nebst etwas Wurzelwerk in die Suppe, später auch \
später auch Spargel Blumenkohl oder Scorzonerwurzeln, was die Jahreszeit bietet,\
und vor dem Anrichten die Herzblättchen der Sellerieknollen und beliebige Klöße."
    for w, pos, l in treeTagger.tag(s):
        print(w, pos, l)
    
    print(treeTagger.tag("Korinthen"))
    
    