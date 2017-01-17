counter = 3

def generate(max):
    numbers = []
    
    for i in range(max):
        max -= 1
        numbers += list(generate(max))
    
    for i in numbers:
        yield i

if __name__ == "__main__":
    for t in generate(3):
        print(t)