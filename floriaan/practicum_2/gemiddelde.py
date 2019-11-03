

getal = int(input('geef een waarde voor getal (0 om te stoppen): '))
aantal_ingelezen_getallen = 1
som = 0

while getal != 0:
    aantal_ingelezen_getallen += 1
    som = getal + som
    getal = int(input('geef een waarde voor getal (0 om te stoppen): '))

print('het aantal ingelezen getallen is: ', aantal_ingelezen_getallen - 1) #want 0 telt niet mee bij het aantal
print('de som van de ingelezen getallen is: ', som)

gemiddelde = som/(aantal_ingelezen_getallen -1)
print('het gemiddelde van de ingelezen getallen is: ', gemiddelde)
