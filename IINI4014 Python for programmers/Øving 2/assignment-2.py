#Get input from user
a = input('Write the first word: ')
b = input('Write the second word: ')

#Checks letters in each word using the ord-function
#Creating two arrays to compare letters with
countA = [0]*26
countB = [0]*26

#goes through each letter in 'a' and gets letter values
for  i in range(len(a)):
    pos = 0
    if ord(a[i]) > 96 and ord(a[i] < 123): #Checks if lower or upper case letters were used and gets the value
        pos = (ord(a[i]) - ord('a'))
    elif ord(a[i]) > 64 and ord(a[i]) < 90:
        pos = (ord(a[i]) - ord('A'))
    countA[pos] += 1

#goes through each letter in 'b' and gets letter values
for  i in range(len(b)):
    pos = 0
    if ord(b[i]) > 91: #Checks if lower or upper case letters were used and gets the value
        pos = (ord(b[i]) - ord('a'))
    else:
        pos = (ord(b[i]) - ord('A'))
    countB[pos] += 1


#Compares the numbers of letters in each word, starting with those missing i the first string
isAnagram = True
print('')

#Checks the first word
Output = ''
for i in range(0, 25):
    if countA[i] < countB[i]: #If string B contains more letters then string A, it will print those letters to the user
        Output += ((chr(i + 65) + ' ') * (countB[i] - countA[i]))

if Output != '': #Writes missing letters to user if any are missing
    print('The following letters are missing from the first word:')
    print(Output)
    isAnagram = False

print('')

#Checks the second word
Output = ''
for i in range(0, 25):
    if countB[i] < countA[i]: #If string B contains more letters then string A, it will print those letters to the user
        Output += ((chr(i + 65) + ' ') * (countA[i] - countB[i]))

if Output != '': #Writes missing letters to user if any are missing
    print('The following letters are missing from the second word:')
    print(Output)
    isAnagram = False

if isAnagram: #If the two words are anagrams, the user is informed of this
    print('The two words, "' + a + '" and "' + b + '" are anagrams')
