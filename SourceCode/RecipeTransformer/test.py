import crfsuite


if __name__ == '__main__':
    r = ['H', '2', 'O']
    replacements = [(index, int(ch)) for index, ch in enumerate(r) if ch.isdigit()]
    
    for postion, times in replacements:
        r[postion] = (times - 1) * r[postion - 1]
    
    # flaten the result
    r = [ch for s in r for ch in s]
    
    print(r)
    print(crfsuite.version())
