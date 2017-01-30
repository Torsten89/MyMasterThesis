from evaluation.comparator import ingInGoldenStandardIngsExactMatch, ingInGoldenStandardIngsRoughMatch

def recallOf2Recipes(goldenStandardIngsOfRcp, ingsOfRcp, attris):
    relevant = len(goldenStandardIngsOfRcp)
    retrievedAndRelevant = 0
    
    for ing in goldenStandardIngsOfRcp:
        if ingInGoldenStandardIngsExactMatch(ing, ingsOfRcp, attris):
            retrievedAndRelevant += 1
        else:
            print("Not retrieved: {}".format(ing))
            
    return retrievedAndRelevant, relevant

def precisionOf2Recipes(goldenStandardIngsOfRcp, retrievedIngs, attris):
    retrieved = len(retrievedIngs)
    retrievedAndRelevant = 0
    
    for ing in retrievedIngs:
        if ingInGoldenStandardIngsRoughMatch(ing, goldenStandardIngsOfRcp, retrievedIngs, attris):
            retrievedAndRelevant += 1
        else:
            print("Not relevant but retrieved: {}".format(ing))
            
    return retrievedAndRelevant, retrieved