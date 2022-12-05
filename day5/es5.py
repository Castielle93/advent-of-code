# [N] [G]                     [Q]    
# [H] [B]         [B] [R]     [H]    
# [S] [N]     [Q] [M] [T]     [Z]    
# [J] [T]     [R] [V] [H]     [R] [S]
# [F] [Q]     [W] [T] [V] [J] [V] [M]
# [W] [P] [V] [S] [F] [B] [Q] [J] [H]
# [T] [R] [Q] [B] [D] [D] [B] [N] [N]
# [D] [H] [L] [N] [N] [M] [D] [D] [B]
#  1   2   3   4   5   6   7   8   9 



with open('input.txt') as infile:
    lines = infile.readlines();

# print(lines[0:3])

def estraiMosse(righe):

    res = []
    for riga in righe[10:]:
        res.append([carattere for carattere in riga.strip() if not carattere.isalpha() and carattere != ' '])
    for i in range(len(res)):
        if len(res[i]) == 4:
            res[i] = [''.join(res[i][0:2])] + res[i][2:] 
    return res


# print(estraiMosse(lines))

def f1(righe):

    diz = {}
    chiavi = [' ']
    chiavi.extend(car for car in righe[8].strip() )
    
    for riga in righe[:8]:
        riga = riga.strip()
        for i in range(1,len(riga)-1,4):
            # print (list(range(1,len(riga)-1,4)))
            if riga[i].isalnum():
                try:
                    diz[chiavi[i]].append(riga[i])
                except KeyError:
                    diz[chiavi[i]] = [riga[i]]
    # print(diz)
    #ho il dizionario con le crates ordinate dalla piu alta(che esce prima) alla piu bassa

    #ora abbiamo bisogno delle istruzioni da fare

    for n, partenza, arrivo in estraiMosse(righe):
        for i in range(int(n)):
            #per n volte inserisco il pacco in cima alla lista di arrivo
            diz[arrivo].insert(0,diz[partenza][0])
            #...e lo rimuovo dalla cima della lista di partenza
            diz[partenza] = diz[partenza][1:]

    #dopo aver fatto tutte le mosse vuole sapere solo i pacchi rimasti in cima a ogni blocco (nb il dizionario non ha un ordinamento)

    return''.join(diz[str(indice)][0] for indice in range(1,10))





print(f1(lines))

