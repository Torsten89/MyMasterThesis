from informationExtraction.QuantityExtractor import str2Quantity

class WordProperty(object):
    quantity = "quantity"
    unit = "unit"
    ingredient = "ingredient" # self.properties["ingredient"] contains a list of model.IngredientCandi objects
    
    def __init__(self, word, lemma, properties):
        self.word = word
        self.lemma = lemma
        self.properties = properties
        
    def toXml(self, cueMLPrefix="cue:"):
        ingProp = self.properties.get(WordProperty.ingredient)
        
        if ingProp is None:
            return self.word
        else:
            return "<{}recipeIngredient {}>{}</{}recipeIngredient>".format(cueMLPrefix, self.attrisToXml(), self.word, cueMLPrefix)
    
    def attrisToXml(self):
        resultAttris = []
        
        quantity = self.properties.get(WordProperty.quantity)
        if quantity:
            if "—" in quantity:
                atLeastAtMost = quantity.split("—")
                resultAttris.append('atLeast="{}"'.format(str2Quantity(atLeastAtMost[0]))) 
                resultAttris.append('atMost="{}"'.format(str2Quantity(atLeastAtMost[1]))) 
            else:
                resultAttris.append('quantity="{}"'.format(str2Quantity(quantity))) 
                
        unit = self.properties.get(WordProperty.unit)
        if unit:
            resultAttris.append('unit="{}"'.format(unit))
        
        refCandis = [candi.xmlID for candi in self.properties.get(WordProperty.ingredient)]
        if refCandis:
            resultAttris.append('ref="{}"'.format(" ".join(["#"+candi for candi in refCandis])))
        
        # target    
        # optional
        # altGrp
            
        return " ".join(resultAttris)

    
    
        