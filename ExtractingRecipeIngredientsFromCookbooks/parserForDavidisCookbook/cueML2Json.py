from parserForDavidisCookbook.XmlParser import XmlParser,\
    parseXml2PlainTextRecipe, getIngsFromNode
from xml.dom.minidom import parse
import json
from parserForDavidisCookbook.xmlHelper import getElems

def getJsonRcps(pathToCueMLFile, rcpIds):
    dictRcps = dict()
    
    xmlRcps = (XmlParser(parse(pathToCueMLFile))).getXmlRecipes(rcpIds)
    for xmlRcp in xmlRcps:
        dictRcp = xmlRcp2dictRcp(xmlRcp)
        t = dictRcp["type"]
        print(dictRcp)
        if t in dictRcps: dictRcps[t].append(dictRcp)
        else: dictRcps[t] = [dictRcp]

    return json.dumps(dictRcps)

def xmlRcp2dictRcp(xmlRcp):
    plainTextRcp = parseXml2PlainTextRecipe(xmlRcp)
    dictRcp = dict()
    
    dictRcp["rcp-id"] = plainTextRcp.rcpId
    dictRcp["type"] = plainTextRcp.rcpType.replace("_", " ")
    dictRcp["name"] = plainTextRcp.name
    dictRcp["instructions"] = plainTextRcp.instructionSentences
    dictRcp["ingredients"] = mergeIngs(getIngsFromNode(xmlRcp))
    dictRcp["cueAlts"] = [altElems.attributes["target"].value.split() for altElems in getElems(xmlRcp, "cue:alt")]
        
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
                    
                    
            
# Wurstmachen,_Einpöckeln_und_Räuchern_des_Fleisches
if __name__ == '__main__':
    pathToCueMLFile = "/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/recipes extracted.xml"
    pathToErg = "/home/torsten/Desktop/MyMasterThesis/docs/Rezepte/Rezepte.json"
    with open(pathToErg, "w") as f:
        f.write("rcps={}".format(getJsonRcps(pathToCueMLFile, []))) 

    #print(json.dumps({"a b c":"hi"}))
        
   # print(getJsonRcps(pathToCueMLFile, [B-16]))
    
    
    
    