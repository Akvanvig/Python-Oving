#Get input from user
a = input('Skriv inn ett tall: ')
b = input('Skriv inn ett tall: ')

#Write results to user
#String + String
c = a + b
print('String + String')
print(c)

#Number + Number
c = int(a) + int(b)
print('int + int')
print(c)

#The first is a result of combining two strings and will just put one after the other (concatenation). In the second one, it understands that it should get the sum as both are numbers (integers)

print('String * int')
print(a*int(b))

print('')
print('No separation')
print('Have','a','nice','day', sep='')
print('')
print('Separation with spaces')
print('Have','a','nice','day', sep=' ')
print('')
print('Separation with arrow')
print('Have','a','nice','day', sep='->')
print('')
print('Separation with tab')
print('Have','a','nice','day', sep='    ')
print('')
print('Separation with return')
print('Have','a','nice','day', sep='\n')
print('')
print('Separation with five blank lines')
print('Have','a','nice','day', sep='\n \n \n \n \n')
print('')

#Text formatting
#Centre
print('{:^20}'.format('test'))
#Stars
print('{:*<20}'.format('test'))
#Left
print('{:20}'.format('test')) #'print(test)' will give the same result
#Right
print('{:>20}'.format('test'))

print('')

#Modulo
x = int(input('Skriv inn tallet du ønsker tabellen for: '))

for i in range(-1, x):
    linje = ''
    for j in range(-1, x):
        #Checks if we are writing the top row as this will contain index numbers
        if i == -1:
            #Checks if we are writing first column of first row (should not contain anything)
            if j == -1:
                linje += '   '
            else:
                linje += str(j) + '   '
                pass
            pass
        else:    #If we are not in first row, we need to check for first column as this won't contain the modulo result but index numbers
            if j == -1:
                linje += str(i) + '  '
            else:
                linje += str((i * j) % x) + '   '
                pass
        pass
    print(linje)
    print()
    pass
