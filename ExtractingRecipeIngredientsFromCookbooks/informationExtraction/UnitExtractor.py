from parserForDavidisCookbook.xmlHelper import getUnitValuesFromCueML

class UnitExtractor(object):

    def __init__(self, cueMLRngDom):
        self.__unitSet__ = set(["kg",
                                "Pfund",
                                "Loth",
                                "Stich",
                                "Messerspitze",
                                "Pfennig", "EL",
                                "Teelöffel",
                                "Tasse",
                                "l",
                                "Maß",
                                "Flasche",
                                "Glas",
                                "Scheibe"
        ])
        
    def getUnit(self, lemma, default=None):
        if lemma in self.__unitSet__:
            return lemma
        
        if lemma == "Eßlöffel" or lemma == "Löffel":
            return "EL"
        
        return default
    