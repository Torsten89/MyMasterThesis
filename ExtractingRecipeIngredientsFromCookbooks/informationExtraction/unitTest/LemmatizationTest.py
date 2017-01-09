import unittest
from dictionaryBasedChecks.lemmatization import getWordLemmaTuples


class Test(unittest.TestCase):


    def testWurzelTrunc(self):
        sentence = 'Eine Stunde später gießt man die Brühe durch ein Haarsieb, weil sie nie \
            ganz klar ist, spült das Stück Fleisch eben ab und setzt es mit der Brühe, die man \
            vom Bodensatz langsam abschüttet, in dem ebenfalls umgespülten Topfe wieder zu Feuer \
            nebst einigen Scorzoner-, einer Sellerie- und Petersilienwurzel'
        lemmas = (lemma for [word, pos, lemma] in getWordLemmaTuples(sentence))
        self.assertTrue("Scorzonerwurzel" in lemmas)
        self.assertTrue("Selleriewurzel" in lemmas)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()