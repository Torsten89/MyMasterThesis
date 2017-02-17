from informationExtraction.QuantityExtractor import str2Quantity

class WordProperty(object):
    QUANTITY = "quantity"
    UNIT = "unit"
    INGREDIENT = "ingredient" # self.properties["ingredient"] contains a list of model.IngredientCandi objects
    OPTIONAL = "optional"
    ALT_GRP = "altGrp"
    
    def __init__(self, word, lemma, properties):
        self.word = word
        self.lemma = lemma
        self.properties = properties
        
    def toXml(self, cueMLPrefix="cue:"):
        ingProp = self.properties.get(WordProperty.INGREDIENT)
        
        if ingProp is not None:
            return "<{}recipeIngredient {}>{}</{}recipeIngredient>".format(cueMLPrefix, self.attrisToXml(), self.word, cueMLPrefix)
        elif self.properties.get(WordProperty.ALT_GRP):
            return '<{}alt target="{}"/>'.format(cueMLPrefix, " ".join(self.properties[WordProperty.ALT_GRP]))
        else:
            return self.word
    
    def attrisToXml(self):
        resultAttris = []
        
        quantity = self.properties.get(WordProperty.QUANTITY)
        if quantity:
            if "—" in quantity:
                atLeastAtMost = quantity.split("—")
                resultAttris.append('atLeast="{}"'.format(str2Quantity(atLeastAtMost[0]))) 
                resultAttris.append('atMost="{}"'.format(str2Quantity(atLeastAtMost[1]))) 
            else:
                resultAttris.append('quantity="{}"'.format(str2Quantity(quantity))) 
                
        unit = self.properties.get(WordProperty.UNIT)
        if unit:
            resultAttris.append('unit="{}"'.format(unit))
        
        refCandis = [candi.xmlID for candi in self.properties.get(WordProperty.INGREDIENT)]
        if refCandis:
            resultAttris.append('ref="{}"'.format(" ".join(["#"+candi for candi in refCandis])))
        
        if self.properties.get(WordProperty.OPTIONAL):
            resultAttris.append('optional="True"')
        
        altGrp = self.properties.get(WordProperty.ALT_GRP)
        if altGrp:
            resultAttris.append('altGrp="{}"'.format(altGrp))
            
        return " ".join(resultAttris)
    
    def __str__(self):
        return "Word: {}, lemma: {}, properties: {}".format(self.word, self.lemma, str(self.properties))

    
    
        