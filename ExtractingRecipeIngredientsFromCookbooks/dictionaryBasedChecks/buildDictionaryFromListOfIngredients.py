from xml.dom.minidom import parseString
from parserForDavidisCookbook.xmlHelper import getAllChildText

def buildIngDict(dom):
    listIngredient = dom.getElementsByTagName("cue:listIngredient")[0]
    for ingElem in listIngredient.getElementsByTagName("cue:ingredient"):
        xmlId = ingElem.attributes["xml:id"].value
        basicForms = [getAllChildText(ingElem.getElementsByTagName("cue:prefBasicForm")[0])]
        for altBasicForm in ingElem.getElementsByTagName("cue:altBasicForm"):
            basicForms.append(getAllChildText(altBasicForm))
        BLSref = ingElem.attributes["BLSref"].value
        comment = ""
        for c in ingElem.getElementsByTagName("cue:note"):
            comment += getAllChildText(c)
        print(xmlId, basicForms, BLSref, comment)

class Ingredient:
    def __init__(self, xmlId, basicForms, BLSref="", comment=""):
        self.xmlId = xmlId
        self.basicForms = basicForms
        self.BLSref = BLSref
        self.comment = comment

if __name__ == '__main__':
    dom = parseString('<cue:listIngredient xmlns="http://www.tei-c.org/ns/1.0" xmlns:cue="http://cueML/ns"> \
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
    </cue:ingredient> \
</cue:listIngredient>')
    
    buildIngDict(dom)