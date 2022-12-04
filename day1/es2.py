
#voglio trovare le calorie dei 3 elfi che ne hanno di piu e dare in uscita poi la somma delle 3 max calorie

with open('input1.txt') as infile:
    righe = [elem.strip() for elem in infile.readlines()]

    maxCal = 0
    res = []
    contaCal = 0
    for cibo in righe:
        if cibo == '':  # sono arrivato alla fine dell'elfo
            res.append(contaCal)
            contaCal = 0  # dopo il check riazzero le cal per l'elfo successivo
        else:
            contaCal += int(cibo)

    # trovo le calorie massime, le salvo e le rimuovo dalla lista dei risultati
    elfo1 = max(res)
    res.remove(elfo1)

    # trovo le calorie massime, le salvo e le rimuovo dalla lista dei risultati
    elfo2 = max(res)
    res.remove(elfo2)

    # trovo le calorie massime, le salvo e le rimuovo dalla lista dei risultati
    elfo3 = max(res)
    res.remove(elfo3)

print(elfo1+elfo2+elfo3)