"""
	Øving 1
	31.08.2018
	Anders Kvanvig

    Velger å skrive programmene i Python 3 ettersom det er noe jeg har vært borti før, Python 2 er på vei ut,
    og det ble sagt under 'Om emnet' på blackboard at det godt kan brukes'
"""

#Oppgave 1
print('Oppgave 1')
#a
print('Hello World')
#b
print('Hei, Anders!')
#c
navn = input('Skriv inn et navn:\n')
print('Hei, ' + navn + '!')


#Oppgave 2
print('\n\nOppgave 2')
#a
print('1 + 3 * 3 = ' + str(1+3*3))
#b
print('1 + (5 * 3) = ' + str(1+(5*3)))
#c
print('(1 + 4) * 3 = ' + str((1+4)*3))
#d
from math import pi
r = 8
print('Omkrets av sirkelen er: ' + str( 2 * pi * r))
print('Arealet av sirkelen er: ' + str( pi * r ** 2))


#Oppgave 3
print('\n\nOppgave 3')
#a
tall1 = input('Skriv inn det første tallet:\n')
tall2 = input('Angi tallet du ønsker å summere med:\n')

print('Summen av disse to tallene er \'' + str(int(tall1) + int(tall2)) + '\'')
