

def analizza(s):

    for indice,lettera in enumerate(s):
        print('Lettera {}: {}'.format(indice+1, lettera))
    return

# frase = input('inserisci che ti pare')

# analizza(frase)

###

# Scrivere un programma che stampi la lunghezza di una stringa fornita dall’utente,
#  e ripeta questo processo finchè l’utente non inserisce la stringa ‘exit’.

def stampaLun():


    s = input('Inserisci una frase (digita exit per uscire)')

    while s.strip() != 'exit':
        print('lunghezza stringa = {}'.format(len(s)))
        s = input('Inserisci una frase (digita exit per uscire)')
    
    print('ok, ciao!')
    return

# stampaLun()


### 

# Scrivere un programma che prenda in ingresso un intero e stampi 
# tutti i numeri primi fino al numero fornito dall’utente.

def stampaPrimi():
    n = int(input('Inserisci un numero: '))

    for i in range(2,n):
        nonDivisibile = True
        for j in range(2,i):
            if i%j == 0:
                nonDivisibile = False
        if nonDivisibile:
            print(i)
    return

# stampaPrimi()


###

# Scrivere un programma che:

# Prenda una stringa in input da tastiera, rappresentante un singolo nucleotide
# (A, C, G oppure T).

# Stampi a video una stringa rappresentante il nucleotide complementare.

# Assicurarsi che il programma funzioni correttamente sia con input maiuscolo 
# che minuscolo.

def stampaComplementare():
    diz = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    s = input('inserisci un nucleotide (a,c,g,t): ').strip().upper()
    if s not in diz.keys():
        print('hai inserito una sigla non valida!')
        return
    print('La base complementare a {} è {}'.format(s,diz[s]))
    return

# stampaComplementare()

### 

# Riprendere l’esercizio 8, e risolverlo definendo una funzione complementare(), 
# che ritorni il nucleotide complementare a quello passato come argomento:

def complementare(nuc):
    nuc = nuc.strip().upper()
    diz = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    
    if nuc not in diz.keys():
        print('hai inserito una sigla non valida!')
        return
    
    return diz[nuc]

# s = 'A'
# print(complementare(s))


### 

# Modificare l’esercizio in modo da gestire il caso in cui sia inserito un nucleotide 
# non valido tramite l’uso delle eccezioni. In particolare si modifichi la funzione
# complementare in modo da lanciare un eccezione generica Exception in caso di 
# nucleotide non valido. Tale eccezione deve essere catturata e gestita dal programma 
# principale tramite la stampa a video di un messaggio di errore.


def complementare2(nuc):
    nuc = nuc.strip().upper()
    diz = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    
    try:
        return diz[nuc]
    except KeyError:
        print('hai inserito la sigla sbagliata')
        return -1

# print(complementare2('a'))


### 

#  Modificare ulteriormente il programma dell’esercizio 9 (punto I) 
#  in modo da aggiungere una funzione filamento_opposto(), che utilizzi
#  la funzione complementare() per restituire il filamento opposto a
#  quello passato come argomento:

def filamentoOpposto(nucs):

    return ''.join(complementare(nuc) for nuc in nucs)

# print(filamentoOpposto('ctaatgt'))


### 

# Aggiungere una funzione reverse_complement(), 
# che restituisca il reverse complement del filamento 
# passato come argomento alla funzione:

def reverseComplement(nucs):
    return ''.join(complementare(nuc) for nuc in nucs[::-1])

# print(reverseComplement('CTAATGT'))


###

# Modificare il programma in maniera tale da importare il modulo 
# random e usarlo per generare un filamento casuale da dare in pasto 
# alla funzione reverse_complement. Si consiglia di usare la funzione choice() 
# del modulo random che ritorna un elemento casuale tra gli elementi di una 
# sequenza data in ingresso.

# import random
# nucs = ('A', 'C', 'G', 'T')
# lunghezza = 100

# filamento = ''.join(random.choice(nucs) for i in range(lunghezza))

# print(filamento)
# print(filamentoOpposto(filamento))




############################



# Scrivere un programma che legga un intero righe e un 
# intero colonne da tastiera e stampi a schermo:

#X X X X X
#X X X X X
#X X X X X

# L’esempio riporta l’output richiesto per righe = 3 e colonne = 5. 
# Per andare a capo, dare l’istruzione print senza argomenti: print.
# Per stampare senza andare a capo, aggiungere una virgola in fondo 
# alla riga con l’istruzione print. Es: print "ciao",

def stampaMatrice(righe, colonne):
    for i in range(righe):
        for j in range(colonne):
            print('X', end = '')
        print()
    return


# r = int(input('Inserisci righe: '))
# c = int(input('Inserisci colonne: '))

# stampaMatrice(r,c)


####################

# Scrivere un programma che definisca la funzione dh(s,t), che implementi 
# il calcolo della distanza di Hamming 
# tra due stringhe s e t.

def dh(s,t):
    if len(s) != len(t):
        return -1
    return sum( 1 if es!=et else 0 for es, et in zip(s,t))

# a = 'porcoddio'
# b = 'porcodcio'
# print('la distanza di Hamming tra le due stringhe è {}'.format(dh(a,b)))

####

# Aggiungere la funzione dhplus(s,t), che generalizzi dh(s,t) al caso di 
# stringhe di diversa lunghezza. Visto che molte generalizzazioni della distanza 
# di Hamming sono possibili e’ richiesta l’implementazione di questo primo modo:
# estendere la stringa di lunghezza minore con una serie di caratteri non validi
# (ad esempio ’-’) in modo da ottenere stringhe di lunghezza uguale.

def dhplus(s,t):

    ls = len(s)
    lt = len(t)
    delta = abs(lt - ls)    

    if delta > 0 :
        
        if ls > lt:
            t += '-' * delta
        else:
            s += '-' * delta

    return s, t, dh(s,t) 

# a = 'ciccia'
# b = 'culoculo'
# s,t,res = dhplus(a,b)
# print('a = {}'.format(s))
# print('b = {}'.format(t))
# print('la distanza di Hamming tra le due stringhe è {}'.format(res))


###################

# Scrivere un programma che calcoli il fattoriale di un numero dato in input dall’utente. 
# Il programma dovra fare uso di funzioni ricorsive.

def fattoriale(n):
    #casi base
    if n == 0:
        return 1
    if n < 0:
        raise Exception("hai sbagliato input")
        
    
    return n*fattoriale(n-1)

# print (fattoriale(10))

###########


# Scrivere una funzione ricorsiva che calcoli la somma degli elementi di un vettore dato in ingresso.

def sommaRicorsiva(lista):
    
    if not lista:
        return 
    if len(lista) == 1:
        return lista[0]
    return lista[0] + sommaRicorsiva(lista[1:])

print(sommaRicorsiva(range(3)))