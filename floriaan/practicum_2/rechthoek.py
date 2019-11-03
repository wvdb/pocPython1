aantal_spaties = int(input('geef het aantal spaties: '))
breedte = int(input('geef de breedte: '))
hoogte = int(input('geef de hoogte: '))
teken = input('geef een teken: ')

tellerH = 1

while tellerH <= hoogte:
    tellerH += 1
    tellerS = 1
    while tellerS <= aantal_spaties:
        tellerS += 1
        print(' ', end='')
    tellerB = 1
    while tellerB <= breedte:
        tellerB += 1
        print(teken, end='')
    print('', end='\n')
