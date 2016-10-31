from model.Recipe import Recipe

class TaggedRecipeParser(object):

    def __init__(self, dom):
        ''' 
            It is assumed that the XML is valid against cueMLv2.rng
            and therefore has the following form:
        
            <TEI>
                <teiHeader>...</teiHeader>
                <instructions>
                    <body>
                        <cue:recipe type="Suppen." rcp-id="B-8">
                            <head>Suppe von Midder (Kalbsmilch).</head>
                            
                            <p> Das <cue:recipeIngredient>Midder</cue:recipeIngredient> wird nach
                                A. No. 16<link target="#A-16"/> vorgerichtet,
                                in kleine Würfel geschnitten und...
                            </p>
                       </cue:recipe>
                       .
                       .
                       .
                       <spanGrp>
                           <span xml:id="Bouillon" from="#Bouillon-start" to="#Bouillon-end">
                               Bouillon
                            </span>
                            .
                            .
                            .
                        </spanGrp>
                    </body>
                </instructions>
            </TEI>
        '''
        self.dom = dom
        

    def getRecipes(self):
        xmlRecipes = self.dom.getElementsByTagName("cue:recipe")
        return [self.parseRecipe(xmlRecipe) for xmlRecipe in xmlRecipes]
    
    def parseRecipe(self, xmlRecipe):
        rcpId = xmlRecipe.attributes["rcp-id"].value
        recipeType = xmlRecipe.attributes["type"].value[:-1]  # remove . at the end
        name = self.getAllChildText(xmlRecipe.getElementsByTagName("head")[0])[:-1]  # remove . at the end
        instructions = self.getInstructions(xmlRecipe)
        ingredients = self.getIngredients(xmlRecipe)
        
        return Recipe(recipeType, rcpId, name, instructions, ingredients)
    
    def getInstructions(self, xmlRecipe):
        return "".join([p.toxml() for p in xmlRecipe.getElementsByTagName("p")] \
                       + ["<p>" + note.toxml() + "</p>" for note in xmlRecipe.getElementsByTagName("note")])
        
    def getIngredients(self, xmlRecipe):
        """ - Get don't use ingredients (from links, ingredients)?
            - Get ingredients from includes (links, ingredients)?
                - Überschreiben der inkludierten ingrs?
            - Get ingredients and altIngredients
            - Get optIngredients
            
            B-4
        """
        pass
        
            
    def getAllChildText(self, node):
        return "".join([c.data if c.nodeType == node.TEXT_NODE else self.getAllChildText(c) for c in node.childNodes])
