labels = ["O",
          "B-Ingredient", "I-Ingredient", 
          "B-Quantity", "I-Quantity",
          "B-Unit", "I-Unit",
          "B-Link", "I-Link",
          "B-Yield", "I-Yield",
          "B-CookTime", "I-CookTime",
          "B-IngredientYield", "I-IngredientYield"]

def getLabelledChunksFromFile(pathToFile):
    """ yields per sentence from file [(word1, label1), (word2, label2), ... ]
    """
    with open(pathToFile, "r") as f:
        labelsOfSentence = []
        for line in f.read().splitlines():
            if not line: # empty line indicates end of sentence
                yield labelsOfSentence
                labelsOfSentence = []
                continue

            if line.startswith("#"): # is a comment
                continue
            else:
                try:
                    word, label = line.split("\t")
                except ValueError:
                    raise ValueError("in: '{}'".format(line))
                if label not in labels:
                    raise Exception("{} is not an allowed label".format(label))
                labelsOfSentence.append((word, label))
                

if __name__ == '__main__':
    labelledChunks = getLabelledChunksFromFile("labelMe.txt")
    for labelledChunk in labelledChunks:
        print(labelledChunk)