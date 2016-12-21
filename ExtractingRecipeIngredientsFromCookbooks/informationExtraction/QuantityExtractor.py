
quantitiyWords = set(["ein, halb", "eine", "einige", "etwas"])

class QuantityExtractor(object):
    
    def getInformation(self, lemma):
        if isNumber(lemma):
            return True
        
        if "—" in lemma and isNumber(lemma.split("—")[0]):
            return True
        
        return False


def isNumber(s):
    if s.isnumeric(): # '¾'.isnumeric() -> True :)
        return True
        
    try: # 0.5.isnumeric() -> False oO therefore try also the cast to float
        float(s)
        return True
    except ValueError:
        pass
    
    if s in quantitiyWords:
        return True
        
    return False
