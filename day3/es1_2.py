
# vJrwpWtwJgWr hcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw



with open('input.txt') as infile:
    lines = [line.strip() for line in infile.readlines()]


def f1(righe):

    offsetLower = 96
    offsetUpper = 38
    res = 0
    for line in righe:

        

        diz1 = {}
        diz2 = {}

        l = int(len(line) / 2)
        for car in line[:l]:
            try:
                diz1[car] += 1
            except KeyError:
                diz1[car] = 1

        for car2 in line[l:]:
            try:
                diz2[car2] += 1
            except KeyError:
                diz2[car2] = 1

        for chiave in diz1.keys():
            if chiave in diz2.keys():
                # print('{} e la sua priorità è {}'.format(chiave, ord(chiave) - offsetLower if chiave.islower() else ord(chiave) - offsetUpper ))
                res += ord(chiave) - offsetLower if chiave.islower() else ord(chiave) - offsetUpper

    return res



def f2(righe):
    #ora devo prendere le righe a 3 a tre, guardare il carattere a comune tra le tre righe e poi sommare la priorità di tale carattere
    #al risultato finale
    offsetLower = 96
    offsetUpper = 38
    res = 0   

    diz1 = {}
    diz2 = {}
    diz3 = {}

    righe = [line.strip() for line in righe]

    righeAtreAtre = [righe[i:i+3] for i in range(0,len(righe)-2,3)]
    

    for gruppo in righeAtreAtre:

        diz1 = {}
        diz2 = {}
        diz3 = {}
        #1
        for car in gruppo[0]:
            try:
                diz1[car] += 1
            except KeyError:
                diz1[car] = 1
        
        #2
        for car in gruppo[1]:
            try:
                diz2[car] += 1
            except KeyError:
                diz2[car] = 1
        
        #3
        for car in gruppo[2]:
            try:
                diz3[car] += 1
            except KeyError:
                diz3[car] = 1
        
        for chiave in diz1.keys():
            if chiave in diz2.keys() and chiave in diz3.keys():
                res += ord(chiave) - offsetLower if chiave.islower() else ord(chiave) - offsetUpper
    #         print('la chiave è {} e la priorità vale {}'.format(chiave,res))
    # print(diz1)
    # print(diz2)
    # print(diz3)
    

    return res

print(f2(lines))





# import time
# start_time = time.time()
# print(f1(lines))
# print("--- %s seconds ---" % (time.time() - start_time))

