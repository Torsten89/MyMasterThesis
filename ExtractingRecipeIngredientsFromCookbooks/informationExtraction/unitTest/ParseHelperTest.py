import unittest
from informationExtraction.parseHelper import getWordLemmaTuples, getSentences

class ParseHelperTest(unittest.TestCase):

    def testWurzelTrunc(self):
        sentence = 'Eine Stunde später gießt man die Brühe durch ein Haarsieb, weil sie nie \
            ganz klar ist, spült das Stück Fleisch eben ab und setzt es mit der Brühe, die man \
            vom Bodensatz langsam abschüttet, in dem ebenfalls umgespülten Topfe wieder zu Feuer \
            nebst einigen Scorzoner-, einer Sellerie- und Petersilienwurzel'
        lemmas = (lemma for (word, lemma) in getWordLemmaTuples(sentence))
        self.assertTrue("Scorzonerwurzel" in lemmas)
        self.assertTrue("Selleriewurzel" in lemmas)
        
    def testGetSentences(self):
        text = "Die Bärsche werden nicht wie in Nro. 20 bloß auf dem Bauche, sondern mit einem \
Reibeisen ganz geschuppt und gereinigt und mit kochendem Salzwasser, Zwiebeln, ganzem \
Pfeffer, Lorberblättern und einem Stückchen Butter zu Feuer gebracht und gahr \
gekocht. Dann hackt man 2 hart gekochte Eier mit Petersilie klein, rührt Muskat und \
gestoßenen Zwieback darunter, legt die Fische in eine Schüssel, bestreut sie damit \
und gibt heiße Butter dazu."
        expectedResult=["Die Bärsche werden nicht wie in Nro. 20 bloß auf dem Bauche, sondern mit einem \
Reibeisen ganz geschuppt und gereinigt und mit kochendem Salzwasser, Zwiebeln, ganzem \
Pfeffer, Lorberblättern und einem Stückchen Butter zu Feuer gebracht und gahr \
gekocht.",
        "Dann hackt man 2 hart gekochte Eier mit Petersilie klein, rührt Muskat und \
gestoßenen Zwieback darunter, legt die Fische in eine Schüssel, bestreut sie damit \
und gibt heiße Butter dazu."]
        self.assertEqual(expectedResult, list(getSentences(text)))


if __name__ == "__main__":
    unittest.main()