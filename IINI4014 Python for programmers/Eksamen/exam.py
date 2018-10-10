"""
	Title:	exam
	Date:	30.11.2017
	Author:	Anders Kvanvig
"""

#Gets textfile and returns it's content
def importText(filepath):
    textfile = open(filepath, 'r')
    return textfile.read()

#Creates a dictionary that says how many times each word was used in the text
def createDict(text): #Remove .,:;-_^¨ osv. if time
    listWords = text.split(" ")
    #Removes certain charachters to get only the words
    for i in range(0, len(listWords)):
        listWords[i] = listWords[i].replace('.', '')
        listWords[i] = listWords[i].replace(',', '')
        listWords[i] = listWords[i].replace("'", '')
        listWords[i] = listWords[i].replace('"', '')
        listWords[i] = listWords[i].replace('!', '')
        listWords[i] = listWords[i].replace('?', '')
        listWords[i] = listWords[i].replace(':', '')
        listWords[i] = listWords[i].replace(';', '')

        #If a new line charachter is found (\n), the following words will be added last in the word list
        if '\n' in listWords[i]:
            listWords[i] = listWords[i].replace('\n',' ')
            newWordList = listWords[i].split(' ')
            for j in range(1, len(newWordList)):
                listWords.append(newWordList[j])


    wordsFound = dict() #creates empty dictionary and goes through all words, adding them to the list
    for word in listWords:
        wordsFound = addWord(word, wordsFound)

    return wordsFound

#Goes through the dictionary and cheks if the word already is in it, if not it gets added with a value of one.
def addWord(word, wordsFound):
    changed = False
    for key in wordsFound.keys():
        if key == word:
            wordsFound[key] += 1
            changed = True

    if not changed:
        wordsFound[word] = 1

    return wordsFound

#Splits a given string on spaces and counts number of words in the text
def countWords(wordsFound):
    totalWords = 0
    for key, value in wordsFound.items():
    	totalWords += value

    return totalWords

def findWordCount(text):
	totalwords = 0
	listWords = text.split(' ')
	totalWords = len(listWords)

	return totalWords

#Splits text on period ('.'), og for each sentence it splits on spaces (' ') and counts words pr sentence. Last all the wordcounts gets averaged
def sentenceLength(text):
    listSentences = text.split('.')
    countSentences = 0
    numberWords = 0

    for sentence in listSentences:
        countSentences += 1
        numberWords += findWordCount(sentence)

    return (numberWords / countSentences)

#Gets average length of paragraphs in number of sentences
def paragraphLength(text):
    listParagraphs = text.split('\n') #splits on each new line
    countParagraphs = 0
    countSentences = 0

    for paragraph in listParagraphs:
        countParagraphs += 1
        listSentences = paragraph.split('.')
        for sentence in listSentences:
            countSentences += 1

    return (countSentences / countParagraphs)

#If a word was used more then x amount of times it is considered easy, should be a percentage for better results, but I'm using set amount because of lack of time :)
def findEasyWords(dictionary):
    easyWords = dict()
    for key, value in dictionary.items():
        if value > 10:
            easyWords[key] = value
    return easyWords

#If a word has been usen more then x amount in the original document, then it is not considered a difficult word
#Again, a percentage should be used, but because of little time, this is done instead.
def findCommonWords(dictionary):
    commonWords = dict()
    for key, value in dictionary.items():
        if value < 2:
            commonWords[key] = value
    return commonWords

#Compares two dictionaries and gets count
def numberOfGivenWords(Words, wordsFoundSecond):
    numberWords = 0
    for key1, value1 in wordsFoundSecond.items():
        for key2, value2 in easyWords.items():
            if key1 == key2:
                numberWords += value1
                break
    return numberWords

    #Analyzes the second text to find certain bits of information about the text
def analyze(text, wordsFoundFirst, easyWords, commonWords):
    wordsFoundSecond = createDict(text)
    totalWordCount = countWords(wordsFoundSecond)
    totalUniqueWordCount = len(wordsFoundSecond)
    averageWordsPrSentence = sentenceLength(text)
    averageSentencesPrParagraph = paragraphLength(text)
    countEasyWords = numberOfGivenWords(easyWords, wordsFoundSecond)
    countCommonWords = numberOfGivenWords(commonWords, wordsFoundSecond)

    #Prints results to user
    print('The average sentence length is:                      {:3f} words'.format(averageWordsPrSentence))
    print('The percentage of easy words in this text is:        {:3f} %'.format(countEasyWords / totalWordCount * 100))
    print('The percentage of hard words in this text is:        {:3f} %'.format((totalWordCount - countCommonWords) / totalWordCount * 100))
    print('The percentage of unique words is:                   {:3f} %'.format(totalUniqueWordCount / totalWordCount * 100))
    print('The average number of sentences pr. paragraph is:    {:3f} sentences'.format(averageSentencesPrParagraph))

#Main
filePath1 = 'c:\\folder-1\\first.txt'   #to create dictionary(histogram)
filepath2 = 'c:\\folder-1\\second.txt'  #to be analysed using dictionary from first file

text1 = importText(filePath1)#Imports textfile to create dictionary
wordsFoundFirst = createDict(text1)#Creates dictionary
#Finds words wich are considered easy and common in dictionary of the first document
easyWords = findEasyWords(wordsFoundFirst)
commonWords = findCommonWords(wordsFoundFirst)

text2 = importText(filepath2)#Imports second textfile to be analyzed
analyze(text2, wordsFoundFirst, easyWords, commonWords)#Sends the text and dictionary of first file to analyze the second one
