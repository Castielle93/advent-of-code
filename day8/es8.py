with open('input.txt') as infile:
    lines = infile.readlines()



def creaMatrix(righe):
    res = []
    for riga in righe:
        riga = riga.strip()
        res.append([int(elem) for elem in riga])
    return res

def trovaVisibili(matrice):

    #ricordarsi di aggiungere il bordo, che è comunque sempre visibile
    conta = 0
    for i,riga in enumerate(matrice[1:-1], start=1):
        for j,albero in enumerate(riga[1:-1], start=1):

            trovato = False
            # print('Sto valutanto l''albero di valore {} all'' indice ({},{})'.format(albero, i, j))
            
            sopra    = max([matrice[indice][j] for indice in range(i)])
            # print('valore massimo trovato sopra: {}'.format(sopra))
  
            sotto    = max([matrice[indice][j] for indice in range(i+1, len(matrice))])
            # print('valore massimo trovato sotto: {}'.format(sotto))

            destra   = max(riga[j+1:])
            # print('valore massimo trovato destra: {}'.format(destra))

            sinistra = max(riga[:j])
            # print('valore massimo trovato sinistra: {}'.format(sinistra))

            #se l'albero è visibile a dx, sx, sopra o sotto
            if albero > destra or albero > sinistra or albero > sotto or albero > sopra :
                trovato = True
                # print('trovato, aggiungo')
                

            if trovato:
                conta += 1
            # else:
            #     print('nada')
            # print('conteggio attuale: {}'.format(conta))
            # print('-----------------------------------')

    #aggiungo il bordo
    conta += (len(matrice)*2 + len(matrice[0])*2 - 4)

    return conta


def trovaCoperturaMax(matrice):
    with open('debug.txt', 'w+') as outfile:
        # interazioni = 0
        res = []
        for i,riga in enumerate(matrice):
            # interazioni += 1
            # if interazioni == 3:
            #     break
            for j,albero in enumerate(riga):
                outfile.write('Sto valutanto l'' albero di valore {} all'' indice ({},{}) \n'.format(albero, i, j))
                
                sopra = sotto = destra = sinistra = 0

                colonna = [ matrice[idx][j]for idx in range(len(matrice))]
                
                #sopra
                if i == 0 :
                    sopra = 1
                else:
                    trovatoUp = False
                    for n,elemento in enumerate(colonna[:i][::-1]):
                        if elemento >= albero:
                            trovatoUp = True
                            indiceUp = n
                            break
                    if trovatoUp:
                        sopra = indiceUp + 1
                    else:
                        sopra = i
                outfile.write('copertura superiore = {}\n'.format(sopra))


                #sotto
                if i == len(matrice)-1:
                    sotto = 1
                else:
                    trovatoDown = False
                    for p,elemento in enumerate(colonna[i+1:]):
                        if elemento >= albero:
                            trovatoDown = True
                            indiceDown = p
                            break
                    if trovatoDown:
                        sotto = indiceDown + 1
                    else:
                        sotto = (len(colonna)-1) - i
                outfile.write('copertura sotto = {}\n'.format(sotto))


                #sinistra
                if j == 0:
                    sinistra = 1
                else:
                    trovatosx = False
                    for q, alberosx in enumerate(riga[:j][::-1]):
                        if alberosx >= albero:
                            trovatosx = True
                            indicesx = q 
                            break
                    if trovatosx:
                        sinistra = indicesx + 1
                    else:
                        sinistra = j
                outfile.write('copertura sinistra = {}\n'.format(sinistra))


                #destra
                if j == len(matrice[0])-1:
                    destra = 1
                else:
                    trovatodx = False
                    for r, alberodx in enumerate(riga[j+1:]):
                        if alberodx >= albero:
                            trovatodx = True
                            indicedx = r                     
                            break
                    if trovatodx:
                        destra = indicedx + 1
                    else:
                        destra = (len(matrice[0])-1) - j

                outfile.write('copertura destra = {}\n'.format(destra))

                res.append(sopra*sotto*destra*sinistra)
                outfile.write('Aggiungo {} alla lista\n'.format(sopra*sotto*destra*sinistra))
                outfile.write('------------------------------------------\n')
    return max(res)




# print(trovaVisibili(creaMatrix(lines)))   

print(trovaCoperturaMax(creaMatrix(lines)))
            


# 234416


