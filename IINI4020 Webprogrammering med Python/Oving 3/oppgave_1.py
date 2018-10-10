"""
	Øving 3
	02.09.2018
	Anders Kvanvig

    Python 3
"""
#a
print('Oppgave a\n')
try:
    f = open('test_oppgave1.txt','w')
    f.write('Hallo\nSkriver en linje til\nHer kommer enda en linje')
    f.close()
    print('Tekst skrevet til fil')
except Exception as e:
    print(e)


#b
print('\nOppgave b\n')
try:
    f = open('test_oppgave1.txt', 'r')
    linjer = f.readlines()
    f.close()
    print(linjer[1])
except Exception as e:
    print(e)


#c
print('\nOppgave c\n')
try:
    f = open('test_oppgave1.txt', 'r')
    print(f.read(10))
    f.close()
except Exception as e:
    print(e)
