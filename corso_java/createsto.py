import random

kek = list(range(97,123))
lunRiga = 30
lunFile = 500
loginGiusto = 'Castielle93'
pwdGiusta = 'popone123'

# ora scelgo due righe a caso
riga1 = random.choice(range(lunFile+1))
riga2 = random.choice(range(lunFile+1))
if riga1 == riga2:
    if riga2+1 <= lunFile:
        riga2 = riga1 + 1
    else:
        riga2 = riga1 - 1

print('riga del login scelta = {}'.format(riga1))
print('riga della pwd scelta = {}'.format(riga2))

with open('./inputLogin.txt', 'w+') as outfile:
    for i in range(lunFile):
        if i == riga1:
            outfile.write(loginGiusto + '\n')
        elif i == riga2:
            outfile.write(pwdGiusta + '\n')
        else:
            stringaTemp = ''.join(chr(random.choice(kek)) for idx in range(lunRiga))
            outfile.write(stringaTemp + '\n')
    


