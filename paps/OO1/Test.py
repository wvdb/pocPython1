from paps.OO1.Employee import Employee

__author__ = 'Wim Van den Brande'

import datetime

# 1ste persoon
p1 = Employee("Wim", "VdB", 52, datetime.datetime(1967, 11, 2), ["bike", "car"])
print(p1)

print(p1.getName())
print('Leeftijd =', p1.age)
print('Person\'s creationDate =', p1.creationDate)

print('Transport-Modi of Person:')
for transport in p1.transportModi:
    print(transport)

p1.age += 1
print('Leeftijd = {:04d} jaar.'.format(p1.age))

p1.printName()

# 2de persoon
p2 = Employee("Floriaan", "VdB", 18, datetime.datetime(2001, 6, 11), None)
print("Floriaan is geboren op", p2.birthDate.strftime("%A"), "op dag", p2.birthDate.strftime("%j"), "van het jaar 2001.")
