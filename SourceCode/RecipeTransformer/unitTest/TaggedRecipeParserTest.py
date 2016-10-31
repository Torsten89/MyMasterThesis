import unittest
from xml.dom.minidom import parseString
from TaggedRecipeParser import TaggedRecipeParser

def createCueMLDom(recipes=[], spans=[]):
    return parseString('<TEI xmlns="http://www.tei-c.org/ns/1.0" xmlns:cue="http://cueML/ns"> \
                <teiHeader>...</teiHeader> \
                <text> \
                    <body>' \
                        + '\n'.join(recipes) \
                        + ' \
                        <spanGrp>' \
                            + '\n'.join(spans) + '\
                        </spanGrp> \
                    </body> \
                </text> \
            </TEI>')

def getRecipeB49():
    return ' \
        <cue:recipe type="Suppen." rcp-id="B-49"> \
            <head>Suppe von feiner Gerste (Graupen).</head> \
             \
            <p>Ungefähr <cue:cookTime dur-iso="PT2H">zwei Stunden</cue:cookTime> muß die \
                  <cue:recipeIngredient>Gerste</cue:recipeIngredient> zu Feuer sein. Sie wird mit \
               etwas <cue:recipeIngredient>Butter</cue:recipeIngredient> in wenig weiches kochendes \
               Wasser gegeben, kurz eingekocht, frische \
                  <cue:recipeIngredient>Milch</cue:recipeIngredient> hinzu geschüttet und zu einer \
               sämigen Suppe gekocht. <cue:recipeIngredient>Salz</cue:recipeIngredient>, \
                  <cue:recipeIngredient>Zucker</cue:recipeIngredient> und \
                  <cue:recipeIngredient>Zimmet</cue:recipeIngredient> darf nicht darin fehlen. \
            </p> \
         </cue:recipe>'
         
def getRecipeB2():
    return ' \
        <cue:recipe type="Suppen." rcp-id="B-2"> \
            <head><cue:recipeIngredient reference="#B-1">Rindfleischsuppe</cue:recipeIngredient> mit Perlgerste und Reis.</head> \
             \
            <p>Wird gekocht wie die vorhergehende<link target="#B-1"/>, nur mit der \
               Abänderung, daß, wenn die Brühe durch ein Haarsieb geschüttet ist, man \
               verhältnißmäßig 1—2 Eßlöffel voll <cue:recipeIngredient quantity="1-2" unit="Eßlöffel" \
                  >Mehl</cue:recipeIngredient> mit frischer \
                  <cue:recipeIngredient>Butter</cue:recipeIngredient> <cue:cookingMethod>durchschwitzt</cue:cookingMethod>, welches jedoch \
               weiß bleiben muß, und die vom Bodensatz abgeklärte Brühe hinzuschüttet. Zugleich gibt \
               man feine <cue:recipeIngredient>Gerste</cue:recipeIngredient> nebst etwas \
                  <cue:recipeIngredient>Wurzelwerk</cue:recipeIngredient> in die Suppe, später auch \
                     <cue:recipeOptionalIngredient>Spargel</cue:recipeOptionalIngredient>, \
                     <cue:recipeOptionalIngredient>Blumenkohl</cue:recipeOptionalIngredient> oder \
                     <cue:recipeOptionalIngredient>Scorzonerwurzeln</cue:recipeOptionalIngredient>, \
               was die Jahreszeit bietet, und vor dem Anrichten die \
                  <cue:recipeIngredient>Herzblättchen der Sellerieknollen</cue:recipeIngredient> und \
               beliebige <cue:recipeIngredient>Klöße</cue:recipeIngredient>. Man rührt die Suppe mit 1—2 <cue:recipeIngredient quantity="1-2" \
                  >Eidotter</cue:recipeIngredient> ab, indem man solche mit etwas Wasser zerrührt, \
               und unter fortwährendem Rühren die kochende Suppe hinzu gibt. Sie muß gebunden, nur \
               ja nicht zu sämig sein. </p> \
            \
            <note>Anmerk. Will man <cue:recipeOptionalIngredient quantity="1" unit="Eßlöffel" \
                  >Reis</cue:recipeOptionalIngredient> oder <cue:recipeOptionalIngredient unit="Eßlöffel" quantity="1" \
                  >Sago</cue:recipeOptionalIngredient> zur Suppe nehmen, so gibt man dieses später hinein. \
               Man rechnet davon auf jede Person bei allen Fleischsuppen einen gestrichenen Eßlöffel \
               voll. </note> \
         </cue:recipe>'

class TaggedRecipeParserTest(unittest.TestCase):
        
    def testFindRecipesInDom(self):
        dom = createCueMLDom([getRecipeB49()])
        self.assertEqual(1, len(TaggedRecipeParser(dom).getRecipes()))

    def testParseRecipe(self):
        dom = createCueMLDom([getRecipeB49()])
        recipe = TaggedRecipeParser(dom).getRecipes()[0]
        self.assertEqual("Suppen", recipe.recipeType)
        self.assertEqual("B-49", recipe.rcpId)
        self.assertEqual("Suppe von feiner Gerste (Graupen)", recipe.name)
        # self.assertEqual(first, second, msg)
        
    def testTagInHead(self):
        dom = createCueMLDom([getRecipeB2()])
        recipe = TaggedRecipeParser(dom).getRecipes()[0]
        self.assertEqual("Rindfleischsuppe mit Perlgerste und Reis", recipe.name)
        
if __name__ == "__main__":
    unittest.main()
