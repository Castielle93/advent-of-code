
with open('input.txt') as infile:
    lines = infile.readlines()



def f1(righe):

    res = 0

    for riga in righe:
        riga = riga.strip()
        l = riga.split(',')
        #['71-97', '71-92']
        range1 = l[0] # '71-97'
        range2 = l[1] # '71-92'

        inizio1 = int(range1.split('-')[0])
        fine1   = int(range1.split('-')[1]) + 1 #estremi inclusi

        inizio2 = int(range2.split('-')[0])
        fine2   = int(range2.split('-')[1]) + 1 #estremi inclusi

        insieme1 = set(range(inizio1, fine1))
        insieme2 = set(range(inizio2, fine2))

        if insieme1.intersection(insieme2) == insieme2 or insieme1.intersection(insieme2) == insieme1:
            res += 1
            
    
    return res



def f2(righe):

    res = 0

    for riga in righe:
        riga = riga.strip()
        l = riga.split(',')
        #['71-97', '71-92']
        range1 = l[0] # '71-97'
        range2 = l[1] # '71-92'

        inizio1 = int(range1.split('-')[0])
        fine1   = int(range1.split('-')[1]) + 1 #estremi inclusi

        inizio2 = int(range2.split('-')[0])
        fine2   = int(range2.split('-')[1]) + 1 #estremi inclusi

        insieme1 = set(range(inizio1, fine1))
        insieme2 = set(range(inizio2, fine2))

        if insieme1.intersection(insieme2): #se l'intersezione non è vuota (c'è overlap, non voglio overlap totale ma basta che ci sia)
            res += 1
            
    
    return res
    

print(f1(lines))
print(f2(lines))
#ciao SIMO