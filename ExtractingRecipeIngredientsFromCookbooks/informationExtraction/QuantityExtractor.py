import unicodedata

#Caution with something like "ein Paar"!
quantityWords = {"ein":"1", "eine":"1", "einige":"einige", "etwas":"etwas"}

def isQuantity(lemma):
    if isNumber(lemma):
        return True
    
    if "—" in lemma and isNumber(lemma.split("—")[0]):
        return True
    
    return False


def isNumber(s):
    if s.isnumeric(): # '¾'.isnumeric() -> True :)
        return True
        
    try: # "0.5".isnumeric() -> False oO therefore try also the cast to float
        float(s)
        return True
    except ValueError:
        pass
    
    if s in quantityWords:
        return True
        
    return False

def str2Quantity(s):
    try: return float(s)
    except: pass # is unicode fraction or in quantityWords
    
    if s.isnumeric():
        frac = unicodedata.numeric(s[-1])
        if len(s)>1: return str2Quantity(frac) + str2Quantity(s[:-1])
        else: return frac
    else:
        return quantityWords[s]
