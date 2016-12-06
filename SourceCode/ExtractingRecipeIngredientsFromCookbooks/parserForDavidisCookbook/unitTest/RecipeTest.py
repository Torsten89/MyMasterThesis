import unittest
from parserForDavidisCookbook.Recipe import *

class RecipeTest(unittest.TestCase):
    def testGetSentences(self):
        paragraph = "Die Bärsche werden nicht wie in Nro. 20 bloß auf dem Bauche, sondern mit einem \
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
        self.assertEqual(expectedResult, list(getSentencesOfParagraph(paragraph)))
        
    def testGetTokensOfSentence(self):
        sentence = "Nachdem dies Alles ¼ Stunde gekocht hat, kommen noch Klöße \
von Kalbfleisch, einige hart gekochte Eier in Würfel geschnitten, ein Paar Eßlöffel \
Engl. Soja hinzu, und wenn die Klößchen einige Minuten gekocht haben, ½ Flasche \
Madeira und auch Austern, wenn man sie haben kann."

        expectedResult=["Nachdem", "dies", "Alles", "¼", "Stunde", "gekocht", "hat", ",", "kommen", "noch", "Klöße", \
"von", "Kalbfleisch", ",", "einige", "hart", "gekochte", "Eier", "in", "Würfel", "geschnitten", ",", "ein", "Paar", "Eßlöffel", \
"Engl", ".", "Soja", "hinzu", ",", "und", "wenn", "die", "Klößchen", "einige", "Minuten", "gekocht", "haben", ",", "½", "Flasche", \
"Madeira", "und", "auch", "Austern", ",", "wenn", "man", "sie", "haben", "kann", "."]
        self.assertEqual(expectedResult, list(chunkSentence(sentence)))
        
         
    def testChunkInstructions(self):
        instructions = "Die Bärsche werden nicht wie in Nro. 20 bloß auf dem Bauche, sondern mit einem \
Reibeisen ganz geschuppt und gereinigt und mit kochendem Salzwasser, Zwiebeln, ganzem \
Pfeffer, Lorberblättern und einem Stückchen Butter zu Feuer gebracht und gahr \
gekocht. Dann hackt man 2 hart gekochte Eier mit Petersilie klein, rührt Muskat und \
gestoßenen Zwieback darunter, legt die Fische in eine Schüssel, bestreut sie damit \
und gibt heiße Butter dazu."
        expectedResult="Die\nBärsche\nwerden\nnicht\nwie\nin\nNro.\n20\nbloß\nauf\ndem\nBauche\n,\nsondern\nmit\neinem\n\
Reibeisen\nganz\ngeschuppt\nund\ngereinigt\nund\nmit\nkochendem\nSalzwasser\n,\nZwiebeln\n,\nganzem\n\
Pfeffer\n,\nLorberblättern\nund\neinem\nStückchen\nButter\nzu\nFeuer\ngebracht\nund\ngahr\n\
gekocht\n.\
\n\
Dann\nhackt\nman\n2\nhart\ngekochte\nEier\nmit\nPetersilie\nklein\n,\nrührt\nMuskat\nund\n\
gestoßenen\nZwieback\ndarunter\n,\nlegt\ndie\nFische\nin\neine\nSchüssel\n,\nbestreut\nsie\ndamit\n\
und\ngibt\nheiße\nButter\ndazu\n."

        self.assertEqual(expectedResult, chunkInstructions(instructions))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()