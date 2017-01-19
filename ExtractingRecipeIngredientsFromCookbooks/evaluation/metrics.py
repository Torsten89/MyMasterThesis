
def recall(numberRelevantAndRetieved, numberRelevant):
    """ Metric for how many of the retrieved values were relevant.
        returns 1 if numberRelevant is 0.
    """
    if numberRelevant == 0:
        return 1
    
    return numberRelevantAndRetieved / numberRelevant

def precision(numberRelevantAndRetieved, numberRetrieved):
    """ Metric for how many of the relevant values were retrieved. """
    return numberRelevantAndRetieved / numberRetrieved
