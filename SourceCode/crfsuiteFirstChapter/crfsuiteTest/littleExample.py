# from crfsuiteTest.crfsuiteTrainer import Trainer
import crfsuite
import sys

class Trainer(crfsuite.Trainer):
    def message(self, s):
        # Simply output the progress messages to STDOUT.
        sys.stdout.write(s)

if __name__ == '__main__':
    trainer = Trainer()  # Trainer("train.txt")
    trainer.select('l2sgd', 'crf1d')
    # trainer.trainModel()
