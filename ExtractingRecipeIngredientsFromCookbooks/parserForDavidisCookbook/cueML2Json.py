from parserForDavidisCookbook.XmlParser import XmlParser,\
    parseXml2PlainTextRecipe, getIngsFromNode
from xml.dom.minidom import parse
import json
from parserForDavidisCookbook.xmlHelper import getElems

def getJsonRcps(pathToCueMLFile):
    dictRcps = dict()
    
    xmlRcps = (XmlParser(parse(pathToCueMLFile))).getXmlRecipes(["B-16"])
    for xmlRcp in xmlRcps:
        dictRcp = xmlRcp2dictRcp(xmlRcp)
        t = dictRcp["type"]
        if t in dictRcps: dictRcps.append(dictRcp)
        else: dictRcps[t] = [dictRcp]

    return json.dumps(dictRcps)

def xmlRcp2dictRcp(xmlRcp):
    plainTextRcp = parseXml2PlainTextRecipe(xmlRcp)
    dictRcp = dict()
    
    dictRcp["rcp-id"] = plainTextRcp.rcpId
    dictRcp["type"] = plainTextRcp.rcpType
    dictRcp["name"] = plainTextRcp.name
    dictRcp["instructions"] = plainTextRcp.instructionSentences
    dictRcp["ingredients"] = mergeIngs(getIngsFromNode(xmlRcp))
    dictRcp["cueAlt"] = [altElems.attributes["target"].value.split() for altElems in getElems(xmlRcp, "cue:alt")]
        
    return dictRcp

def mergeIngs(ings):
    newIngs = []
    for ing in ings:
        if "ref" not in ing.__dict__:
            newIngs.append(ing)
            continue
        
        ref = ing.__dict__["ref"]
        added = False
        for iPrime in newIngs:
            if "ref" not in iPrime.__dict__:
                continue
            else:
                if ref == iPrime.__dict__["ref"]:
                    iPrime.__dict__.update (ing.__dict__)
                    added = True
                    break
        if not added:
            newIngs.append(ing)
            
    return [i.__dict__ for i in newIngs]
                    
                    
            

if __name__ == '__main__':
    pathToCueMLFile = "/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/recipes extracted.xml"
     
    print(getJsonRcps(pathToCueMLFile))
    
    
    
    