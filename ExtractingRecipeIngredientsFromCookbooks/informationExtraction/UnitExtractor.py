from parserForDavidisCookbook.xmlHelper import getUnitValuesFromCueML
from xml.dom.minidom import parse

class UnitExtractor(object):

    def __init__(self, cueMLRngDom):
        self.__unitSet__ = set(unit for unit in getUnitValuesFromCueML(cueMLRngDom))
        
    def getInformation(self, lemma, default=None):
        if lemma in self.__unitSet__:
            return lemma
        
        return default


if __name__ == '__main__':
    dom = parse("/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/cueML/cueML_v0.5.rng")
    uE = UnitExtractor(dom)
    print(uE.__unitSet__)