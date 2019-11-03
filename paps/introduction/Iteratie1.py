counter = 1
inputPostFixString = "Geef positief getal in:"
inputString = "Poging {} ".format(counter) + inputPostFixString
myVariable = int(input(inputString))

while (myVariable <= 0):
    counter += 1
    inputString = "Poging {} ".format(counter) + inputPostFixString
    myVariable = int(input(inputString))

print ('Positief getal =', myVariable)