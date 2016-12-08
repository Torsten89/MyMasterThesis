from xml.dom import minidom
from parserForDavidisCookbook.XmlParser import XmlParser

targetCookbook = "/home/torsten/Desktop/MyMasterThesis/DavidisKochbuch/recipes_cueML_v0.5.xml"
targetRecipes = ["B-16"] # empty means all, else the containing rcp-ids

def writeChunksToFile(cookbook, fileName, rcpIds=[]):
    """ cookbook is path to the xml-file of the book
    """
    parser = XmlParser(minidom.parse(targetCookbook))
    recipes = parser.getRecipes(rcpIds)
    
    with open(fileName, "w") as f:
        for recipe in recipes:
            f.write("#{}\n".format(recipe.rcpId))
            for chunk in recipe.chunksWithNewlines():
                f.write(chunk)
            f.write("\n")
        
    

if __name__ == '__main__':
    # write chunks for training data
    trainingRecipes = ["B-{}".format(i) for i in range(1,9)] + ["B-16"]
    writeChunksToFile(targetCookbook, "trainingRecipes.txt", trainingRecipes)
    # write chunks for test data
    testRecipes = ["B-9"]
    writeChunksToFile(targetCookbook, "testRecipes.txt", testRecipes)
    print("finish")