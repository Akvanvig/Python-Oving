"""
	Title:	testMultipleTurtle.py
	Date:	07.03.2018
	Author:	Anders Kvanvig
"""

import turtle
import threading

#Settings
rad = -350              #Sets the radius to negative 100 so that the circle is drawn clockwise
numPoints = 200      	#Sets the number of points on the circleline (Should be divisible by number of turtles)
multiplier = 4          #Sets the number everything should be multiplied with
countTurtles = 2        #Number of turtles used
turtleSpeed = 0         #Sets the speed of the turtle (1: slowest, 6: standard, 10: fast, 0: fastest)
dpp = 360 / numPoints   #Degrees pr Point
posTurtle = [] * countTurtles   #[posx,posy,heading,dpp,numpointsleft]
finishedTurtle = [False] * countTurtles

def circleLine(rudolf, startPosX, startPosY, directionFromEast, degPP, numPoints, radius):
    #Moves turtle to starting position
    points = [0] * numPoints
    i = 0
    rudolf.penup()
    rudolf.setpos(startPosX, startPosY)
    rudolf.right(directionFromEast)
    rudolf.pendown()

    #Draws its part of the circle and puts down points
    while i < numPoints:
        rudolf.circle(radius, degPP)
        rudolf.dot(7,'red')
        points[i] = [rudolf.xcor(), rudolf.ycor()]
        print(points[i])
        i += 1

    return points


window = turtle.Screen()
turtles = [turtle.Turtle()] * countTurtles
points = [] * countTurtles
tmpStartX = [rad,-rad]
tmpStartY = [0,0]
tmpDirFromEast = [270, 90]

for i in range(0,countTurtles):
    points[i].append(circleLine(turtles[i], tmpStartX[i], tmpStartY[i], tmpDirFromEast[i], dpp, numPoints))

turtleMoved = True
while turtleMoved:
    turtleMoved = False
    for i in range(0,countTurtles):
        if finishedTurtle == False:

    if condition:
        pass

window.exitonclick()
