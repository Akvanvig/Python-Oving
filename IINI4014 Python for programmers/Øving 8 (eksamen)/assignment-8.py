"""
	Title:	assignment-8.py
	Date:	13.11.2017
	Author:	Anders Kvanvig
"""

filePath = 'c:\\folder-1\\textfile.txt' #Filepath for the textfile you want to read

#Checkes if a word is added into list of dictionaries, and increments if it is
def addWord(word, wordsFound):
    changed = False
    for key in wordsFound.keys():
        if key == word:
            wordsFound[key] += 1
            changed = True

    if not changed:
        wordsFound[word] = 1

    return wordsFound


#Gets string to split on/word to check after
print('What symbol do you want to split the text on? (space for words, or nothing for split on all characters)')
splitOn = input('')
print('Type in the word you wish to check count of following words for')
testWord = input('')

#Opens file
textFile = open(filePath, 'r')
content = textFile.read()

#If user wants split on each char, it is sent to list of char, else splits on given string
if splitOn == '':
    listWords = list(content)
else:
    listWords = content.split(splitOn)

#Goes through the list of words for the 'testWord' and when one is found
#it gets added to 'wordsFound' in the function 'addWord'
wordsFound = dict()

for i in range(0, len(listWords)):
    if listWords[i] == testWord:
        wordsFound = addWord(listWords[i+1], wordsFound)

print(wordsFound)
