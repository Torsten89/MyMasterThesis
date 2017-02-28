from treetagger import TreeTagger #Environment variable TREETAGGER_HOME=/path/to/TreeTagger/cmd has to be set for TreeTaggers nltk
import string 

treeTagger = TreeTagger(language='german')
unknownTag = "<unknown>"
truncTag = "TRUNC"
nNTag ="NN"

truncatedEndings = ("wurzel", "klöße", "kloß", "brot", "brod")
shortenings = ("Nro.", "No.", "Engl.") + tuple(chapterNumber+"." for chapterNumber in string.ascii_uppercase[:-3])

def getWordLemmaTuples(sentence):
    treeTaggerTags = treeTagger.tag(sentence)
            
    for i, [word, pos, lemma] in enumerate(treeTaggerTags):
        if "|" in lemma: # Linse|Linsen
            lemma = lemma.split("|")[0] 
        if lemma == unknownTag:
            lemma = guessLemma(word)
        if pos == truncTag: # e.g. Sellerie- und Petersilienwurzeln -> Selleriewurzel
            lemma = word.replace("-", findTruncatedEnd(i, treeTaggerTags))
        treeTaggerTags[i][2] = lemma
            
    return [(word, lemma) for [word, _, lemma] in treeTaggerTags]

def guessLemma(word):
    if word[-1]!="-" and "-" in word:
        wordParts = word.split("-")
        return wordParts[0]+(getWordLemmaTuples(wordParts[1])[0][1]).lower()

    return word # take the word as lemma, when its lemma is unknown
            
def findTruncatedEnd(i, tags):
    """ i is the position of the truncated word in the sentence. """
    for [word, pos, _] in tags[i+1:]: #search next normal nominas
        if pos == nNTag:
            for truncatedEnd in truncatedEndings:
                if truncatedEnd in word.lower():
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
    s2 = "Dann nimmt man 2—3 Pfund kleine Aale, zieht die Haut ab, schneidet sie in 3 \
Finger breite Stücke, wäscht sie rein, und läßt sie in kochendem Wasser und Salz halb \
gahr kochen, thut sie in die Suppe, nebst feinen Suppenkräutern, einigen \
Zitronenscheiben, macht dieselbe mit in Butter gelb geröstetem Mehl gebunden und gibt \
kurz vor dem Anrichten Fleisch- oder Schwammklöße hinein."
    s="\n\n"
    for w, pos, l in treeTagger.tag(s):
        print(w, pos, l)

    
    