from xml.dom import minidom
from parserForDavidisCookbook.XmlParser import XmlParser

targetCookbook = "/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/recipes_cueML_v0.5.xml"
targetRecipes = ["B-16"] 

def writeChunksToFile(cookbook, fileName, rcpIds=[]):
    parser = XmlParser(minidom.parse(targetCookbook))
    recipes = parser.getRecipes(rcpIds)
    
    with open(fileName, "x") as f:
        for recipe in recipes:
            for chunk in recipe.chunk():
                f.write(chunk)
    

if __name__ == '__main__':
    writeChunksToFile(targetCookbook, "labelMe.txt", targetRecipes)
    