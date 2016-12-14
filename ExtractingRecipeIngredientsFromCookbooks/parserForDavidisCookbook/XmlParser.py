from parserForDavidisCookbook.Recipe import Recipe

rcpTagName = "cue:recipe"
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
        """ When rcpIds is an empty list, all recipes will be parsed.
            Otherwise only recipes, which have a in rcpIds specified rcp-id.
        """ 
        withAttris = {} if not rcpIds else {rcpIdTagName:rcpIds}
        for xmlRecipe in self.getElems(rcpTagName, withAttris):
            yield self.parseRecipe(xmlRecipe)
    
    def parseRecipe(self, xmlRecipe):
        rcpId = xmlRecipe.attributes[rcpIdTagName].value
        rcpType = xmlRecipe.attributes[typeTagName].value[:-1]  # remove . at the end
        name = self.getAllChildText(xmlRecipe.getElementsByTagName("head")[0])[:-1]  # remove . at the end
        instructions = self.getInstructions(xmlRecipe)
        
        return Recipe(rcpId, rcpType, name, instructions)
    
    def getInstructions(self, xmlRecipe):
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
            for k, possibleValues in withAttris.items():
                if elem.attributes[k].value not in possibleValues:
                    hasAllAttris = False
                    break
            if hasAllAttris:
                yield elem
    
    def getAllChildText(self, node):
        # " ".join(c.data.split() removes multiple whitespaces
        return " ".join([(" ".join(c.data.split()) if c.nodeType == node.TEXT_NODE else self.getAllChildText(c)).strip() for c in node.childNodes])
