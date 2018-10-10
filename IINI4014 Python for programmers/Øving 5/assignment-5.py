"""
	Title:	assignment-5.py
	Date:	16.10.2017
	Author:	Anders Kvanvig
"""

# Users get added in dictionary, on the right side the tasks along with their corresponding point will be added
# User : { task : reward }
chores = {
    'him': {}, 'her': {}, 'notFinished': {}
}

# Creates task given name and number of points recived when finished (Is added to the 'notFinished' user)
def addTask(task, points):
    chores['notFinished'].update({
        task: points
    })
    print('Chore added (' + task + ',' + str(points) + ')')

# Gets the points from the finished task, and delete the entry in the notFinished dictionary
# Then the given user is awarded the task and points
def finishedTask(user, task):
    points = chores['notFinished'].get(task, 0) #retrieves points
    chores['notFinished'].pop(task)             #delete current entry
    chores[user].update({
        task: points
    })                                          #gives user their points
    print('The task "' + task + '" has been finished by ' + user + ' rewarding them ' + str(points) + ' points')

# Collects scores for each user, and checks for a winner
def checkScores():
    Scores = {
        'him':0, 'her': 0, 'notFinished': 0
    }
    for user in Scores:
        for key, value in chores[user].items():
            Scores[user] += value

    print(Scores)
    print('-------------------------')
    if Scores['him'] == 0:
        print('her has just filed for a divorce')
    elif Scores['her'] == 0:
        print('him has just filed for a divorce')
    if Scores['notFinished'] > Scores['him'] and Scores['notFinished'] > Scores['her']:
        print('Try a bit harder next time')
    return

def end():
    print('-------------------------')
    print('The challenge has ended')
    checkScores()

# Adding chores for them to complete
addTask('Take out the trash', 1)
addTask('Wash clothes', 3)
addTask('Grocery shopping', 2)
addTask('Clean kitchen', 2)
addTask('Vacuuming', 2)
addTask('Washing the dishes', 1)
addTask('Dusting', 1)

# Let them finish a few tasks
finishedTask('him', 'Take out the trash')
finishedTask('him', 'Vacuuming')

end()
