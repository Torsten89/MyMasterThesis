from xml.dom.minidom import parseString
import unittest
from parserForDavidisCookbook.xmlHelper import buildIngredientDict


class XmlHelperTest(unittest.TestCase):

    def testMidder(self):
        dom = parseString(' \
<cue:listIngredient xmlns="http://www.tei-c.org/ns/1.0" xmlns:cue="http://cueML/ns"> \
    <cue:ingredient xml:id="Rindkochfleisch" BLSref="U180100"> \
        <cue:prefBasicForm>Rindfleisch</cue:prefBasicForm> \
    </cue:ingredient> \
    <cue:ingredient xml:id="Wurzelwerk" BLSref="G600000"> \
        <cue:prefBasicForm>Wurzelwerk</cue:prefBasicForm> \
        <cue:note>Another possible value for BLSref is "X560003"</cue:note> \
    </cue:ingredient> \
    <cue:ingredient xml:id="Midder" BLSref="V582100"> \
        <cue:prefBasicForm>Midder</cue:prefBasicForm> \
        <cue:altBasicForm>Kalbsmidder</cue:altBasicForm> \
        <cue:altBasicForm>Bries</cue:altBasicForm> \
        <cue:altBasicForm>Kalbsmilch</cue:altBasicForm> \
        <cue:note>"Kalbsmidder ist auch unter dem Synonym: Bries, Kalbsmilch bekannt. Kalbsmilch ist die Thymusdrüse des Kalbes. 100 g frische Kalbsmilch enthalten 99,8 kcal, 3,4 g Fett, 17,2 g Eiweiß, 77,8 g Wasser, 1,91 mg Eisen, 268 mg Cholesterin und 0,42 g Purine. Dieses Organ ist bei Jungtieren voll entwickelt. Bei erwachsenen Tieren bildet sich das Organ zurück. Kalbsmilch wird zur Herstellung von Spezialitäten, wie Suppen, Klöße und Ragout, verwendet." (http://www.cosmiq.de/qa/show/70827/was-ist-kalbsmidder/)</cue:note> \
        <cue:note>2. Note</cue:note> \
    </cue:ingredient> \
</cue:listIngredient>')
                    
        d = buildIngredientDict(dom)
        self.assertIsNotNone(d.get("Bries"))
        self.assertEqual(1, len(d.get("Bries")))
        self.assertEqual("Midder", d["Bries"][0].xmlID)
        
    def testWein(self):
        dom = parseString(' \
<cue:listIngredient xmlns="http://www.tei-c.org/ns/1.0" xmlns:cue="http://cueML/ns"> \
    <cue:ingredient xml:id="Rotwein" BLSref="P240000"> \
        <cue:prefBasicForm>Rotwein</cue:prefBasicForm> \
        <cue:altBasicForm>roter Wein</cue:altBasicForm> \
    </cue:ingredient> \
    <cue:ingredient xml:id="Weißwein" BLSref="P220000"> \
        <cue:prefBasicForm>Weißwein</cue:prefBasicForm> \
        <cue:altBasicForm>weißer Wein</cue:altBasicForm> \
    </cue:ingredient> \
</cue:listIngredient>')
        
        d = buildIngredientDict(dom)
        self.assertIsNotNone(d.get("Wein"))
        self.assertEqual(2, len(d.get("Wein")))
        self.assertEqual("Rotwein", d["Wein"][0].xmlID)
        self.assertEqual("roter Wein", d["Wein"][0].basicForm)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()