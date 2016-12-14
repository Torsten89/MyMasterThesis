from xml.dom.minidom import parseString
listIngredientTag = "cue:listIngredient"
ingredientTag = "cue:ingredient"

def buildIngDict(dom):
    listIngredient = dom.getElementsByTagName(listIngredientTag)[0]
    for ing in listIngredient.getElementsByTagName(ingredientTag):
        xmlId = ing.attributes["xml:id"].value
        basicForms = [ing.getElementsByTagName("cue:prefBasicForm")[0].data]
        for altBasicForm in ing.getElementsByTagName("cue:altBasicForm"):
            basicForms.append(altBasicForm.data)
        BLSref = ing.attributes["BLSref"].value
        comment = ing.getElementsByTagName("cue:note").data
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
</cue:listIngredient>')
    
    buildIngDict(dom)