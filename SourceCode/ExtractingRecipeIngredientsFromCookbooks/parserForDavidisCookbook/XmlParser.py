from parserForDavidisCookbook.Recipe import Recipe

recipeTagName = "cue:recipe"
rcpIdTagName = "rcp-id"
typeTagName = "type"

class XmlParser(object):

    def __init__(self, dom):
        ''' 
            It is assumed that the XML has the following TEI-format:
        
            <TEI>
                <teiHeader>...</teiHeader>
                <text>
                    <body>
                        <cue:recipe type="Suppen." rcp-id="B-8">
                            <head>Suppe von Midder (Kalbsmilch).</head>
                            
                            <p> Das Midderwird nach A. No. 16 vorgerichtet, in kleine Würfel geschnitten und...</p>
                       </cue:recipe>
                       <cue:recipe>...</cue:recipe>
                       .
                       .
                       .
                    </body>
                </text>
            </TEI>
        '''
        self.dom = dom

    def getRecipes(self, rcpIds=[]):
        withAttris = {} if not rcpIds else {"rcp-id":rcpIds}
        for xmlRecipe in self.getElems(recipeTagName, withAttris):
            yield self.parseRecipe(xmlRecipe)
    
    def parseRecipe(self, xmlRecipe):
        rcpId = xmlRecipe.attributes[rcpIdTagName].value
        recipeType = xmlRecipe.attributes[typeTagName].value[:-1]  # remove . at the end
        head = self.getAllChildText(xmlRecipe.getElementsByTagName("head")[0])[:-1]  # remove . at the end
        instructions = self.getInstructions(xmlRecipe, head)
        
        return Recipe(rcpId, recipeType, head, instructions)
    
    def getInstructions(self, xmlRecipe, head):
        return "\n".join([self.getAllChildText(p) for p in xmlRecipe.getElementsByTagName("p")] \
            + [self.getAllChildText(note) for note in xmlRecipe.getElementsByTagName("note")] \
        )
        
        
    """ Underneath only helper methods
    """        
    
    def getElems(self, elemName, withAttris={}):
        """ withAttris = {key: iterator with possible values}
        """
        for elem in self.dom.getElementsByTagName(elemName):
            hasAllAttris = True
            for k, v in withAttris.items():
                if elem.attributes[k].value not in v:
                    hasAllAttris = False
                    break
            if hasAllAttris:
                yield elem
    
    def getAllChildText(self, node):
        # " ".join(c.data.split() removes multiple whitespaces
        return " ".join([(" ".join(c.data.split()) if c.nodeType == node.TEXT_NODE else self.getAllChildText(c)).strip() for c in node.childNodes])
