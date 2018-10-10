"""
	Øving 2
	02.09.2018
	Anders Kvanvig

    Python 3
"""

#Oppgave 1
print('Oppgave 1\n')
#a
dager = ['Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lørdag', 'Søndag']

#b
print('Dagene i uka er: ')
for dag in dager:
    print('\t' + dag)

#c
print('I lista er det ' + str(len(dager)) + ' elementer')

#d
print('Dagene i uka sortert i stigende rekkefølge:')
for dag in sorted(dager):
    print('\t' + dag)


#Oppgave 2
print('\n\nOppgave 2\n')
#a
from math import sqrt, pi
sqrtPi = sqrt(pi)
print(sqrtPi)

#b
#Velger å bruke nye metoden for formatering
print('{:.3f}'.format(sqrtPi))
#Følgende skal også fungere om gammel metode skal brukes
#print('%.3f' % (sqrtPi,))

#c
print('{:.6}'.format(sqrtPi))
#Gammel metode:
#print('%.5f' % (sqrtPi,))

#d
from math import sin, cos
print('{:^11}{:^11}{:^11}'.format('x','sin(x)','cos(x)'))
#Standard for-løkke kan ikke operere med flyttall, derfor ganges det med hundre
for i in range(-100,100,5):
    j = i / 100
    sinX = sin(j)
    cosX = cos(j)
    #Setter maks bredde pr. felt til 11, flyttall får maks lengde 11, og maks 4 desimaler
    #Alle tallene blir også sentrert i sitt felt og satt direkte under overskrift på sitt felt
    print('{:^11}{:^11.4f}{:^11.4f}'.format(j,sinX,cosX))


#Oppgave 3
print('\n\nOppgave 3\n')
#a
#Funksjon for å omgjøre fra Celsius til Fahrenheit
def celsiusFar(graderC):
    graderF = graderC * (9 / 5) + 32
    return graderF

antGraderC = input('Angi temperatur i grader Celsius:\n')
try:
    antGraderF = celsiusFar(int(antGraderC))
    print(str(antGraderC) + ' grader Celsius er lik {:.1f} grader Fahrenheit'.format(antGraderF) )
except Exception as e:
    print(e)

#Oppgave 4
print('\n\nOppgave 4\n')

#Bruker skriver inn et regnestykke (f.eks. 4 + 9) bestående av to heltall og pluss, minus og gange og får svaret i retur
string = input('Skriv inn to tall separert av enten pluss (+), minus (-) eller gange (*) for å regne ut resultatet:\n')
string = string.replace(' ', '')
#Sjekker om det skal summeres
try:
    if len(string.split('+')) > 1:
        tall = string.split('+')
        print('Summen av {}, og {} er {}'.format(tall[0], tall[1], str(int(tall[0]) + int(tall[1]))))
    #Sjekker om det skal finnes differansen
    elif len(string.split('-')) > 1:
        tall = string.split('-')
        print('Differansen mellom {}, og {} er {}'.format(tall[0], tall[1], str(int(tall[0]) - int(tall[1]))))
    #Sjekker om bruker ønsker produktet av tallene
    elif len(string.split('*')) > 1:
        tall = string.split('*')
        print('Produktet av {}, og {} er {}'.format(tall[0], tall[1], str(int(tall[0]) * int(tall[1]))))
    #Klarte ikke tolke gitt tekst
    else:
        print('regnestykket ble ikke gjenkjent')
except Exception as e:
    print(e)
