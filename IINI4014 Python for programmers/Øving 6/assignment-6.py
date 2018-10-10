"""
	Title:	assignment-5.py
	Date:	21.10.2017
	Author:	Anders Kvanvig
"""
import os
basefolder = 'c:\\Folder-1'

def checkFiles(files, folder):	#Checks every file in folder for txt files, and writes their contents to the log when something is found
	global basefolder
	for file1 in files:
		if file1.endswith('.txt') and not file1 == 'Log.txt':
			textFile = open(folder + '\\' + file1, 'r')			#Selects the correct file
			content = textFile.read()							#Collects text from the txt file
			textFile.close()
			textFile = open(basefolder + '\\Log.txt', 'a')		#Opens the Log file
			textFile.write('\n \n' + folder + '\\' + file1 + '\n' + content)	#Writes contents of the file to the Log-file
			textFile.close()

		elif os.path.isdir(folder + '\\' + file1):				#If a folder is found, the program will check for files/folders in that as well
			checkFiles(os.listdir(folder + '\\' + file1), folder + '\\' + file1)

def main():
	global basefolder

	#Create the three folders unders C:\
	try:											#If the two first folders already excists, the program will notify user
		os.makedirs(basefolder + '\\Folder-2-1')	#Creates the first and second folder
	except Exception as e:
		print('folders 1, and 2 already excists')

	try:											#If the third folder already excists, the program will notify user
		os.makedirs(basefolder + '\\Folder-2-2')	#Creates the third folder
	except Exception as e:
		print('folder 3 already excists')

	#Places one textfile in each folder
	file1 = open(basefolder + '\\File-1.txt', 'w')				#Creates the first file
	file1.write('When, in disgrace with fortune and men\'s eyes,\n')
	file1.close()

	file2 = open(basefolder + '\\Folder-2-1\\File2.txt', 'w')	#Creates the second file
	file2.write('I all alone beweep my outcast state, \nAnd trouble deaf heaven with my bootless cries,')
	file2.close()

	file3 = open(basefolder + '\\Folder-2-2\\File3.txt', 'w')	#Creates the third file
	file3.write('And look upon myself and curse my fate,')
	file3.close()

	fileLog = open(basefolder + '\\Log.txt', 'w')				#Creates the Log file, which copies all other files into it

	#Checks for textfiles in the folders
	filesFound = os.listdir(basefolder)							#Checks the folder
	checkFiles(filesFound, basefolder)

main()

"""
	filesFound = os.listdir('c:\\Folder-1\\Folder-2-1')	#Checks the second folder
	checkFiles(filesFound))
	filesFound = os.listdir('c:\\Folder-1\\Folder-2-2')	#Checks the third folder
	checkFiles(findTxtFiles(filesFound))
"""
