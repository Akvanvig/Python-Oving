"""
	Øving 3
	02.09.2018
	Anders Kvanvig

    Python 3
"""
filer = ['test_oppgave1.txt', 'Lorem.txt', 'wiki.txt']

#Oppgave 2
def hentTekstinfo(filnavn):
    f = open(filnavn, 'r')
    linjer = f.readlines()
    f.close()
    antLinjer = len(linjer)

    #Finner antall ord
    sumOrd = 0
    for linje in linjer:
        ord = linje.split(' ')
        sumOrd += len(ord)

    return antLinjer, sumOrd

#Oppgave 3
#Skriver ikke ut antall bytes, ettersom jeg da måtte visst hvilken encoding som er i bruk (ANSI = 8 bit, UTF-8 = 8-32 bit)
def hentAntTegn(filnavn):
    f = open(filnavn, 'r')
    tekst = f.read()
    f.close()
    return len(list(tekst))


print('{:25}{:>14}{:>14}{:>14}'.format('filnavn','Antall linjer', 'Antall Ord', 'Antall Tegn'))
for fil in filer:
    try:
        antallLinjer, antallOrd = hentTekstinfo(fil)
        antallTegn = hentAntTegn(fil)
        print('{:25}{:>14}{:>14}{:>14}'.format(fil, antallLinjer, antallOrd, antallTegn))
    except Exception as e:
        print('Filen {} kunne ikke leses'.format(fil))
        f = open('error.log','a+')
        f.write('{:25}{}\n'.format(fil, e))
        f.close()
