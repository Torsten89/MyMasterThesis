from treetagger import TreeTagger #Environment variable TREETAGGER_HOME=/path/to/TreeTagger/cmd has to be set for TreeTaggers nltk


treeTagger = TreeTagger(language='german')
unknownTag = "<unknown>"
truncTag = "TRUNC"
nNTag ="NN"

truncedEndings = ("wurzel", )

def getLemmas(sentence):
    """ sentence is a string
        The result is a list with "tuples" of the form [[word1, pos1, lemma1), [word2, pos2, lemma2], ...]
    """
    tags = treeTagger.tag(sentence)
    for i, [word, pos, lemma] in enumerate(tags):
        if lemma == unknownTag and pos == truncTag:
            tags[i][2] = word.replace("-", findTruncedEnd(i, tags))
    
    return tags
            
def findTruncedEnd(i, tags):
    for [word, pos, lemma] in tags[i+1:]: #search next normal nomina
        if pos == nNTag:
            for truncedEnd in truncedEndings:
                if lemma.find(truncedEnd) > -1:
                    return truncedEnd
                     
            
        
if __name__ == '__main__':
#     printLemmas("Der Soja macht die Suppe gewürzreicher, kann jedoch gut wegbleiben, und statt Madeira kann man weißen Franzwein und etwas Rum nehmen.")
    
    #Kartoffel-Klöße
    #weißer Franzwein
    #braunes Gewürz
    s = 'Eine Stunde später gießt man die Brühe durch ein Haarsieb, weil sie nie \
            ganz klar ist, spült das Stück Fleisch eben ab und setzt es mit der Brühe, die man \
            vom Bodensatz langsam abschüttet, in dem ebenfalls umgespülten Topfe wieder zu Feuer \
            nebst einigen Scorzoner-, einer Sellerie- und Petersilienwurzel'
    
    
