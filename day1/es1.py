

#voglio trovare l'elfo che ha piu calorie e restituire il numero di calorie max
with open('input1.txt') as infile:
    righe = [ elem.strip() for elem in infile.readlines()]

    maxCal = 0
   
    contaCal = 0
    for cibo in righe:
        if cibo == '': #sono arrivato alla fine dell'elfo 
            if contaCal > maxCal: #controllo se ho superato il massimo raggiunto
                maxCal = contaCal #in caso sostituisco il max
            contaCal = 0          #dopo il check riazzero le cal per l'elfo successivo
        else:
            contaCal += int(cibo)
    


print(maxCal)

