
def recall(numberRelevantAndRetieved, numberRelevant):
    """ Metric for how many of the retrieved values are relevant.
        Returns 1 if numberRelevant is 0.
    """
    if numberRelevant == 0:
        return 1
    
    return numberRelevantAndRetieved / numberRelevant

def precision(numberRelevantAndRetieved, numberRetrieved):
    """ Metric for how many of the relevant values were retrieved. """
    if numberRetrieved == 0:
        if numberRelevantAndRetieved == 0: return 1
        else: return 0
        
    return numberRelevantAndRetieved / numberRetrieved
