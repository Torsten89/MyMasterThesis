import unittest
from xml.dom.minidom import parseString
from parserForDavidisCookbook.XmlParser import XmlParser

def createCueMLDom(recipes=[]):
    return parseString('<TEI xmlns="http://www.tei-c.org/ns/1.0" xmlns:cue="http://cueML/ns"> \
                <teiHeader>...</teiHeader> \
                <text> \
                    <body>' \
                        + '\n'.join(recipes) \
                        + ' \
                    </body> \
                </text> \
            </TEI>')

def getRecipeB49():
    return '<cue:recipe type="Suppen." rcp-id="B-49"> \
            <head>Suppe von feiner Gerste (Graupen).</head> \
             \
            <p>Ungefähr zwei Stunden muß die Gerste zu Feuer sein. Sie wird mit etwas Butter in \
               wenig weiches kochendes Wasser gegeben, kurz eingekocht, frische Milch hinzu \
               geschüttet und zu einer sämigen Suppe gekocht. Salz, Zucker und Zimmet darf nicht \
               darin fehlen.</p> \
             \
         </cue:recipe>'
         
def getRecipeB2():
    return ' \
        <cue:recipe type="Suppen." rcp-id="B-2"> \
            <head>Rindfleischsuppe mit Perlgerste und Reis.</head> \
             \
            <p>Wird gekocht wie die vorhergehende, nur mit der Abänderung, daß, wenn die Brühe durch \
               ein Haarsieb geschüttet ist, man verhältnißmäßig 1—2 Eßlöffel voll Mehl mit frischer \
               Butter durchschwitzt, welches jedoch weiß bleiben muß, und die vom Bodensatz \
               abgeklärte Brühe hinzuschüttet. Zugleich gibt man feine Gerste nebst etwas Wurzelwerk \
               in die Suppe, später auch Spargel, Blumenkohl oder Scorzonerwurzeln, was die \
               Jahreszeit bietet, und vor dem Anrichten die Herzblättchen der Sellerieknollen und \
               beliebige Klöße. Man rührt die Suppe mit 1—2 Eidotter ab, indem man solche mit etwas \
               Wasser zerrührt, und unter fortwährendem Rühren die kochende Suppe hinzu gibt. Sie \
               muß gebunden, nur ja nicht zu sämig sein. </p> \
             \
            <note>Anmerk. Will man Reis oder Sago zur Suppe nehmen, so gibt man dieses später \
               hinein. Man rechnet davon auf jede Person bei allen Fleischsuppen einen gestrichenen \
               Eßlöffel voll. </note> \
         </cue:recipe>'

class XmlParserTest(unittest.TestCase):

    def testFindRecipesInDom(self):
        dom = createCueMLDom([getRecipeB49(), getRecipeB2()])
        self.assertEqual(2, len(list(XmlParser(dom).getRecipes())))

    def testRecipeB49(self):
        dom = createCueMLDom([getRecipeB49()])
        recipe = XmlParser(dom).getRecipes().__next__()
        self.assertEqual("Suppen", recipe.rcpType)
        self.assertEqual("B-49", recipe.rcpId)
        self.assertEqual("Suppe von feiner Gerste (Graupen)", recipe.name)
        self.assertEqual("Suppe von feiner Gerste (Graupen)", recipe.name)
        self.assertEqual("Ungefähr zwei Stunden muß die Gerste zu Feuer sein. Sie wird mit etwas Butter in \
wenig weiches kochendes Wasser gegeben, kurz eingekocht, frische Milch hinzu \
geschüttet und zu einer sämigen Suppe gekocht. Salz, Zucker und Zimmet darf nicht \
darin fehlen." \
            , recipe.instructions)
        
    def testRecipeB2(self):
        dom = createCueMLDom([getRecipeB2()])
        recipe = XmlParser(dom).getRecipes().__next__()
        self.assertEqual("Suppen", recipe.rcpType)
        self.assertEqual("B-2", recipe.rcpId)
        self.assertEqual("Wird gekocht wie die vorhergehende, nur mit der Abänderung, daß, wenn die Brühe durch \
ein Haarsieb geschüttet ist, man verhältnißmäßig 1—2 Eßlöffel voll Mehl mit frischer \
Butter durchschwitzt, welches jedoch weiß bleiben muß, und die vom Bodensatz \
abgeklärte Brühe hinzuschüttet. Zugleich gibt man feine Gerste nebst etwas Wurzelwerk \
in die Suppe, später auch Spargel, Blumenkohl oder Scorzonerwurzeln, was die \
Jahreszeit bietet, und vor dem Anrichten die Herzblättchen der Sellerieknollen und \
beliebige Klöße. Man rührt die Suppe mit 1—2 Eidotter ab, indem man solche mit etwas \
Wasser zerrührt, und unter fortwährendem Rühren die kochende Suppe hinzu gibt. Sie \
muß gebunden, nur ja nicht zu sämig sein.\n\
Anmerk. Will man Reis oder Sago zur Suppe nehmen, so gibt man dieses später \
hinein. Man rechnet davon auf jede Person bei allen Fleischsuppen einen gestrichenen \
Eßlöffel voll." \
               , recipe.instructions)
        
    def testGetCertainRecipe(self):
        dom = createCueMLDom([getRecipeB49(), getRecipeB2()])
        recipes = list(XmlParser(dom).getRecipes(["B-2"]))
        self.assertEqual(1, len(recipes))
        self.assertEqual("B-2", recipes[0].rcpId)
        
    def testParseName(self):
        dom = createCueMLDom([getRecipeB49()])
        recipe = XmlParser(dom).getRecipes().__next__()
        self.assertEqual("Suppe von feiner Gerste (Graupen)", recipe.name)
        
if __name__ == "__main__":
    unittest.main()
