import crfsuite

if __name__ == '__main__':
    tagger = crfsuite.Tagger()
    tagger.open("lillteExample.model")
    
    with open("test.txt", "r") as fil:
        xseq = crfsuite.ItemSequence()
        
        for line in fil:
            # An empty line presents an end of a sequence and every line ends with '\n'
            line = line.strip()
            if not line:
                tagger.set(xseq)
                labels = tagger.viterbi()
                for t, y in enumerate(labels):
                    print(y)  # print(y, tagger.marginal(y, t))
                print()
                xseq = crfsuite.ItemSequence()
                continue
            
            fields = line.split('\t')
            item = crfsuite.Item()  # item contains all features of one x
            for field in fields[1:]:
                item.append(crfsuite.Attribute(field))
            xseq.append(item)
            
        tagger.set(xseq)
        labels = tagger.viterbi()
        for t, y in enumerate(labels):
            print(y, tagger.marginal(y, t))
        print()
        xseq = crfsuite.ItemSequence()
