class WordProperty(object):
    quantity = "quantity"
    unit = "unit"
    ingredient = "ingredient"
    
    def __init__(self, word, lemma, properties):
        self.word = word
        self.lemma = lemma
        self.properties = properties
        
    def toXml(self):
        ingProp = self.getProperty(WordProperty.ingredient)
        
        if not ingProp:
            return self.word
        else:
            return "<recipeIngredient {}>{}</recipeIngredient>".format(self.attrisToXml(), self.lemma)
    
    def attrisToXml(self):
        resultAttris = []
        
        quantity = self.properties.get(WordProperty.quantity)
        if quantity:
            if "—" in quantity:
                atLeastAtMost = quantity.split("—")
                resultAttris.append("atLeast={}".format(atLeastAtMost[0])) 
                resultAttris.append("atMost={}".format(atLeastAtMost[1])) 
            else:
                resultAttris.append("quantity={}".format(quantity)) 
                
        unit = self.properties.get(WordProperty.unit)
        if unit:
            resultAttris.append("unit={}".format(unit))
        
        refCandis = [candi.xmlID for candi in self.properties.get(WordProperty.ingredient)]
        if refCandis:
            resultAttris.append("ref={}".format(" ".join(["#"+candi for candi in refCandis])))
        
        # target    
        # optional
        # altGrp
            
        return " ".join(resultAttris)
        