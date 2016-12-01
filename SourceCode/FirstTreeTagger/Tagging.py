#Environment variable TREETAGGER_HOME=/path/to/TreeTagger/cmd has to be set for TreeTaggers nltk
from treetagger import TreeTagger

if __name__ == '__main__':
    tt_ger = TreeTagger(language='german')
    # print(tt_ger.tag('Das Haus hat einen großen hübschen Garten.'))
    tags =tt_ger.tag('Eine Stunde später gießt man die Brühe durch ein Haarsieb, weil sie nie \
            ganz klar ist, spült das Stück Fleisch eben ab und setzt es mit der Brühe, die man \
            vom Bodensatz langsam abschüttet, in dem ebenfalls umgespülten Topfe wieder zu Feuer \
            nebst einigen Scorzoner-, einer Sellerie- und Petersilienwurzel')
    
    for t in tags:
        print(t)
        
    print(tt_ger.tag("Meer doof"))