import os.path

def getManualCreatedListOfDavidisIngredients():
    with open(os.path.dirname(os.path.abspath(__file__))+"/manualCreatedListOfDavidisIngredients.txt" , 'r') as f:
        return [line.split()[1] for line in f.readlines() if not line.startswith("#")]

if __name__ == '__main__':
    print(getManualCreatedListOfDavidisIngredients())