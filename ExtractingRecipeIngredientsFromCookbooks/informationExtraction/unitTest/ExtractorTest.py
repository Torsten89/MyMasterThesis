import unittest
from xml.dom.minidom import parseString, parse
from informationExtraction.UnitExtractor import UnitExtractor
from parserForDavidisCookbook.XmlParser import XmlParser
from informationExtraction.IngredientExtractor import IngredientExtractor
from informationExtraction.Extractor import Extractor

def createCueMLDom(recipes=[]):
    return parseString('\
            <TEI xmlns="http://www.tei-c.org/ns/1.0" xmlns:cue="http://cueML/ns"> \
                <teiHeader>...</teiHeader> \
                <text> \
                    <body>' \
                        + '\n'.join(recipes) \
                        + ' \
                    </body> \
                </text> \
            </TEI>')
    
def getRecipeB49():
    return '\
        <cue:recipe type="Suppen." rcp-id="B-49"> \
            <head>Suppe von feiner Gerste (Graupen).</head> \
             \
            <p>Ungefähr zwei Stunden muß die Gerste zu Feuer sein. Sie wird mit etwas Butter in \
               wenig weiches kochendes Wasser gegeben, kurz eingekocht, frische Milch hinzu \
               geschüttet und zu einer sämigen Suppe gekocht. Salz, Zucker und Zimmet darf nicht \
               darin fehlen.</p> \
             \
         </cue:recipe>'


class ExtractorTest(unittest.TestCase):

    def testExtractionIsValidXml(self):
        uE = UnitExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/cueML/cueML_v0.5.rng"))
        plainTextRcp = XmlParser(createCueMLDom([getRecipeB49()])).getPlainTextRecipes().__next__()
        iE = IngredientExtractor(parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/listIngredients.xml"))
        e = Extractor(iE, uE)
        xmlString = e.extractRecipe(plainTextRcp)
        try:
            parseString(xmlString).toprettyxml()
        except Exception as e:
            self.fail("Not valid xml extracted: {}".format(str(e)))
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()