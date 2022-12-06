# mjqjpqmgbljsphdztnvjfqwrcgsmlb  prima sequenza di 4 caratteri diversi dopo aver ricevuto 7 caratteri (quindi i 4 caratteri prima)

with open('input.txt') as infile:
    line = infile.read().strip()

# print(line)

def f1(riga):

    for i in range(len(riga)-4):
        if len(set(riga[i:i+4])) == 4:
            return i+4
        
    return -1

def f2(riga):

    for i in range(len(riga)-14):
        if len(set(riga[i:i+14])) == 14:
            return i+14
        
    return -1

print(f1(line))
print(f2(line))

