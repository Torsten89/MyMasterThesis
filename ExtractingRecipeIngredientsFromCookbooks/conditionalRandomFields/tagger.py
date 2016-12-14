import crfsuite
from manualLabelHelper.getLabelledChunksFromFile import getLabelledChunksFromFile

def tagChunkedSentences(chunkedSentences, pathToModel):
    """ Each sentence is an iterator over its chunks
    """
    
    # swig (python interface for C) and yield/generator does not work
    # (see https://github.com/swig/swig/issues/559 and https://docs.python.org/3/library/exceptions.html#StopIteration )
    # Therefore collect labels in labelsOfSentences; each sentence produces a tuple of labels
    labelsOfSentences=[]
    
    tagger = crfsuite.Tagger()
    tagger.open(pathToModel)
    
    for chunkedSentence in chunkedSentences:
        featureSeq = crfsuite.ItemSequence() # all features of one word
        
        for chunk in chunkedSentence:
            features = crfsuite.Item()
            features.append(crfsuite.Attribute("w[0]={}".format(chunk))) # use only word identity so far
            featureSeq.append(features)
        tagger.set(featureSeq)
        labelsOfSentences.append(tagger.viterbi()) # tagger.viterbi() labels the current, through tagger.set(itemSeequence) set, sentence.

    return labelsOfSentences
        
if __name__ == '__main__':
    # flatten all labels to one list
    labelledChunks = list(getLabelledChunksFromFile("../manualLabelHelper/testRecipesB9.txt"))
    realLabels = [label for sentence in labelledChunks for word, label in sentence] 

    chunkedSentence = [[word for word, label in sentence] for sentence in labelledChunks]
    taggedSentences = tagChunkedSentences(chunkedSentence, "trained.model")
    # flatten all labels to one list
    taggedLabels = [tag for sentence in taggedSentences for tag in sentence]
    
    # flatten all words to one list
    words = [word for sentence in labelledChunks for word, label in sentence]
    
#     diffPositions = [i for i in range(len(words)) if taggedLabels[i] != realLabels[i]]
#     for i in range(len(diffPositions)):
#         print("{:20}{:20}{}".format(realLabels[diffPositions[i]], taggedLabels[diffPositions[i]], words[diffPositions[i]]))
#     print("Insgesamt {} Wörter, {} labels != 'O' und {} Unterschiede".format(len(words), len([1 for label in realLabels if label!="O"]), len(diffPositions)))

    for i in range(len(words)):
        print("{:20}{:20}{}".format(realLabels[i], taggedLabels[i], words[i]))
    