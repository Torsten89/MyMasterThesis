import unicodedata

#not really good cause of things like "ein Paar", "schüttet es durch ein Sieb"... -.-
quantityWords = {"einige":"einige", "etwas":"etwas",
                 "ein":"1", "eine":"1",
                 "zwei":"2",
                 "drei":"3",
                 "vier":"4",
                 "fünf":"5",
                 "sechs":"6",
                 "sieben":"7",
                 "acht":"8",
                 "neun":"9",
                 "zehn":"10",
                 "elf":"11",
                 "zwölf":"12"}

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
    
    if s.lower() in quantityWords:
        return True
        
    return False

def str2Quantity(s):
    try:
        s = str(float(s))
        if s.endswith(".0"): return s[:-2] # is int
        else: return s
    except:
        pass # is unicode fraction or in quantityWords
    
    if s.isnumeric():
        frac = unicodedata.numeric(s[-1])
        if len(s)>1: return s[:-1] + "."+ str(frac)[2:]
        else: return str(frac)
    else:
        return quantityWords[s.lower()]
