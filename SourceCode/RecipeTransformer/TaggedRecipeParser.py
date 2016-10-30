class TaggedRecipeParser(object):

    def __init__(self, dom):
        ''' 
            It is assumed that the XML is valid against cueMLv2.rng
            and therefore has the following form:
        
            <TEI>
                <teiHeader>...</teiHeader>
                <text>
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
                </text>
            </TEI>
        '''
        self.dom = dom
        
    def getRecipes(self):
        xmlRecipes = self.dom.getElementsByTagName("recipe")
        return xmlRecipes