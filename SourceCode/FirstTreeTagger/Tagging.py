#Environment variable TREETAGGER_HOME=/path/to/TreeTagger/cmd has to be set for TreeTaggers nltk
from treetagger import TreeTagger

if __name__ == '__main__':
    tt_ger = TreeTagger(language='german')
    
    tags =tt_ger.tag('Eine Stunde später gießt man die Brühe durch ein Haarsieb, weil sie nie \
            ganz klar ist, spült das Stück Fleisch eben ab und setzt es mit der Brühe, die man \
            vom Bodensatz langsam abschüttet, in dem ebenfalls umgespülten Topfe wieder zu Feuer \
            nebst einigen Scorzoner-, einer Sellerie- und Petersilienwurzel')
    for t in tags:
        print(t)

    
#     for t in tt_ger.tag("Man nehme Parfüm Nr. 1. Dieses riecht besonders gut."): # Nro. geht nicht -.-
#         print(t)
        
