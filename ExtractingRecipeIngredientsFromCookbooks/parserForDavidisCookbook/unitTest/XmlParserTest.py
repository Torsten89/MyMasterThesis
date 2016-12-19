import unittest
from xml.dom.minidom import parseString
from parserForDavidisCookbook.XmlParser import XmlParser
from recipeModel.Ingredient import Ingredient

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
darin fehlen.", recipe.instructions)
        
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
muß gebunden, nur ja nicht zu sämig sein.\
\n\
Anmerk. Will man Reis oder Sago zur Suppe nehmen, so gibt man dieses später \
hinein. Man rechnet davon auf jede Person bei allen Fleischsuppen einen gestrichenen \
Eßlöffel voll.", recipe.instructions)
        
    def testGetCertainRecipe(self):
        dom = createCueMLDom([getRecipeB49(), getRecipeB2()])
        recipes = list(XmlParser(dom).getRecipes(["B-2"]))
        self.assertEqual(1, len(recipes))
        self.assertEqual("B-2", recipes[0].rcpId)
        
    def testParseName(self):
        dom = createCueMLDom([getRecipeB49()])
        recipe = XmlParser(dom).getRecipes().__next__()
        self.assertEqual("Suppe von feiner Gerste (Graupen)", recipe.name)
        
    def testGetTaggedRecipeInstructionB16(self):
        dom = createCueMLDom([getTaggedRecipeB16()])
        recipe = XmlParser(dom).getRecipes().__next__()
        self.assertEqual('Es wird hierzu für 24—30 Personen eine kräftige Bouillon von 8—10 Pfund Rindfleisch \
mit Wurzelwerk gekocht. Zugleich bringt man einen großen Kalbskopf, eine \
Schweineschnauze und Ohren, einen Ochsengaumen und eine geräucherte Ochsenzunge zu \
Feuer und kocht dies Alles gahr, aber nicht zu weich. Kalt, schneidet man es in \
kleine, länglich viereckige Stückchen, gibt das Fleisch in die Bouillon, nebst \
braunem Gewürz, ein Paar Messerspitzen Cayenne-Pfeffer, einige Kalbsmidder in \
Stückchen geschnitten (siehe Vorbereitungsregeln), kleine Saucissen, so viel \
Kalbskopfbrühe, daß man hinreichend Suppe hat, und macht dies mit in Butter braun \
gemachtem Mehl gebunden. Nachdem dies Alles ¼ Stunde gekocht hat, kommen noch Klöße \
von Kalbfleisch, einige hart gekochte Eier in Würfel geschnitten, ein Paar Eßlöffel \
Engl. Soja hinzu, und wenn die Klößchen einige Minuten gekocht haben, ½ Flasche \
Madeira und auch Austern, wenn man sie haben kann. Dann wird die Suppe sogleich \
angerichtet.\
\n\
Anmerk. Der Soja macht die Suppe gewürzreicher, kann jedoch gut wegbleiben, und \
statt Madeira kann man weißen Franzwein und etwas Rum nehmen. Sowohl die Bouillon als \
Kalbskopf können schon am vorhergehenden Tage, ohne Nachtheil der Suppe, gekocht \
werden.', recipe.instructions)
        
    def testGetTaggedRecipeIngredientsB16(self):
        dom = createCueMLDom([getTaggedRecipeB16()])
        recipe = XmlParser(dom).getRecipes().__next__()
        self.assertIn(Ingredient(target="#Bouillon"), recipe.ingredients.values())
        self.assertIn(Ingredient(ref="#Englische_Soja", optional=True), recipe.optIngredients.values())
        self.assertIn(Ingredient(ref="#Rum", altGrp="2", quantity="etwas"), recipe.altIngredients.values())
        self.assertIn(["1", "2"], recipe.alts)
        
        recipe.mergeIngredients()
        # print(recipe)
        
    
if __name__ == "__main__":
    unittest.main()
