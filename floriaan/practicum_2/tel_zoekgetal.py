te_zoeken_getal = int(input('geef een waarde voor het te zoeken getal: '))
aantal =0

for i in range (1,7):
    waarde = int(input('geef een waarde voor getal: '))
    if te_zoeken_getal == waarde:
        aantal += 1

print('het getal', te_zoeken_getal, 'komt', aantal, 'keer voor')

