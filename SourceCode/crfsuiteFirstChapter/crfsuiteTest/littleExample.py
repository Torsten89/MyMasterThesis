from crfsuiteTest.crfsuiteTrainer import Trainer

if __name__ == '__main__':
    trainer = Trainer("train.txt")  # Trainer("train.txt")
    trainer.trainModel()
