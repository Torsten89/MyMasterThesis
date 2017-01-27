import unittest
from xml.dom.minidom import parseString
from parserForDavidisCookbook.XmlParser import XmlParser
from parserForDavidisCookbook.Ingredient import Ingredient

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
         
def getRecipeB2():
    return '\
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
         
def getTaggedRecipeB16():
    return '\
    <cue:recipe type="Suppen." rcp-id="B-16"> \
        <head>Mock Turtle Suppe.</head> \
         \
        <p>Es wird hierzu für <cue:recipeYield atLeast="24" atMost="30" unit="people">24—30 Personen</cue:recipeYield> \
eine kräftige <cue:recipeIngredient target="#Bouillon" \
                >Bouillon</cue:recipeIngredient> von 8—10 Pfund <cue:recipeIngredient \
                ref="#Rindkochfleisch" atLeast="8" atMost="10" unit="Pfund" \
                >Rindfleisch</cue:recipeIngredient> mit <cue:recipeIngredient \
                ref="#Wurzelwerk">Wurzelwerk</cue:recipeIngredient> gekocht. Zugleich bringt \
            man einen großen <cue:recipeIngredient ref="#Kalbskopf" quantity="1" \
                >Kalbskopf</cue:recipeIngredient>, eine <cue:recipeIngredient \
                ref="#Schweineschnauze" quantity="1">Schweineschnauze</cue:recipeIngredient> \
            und <cue:recipeIngredient ref="#Schweineohr">Ohren</cue:recipeIngredient>, einen \
                <cue:recipeIngredient ref="#Ochsengaumen" quantity="1" \
                >Ochsengaumen</cue:recipeIngredient> und eine geräucherte \
                <cue:recipeIngredient ref="#Ochsenzunge" quantity="1" \
                >Ochsenzunge</cue:recipeIngredient> zu Feuer und kocht dies Alles gahr, aber \
            nicht zu weich. Kalt, schneidet man es in kleine, länglich viereckige Stückchen, \
            gibt das Fleisch in die Bouillon, nebst <cue:recipeIngredient \
                ref="#braunes_Gewürz">braunem Gewürz</cue:recipeIngredient>, ein Paar \
            Messerspitzen <cue:recipeIngredient ref="#Cayennepfeffer" quantity="ein Paar" \
                unit="Messerspitze">Cayenne-Pfeffer</cue:recipeIngredient>, einige \
                <cue:recipeIngredient ref="#Midder" quantity="einige" \
                >Kalbsmidder</cue:recipeIngredient> in Stückchen geschnitten <ref \
                target="#A-16">(siehe Vorbereitungsregeln)</ref>, kleine \
                <cue:recipeIngredient ref="#Saucisse">Saucissen</cue:recipeIngredient>, so \
            viel Kalbskopfbrühe, daß man hinreichend Suppe hat, und macht dies mit in \
                <cue:recipeIngredient ref="#Butter">Butter</cue:recipeIngredient> braun \
            gemachtem <cue:recipeIngredient ref="#Mehl">Mehl</cue:recipeIngredient> \
            gebunden. Nachdem dies Alles ¼ Stunde gekocht hat, kommen noch \
                <cue:recipeIngredient target="#L-4">Klöße von \
                Kalbfleisch</cue:recipeIngredient>, einige hart gekochte \
                <cue:recipeIngredient ref="#Ei" quantity="einige" \
                >Eier</cue:recipeIngredient> in Würfel geschnitten, ein Paar Eßlöffel \
                <cue:recipeIngredient ref="#Englische_Soja" quantity="ein Paar" unit="EL" \
                >Engl. Soja</cue:recipeIngredient> hinzu, und wenn die Klößchen einige \
            Minuten gekocht haben, ½ Flasche <cue:recipeIngredient ref="#Madeira" \
                quantity="0.5" unit="Flasche">Madeira</cue:recipeIngredient> und auch \
                <cue:recipeIngredient ref="#Auster" optional="True">Austern</cue:recipeIngredient>, wenn man \
            sie haben kann. Dann wird die Suppe sogleich angerichtet.</p> \
         \
        <note>Anmerk. Der <cue:recipeIngredient ref="#Englische_Soja" optional="True" \
                >Soja</cue:recipeIngredient> macht die Suppe gewürzreicher, kann jedoch gut \
            wegbleiben, und statt <cue:recipeIngredient ref="#Madeira" altGrp="1" \
                >Madeira</cue:recipeIngredient> kann man <cue:recipeIngredient \
                ref="weißen_Franzwein" altGrp="2">weißen Franzwein</cue:recipeIngredient> \
            und etwas <cue:recipeIngredient ref="#Rum" altGrp="2" quantity="etwas" \
                >Rum</cue:recipeIngredient> nehmen<cue:alt target="1 2"/>. Sowohl die \
            Bouillon als Kalbskopf können schon am vorhergehenden Tage, ohne Nachtheil der \
            Suppe, gekocht werden.</note> \
    </cue:recipe>'
    

class XmlParserTest(unittest.TestCase):
    def testFindRecipesInDom(self):
        dom = createCueMLDom([getRecipeB49(), getRecipeB2()])
        self.assertEqual(2, len(list(XmlParser(dom).getPlainTextRecipes())))
         
    def testRecipeB49(self):
        dom = createCueMLDom([getRecipeB49()])
        recipe = XmlParser(dom).getPlainTextRecipes().__next__()
        self.assertEqual("Suppen", recipe.rcpType)
        self.assertEqual("B-49", recipe.rcpId)
        self.assertEqual("Suppe von feiner Gerste (Graupen).", recipe.name)
        instructionSentences = ["Ungefähr zwei Stunden muß die Gerste zu Feuer sein.",
            "Sie wird mit etwas Butter in wenig weiches kochendes Wasser gegeben, kurz eingekocht, frische Milch hinzu geschüttet und zu einer sämigen Suppe gekocht.",
            "Salz, Zucker und Zimmet darf nicht darin fehlen."]
        self.assertEqual(instructionSentences, recipe.instructionSentences)
        
         
    def testRecipeB2(self):
        dom = createCueMLDom([getRecipeB2()])
        recipe = XmlParser(dom).getPlainTextRecipes().__next__()
        self.assertEqual("Suppen", recipe.rcpType)
        self.assertEqual("B-2", recipe.rcpId)
        self.assertEqual("Rindfleischsuppe mit Perlgerste und Reis.", recipe.name)
         
    def testGetCertainRecipe(self):
        dom = createCueMLDom([getRecipeB49(), getRecipeB2()])
        recipes = list(XmlParser(dom).getPlainTextRecipes(["B-2"]))
        self.assertEqual(1, len(recipes))
        self.assertEqual("B-2", recipes[0].rcpId)
                    
         
if __name__ == "__main__":
    unittest.main()
