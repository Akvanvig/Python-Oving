"""
	Title:	assignment-4.py
	Date:	24.09.2017
	Author:	Anders Kvanvig
"""
def bubblesort(list1, list2):
    #Gets the lenght of each list
    l1 = len(list1)
    l2 = len(list2)

    #Loop goes from length of lists minus 1 to 0 using step -1, this is to avoid going through those that are already sorted
    for passnum in range((l1+l2-1),0,-1):
        noChanges = True
        for i in range(passnum):
            if ((i+1) < l1):    #If both numbers are in the first list
                if list1[i] > list1[i+1]:   #Checks if the first number is larger then the following number
                    list1[i],list1[i+1] = list1[i+1],list1[i]   #Switches the position of the two numbers
                    noChanges = False

            elif (i < l1 and (i+1) >= l1):  #If the lower number is in first list, and higher number is in second
                if list1[i] > list2[i+1-l1]: #Checks if the first number is larger then the following number, which is in the second list
                    list1[i],list2[i+1-l1] = list2[i+1-l1],list1[i] #Switches the position of the two numbers
                    noChanges = False

            else: #If both numbers are in second list
                if list2[i-l1] > list2[i+1-l1]: #Checks if the first number is larger then the following number, both in second list
                    list2[i-l1],list2[i+1-l1] = list2[i+1-l1],list2[i-l1] #Switches the position of the two numbers
                    noChanges = False

        #If no switches are done in the loop, then the program is finished, and all numbers must be sorted
        if noChanges:
            break

    #returns resultes
    lists = [list1,list2]
    return lists            #returnes the two lists to the user sorted

#----------------------------main------------------------------------------------------
#Create two lists
listA = [13, 24, 1, 8, 5, 7,4]
listB = [2, 8, 17, 6, 22]

lists = bubblesort(listA,listB)

print(lists)
