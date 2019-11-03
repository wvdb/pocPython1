hoogte = int(input('geef de hoogte: '))

print('', end='\n')

tellerHoogte = 1

while tellerHoogte <= hoogte:
    tellerSpatie = 1

    # zorg voor correct aantal spaties
    while tellerSpatie <= hoogte - tellerHoogte:
        tellerSpatie += 1
        print(' ', end='')

    # zorg voor printen van het getal
    tellerGetal = 1
    while tellerGetal <= tellerHoogte:
        tellerGetal += 1
        print(tellerHoogte, end=' ')

    tellerHoogte += 1
    print('', end='\n')
