
class Ingredient:

    def __init__(self, ref=None, target=None, quantity=None, atLeast=None, atMost=None, unit=None,
                 altGrp=None, optional=None, dontUse=None, ingYield=None, ingYieldUnit = None):
        """ See definition of cueML for meaning of these attributes # ToDo link to definition
        """
        self.ref = ref
        self.target = target
        self.quantity = quantity
        self.atLeast = atLeast
        self.atMost = atMost
        self.unit = unit
        self.altGrp = altGrp
        self.optional = optional
        self.dontUse = dontUse
        
    
    def __eq__(self, other):
#         for k, v in self.__dict__.items():
#             if v != other.__dict__[k]:
#                 print(k, v)
#                 print(k, other.__dict__[k])
             
        return self.__dict__ == other.__dict__ # compares all attris cause classes are basically dicts in python :)
    
    def __str__(self):
        entries = []
        for prop, value in self.__dict__.items():
            if value:
                entries.append("{}={}".format(prop, value))
                
        return ", ".join(entries)