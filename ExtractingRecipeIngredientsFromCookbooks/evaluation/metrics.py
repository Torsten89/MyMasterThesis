
def recall(numberRelevantAndRetieved, numberRelevant):
    """ Metric for how many of the retrieved values are relevant.
        Returns 1 if numberRelevant is 0.
        (numberRelevantAndRetieved / numberRelevant)
    """
    if numberRelevant == 0:
        return 1
    
    return numberRelevantAndRetieved / numberRelevant

def precision(numberRetievedAndRelevant, numberRetrieved):
    """ Metric for how many of the relevant values were retrieved. (numberRetievedAndRelevant / numberRetrieved) """
    if numberRetrieved == 0:
        if numberRetievedAndRelevant == 0: return 1
        else: return 0
        
    return numberRetievedAndRelevant / numberRetrieved
