import crfsuite
import os.path
import sys
from manualLabelHelper.getLabelledChunksFromFile import getLabelledChunksFromFile


class Trainer(crfsuite.Trainer):        

    # @override
    def message(self, s):
        sys.stdout.write(s)

    def readModelParameter(self, parameter):
        """ Parameter is a iterator over sentences.
            Each sentence is a list of the form [(word1, label1), (word2, label2), ...]
        """
        for sentence in parameter:
            labelSeq = crfsuite.StringList()
            featureSeq = crfsuite.ItemSequence()
            
            for word, label in sentence:
                labelSeq.append(label)
                
                features = crfsuite.Item()  # item contains all features of one label
                features.append(crfsuite.Attribute("w[0]={}".format(word)))
                featureSeq.append(features) # only use word identity so far
            
            self.append(featureSeq, labelSeq, 0)  # add to training data  

    def trainModel(self, parameter, modelName="trained.model"):
        # Use L2-regularized SGD and 1st-order dyad features (bigram features).
        self.select('l2sgd', 'crf1d')
        # Set the coefficient for L2 regularization to 0.1
        self.set('c2', '0.1')
        # also feature with negative values
        self.set("feature.possible_states", "1")
    
        self.readModelParameter(parameter)
                 
        self.train(modelName, -1)

if __name__ == '__main__':
    trainer = Trainer()
    trainer.trainModel(getLabelledChunksFromFile("../manualLabelHelper/trainingRecipes9.txt"))
