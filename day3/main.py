
import random

lines = None

# with open("./big.txt", "w+") as f:
#     for i in range(10000):
#         str = ""
#         same = chr(random.randint(1, 26) + 96)
#         for i in range(5000):
#             str += chr(random.randint(1, 26) + 96)
#         str += same
#         for i in range(5000):
#             str += chr(random.randint(1, 26) + 38)
#         str += same
#         f.write(str + "\n")


with open("big.txt") as f:
    lines = f.readlines()


def f1(lines):
    sum = 0
    for line in lines:
        line = list(line.strip())
        a = line[:int(len(line)/2)]
        b = line[int(len(line)/2):]
        for char in b:
            if char in a:
                if ord(char) > 96:
                    sum += ord(char) - 96
                    break
                else:
                    sum += ord(char) - 38
                    break
    return sum

def f2(lines):
    sum = 0
    for line in lines:
        d = {}
        line = list(line.strip())
        a = line[:int(len(line)/2)]
        b = line[int(len(line)/2):]
        for char in a:
            d[char] = "A"
        for char in b:
            if char in d and d[char] == "A":
                if ord(char) > 96:
                    sum += ord(char) - 96
                    break
                else:
                    sum += ord(char) - 38
                    break
            else:
                d[char] = "B"
    return sum

import time
#start_time = time.time()
#print(f1(lines))
#print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(f2(lines))
print("--- %s seconds ---" % (time.time() - start_time))
