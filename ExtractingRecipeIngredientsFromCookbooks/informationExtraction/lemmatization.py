from treetagger import TreeTagger #Environment variable TREETAGGER_HOME=/path/to/TreeTagger/cmd has to be set for TreeTaggers nltk

treeTagger = TreeTagger(language='german')
unknownTag = "<unknown>"
truncTag = "TRUNC"
nNTag ="NN"

truncatedEndings = ("wurzel", )

def getLemmas(sentence):
    treeTaggerTags = treeTagger.tag(sentence)
            
    for i, [word, pos, lemma] in enumerate(treeTaggerTags):
        if lemma == unknownTag:
            treeTaggerTags[i][2] = word # take the word as lemma when its lemma is unknown
        if pos == truncTag: # e.g. Sellerie- und Petersilienwurzeln -> Selleriewurzel
            treeTaggerTags[i][2] = word.replace("-", findTruncatedEnd(i, treeTaggerTags))
    
    return [(word, lemma) for [word, _, lemma] in treeTaggerTags]
            
def findTruncatedEnd(i, tags):
    """ i is the position of the truncated word in the sentence,
        and tags is a "tuple" of [word, PoS, lemma] for each word
    """
    for [word, pos, lemma] in tags[i+1:]: #search next normal nomina
        if pos == nNTag:
            for truncatedEnd in truncatedEndings:
                if lemma.find(truncatedEnd) > -1:
                    return truncatedEnd
    
    return ""
            
        
if __name__ == '__main__':
#     "Der Soja macht die Suppe gewürzreicher, kann jedoch gut wegbleiben, und statt Madeira kann man weißen Franzwein und etwas Rum nehmen."
    
    #Kartoffel-Klöße
    #weißer Franzwein
    #braunes Gewürz
    s = 'Eine Stunde später gießt man die Brühe durch ein Haarsieb, weil sie nie \
            ganz klar ist, spült das Stück Fleisch eben ab und setzt es mit der Brühe, die man \
            vom Bodensatz langsam abschüttet, in dem ebenfalls umgespülten Topfe wieder zu Feuer \
            nebst einigen Scorzoner-, einer Sellerie- und Petersilienwurzel'
    print(getLemmas("braunes Gewürz"))
    
    
