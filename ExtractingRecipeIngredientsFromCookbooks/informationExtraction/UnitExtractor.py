from parserForDavidisCookbook.xmlHelper import getUnitValuesFromCueML

class UnitExtractor(object):

    def __init__(self, cueMLRngDom):
        self.__unitSet__ = set(unit for unit in getUnitValuesFromCueML(cueMLRngDom))
        
    def getUnit(self, lemma, default=None):
        if lemma in self.__unitSet__:
            return lemma
        
        if lemma == "Eßlöffel" or lemma == "Löffel":
            return "EL"
        
        return default
    