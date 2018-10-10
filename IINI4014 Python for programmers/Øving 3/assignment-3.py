"""
	Title:	assignment-3.py
	Date:	12.09.2017
	Author:	Anders Kvanvig
"""

import turtle
window = turtle.Screen()
asgeir = turtle.Turtle() #creates a turtle named 'asgeir'

#Settings
rad = -300          #Sets the radius to negative 100 so that the circle is drawn clockwise
points = 200     	#Sets the number of points on the circleline
multiplier = 15      #Sets the number everything should be multiplied with
asgeir.speed(0)     #Sets the speed of the turtle (1: slowest, 6: standard, 10: fast, 0: fastest)

dpp = 360 / points  #Degrees pr Point

asgeir.penup()          #Lifts the pen to avoid drawing while moving
asgeir.setpos((rad), 0) #Changes the position so that the centre of the circle is at (0,0)
asgeir.pendown()        #Lowers the pen to start drawing again
asgeir.left(90)         #Turns 90 degrees to the left

i = 0
posX = [0] * points         #List to store X-coordinates
posY = [0] * points         #List to store Y-coordinates


#Draws the circle itself and the red dots
while i < points:
    asgeir.circle(rad, dpp) #Draws one fraction of the circle
    asgeir.dot(7, 'red')    #Puts down a red dot
    posX[i] = asgeir.xcor() #Saves the X-coordinate of each point for easier navigation
    posY[i] = asgeir.ycor() #Saves the Y-coordinate of each point for easier navigation
    print('(' + str(posX[i]) + ',' + str(posY[i]) + ')')    #Print position of each point
    i += 1


#Draws multiplier values from each point, the lines across
for i in range(0,points):
    #Moves asgeir to the point of origin
    asgeir.penup()
    asgeir.goto(posX[i],posY[i])    #Moves turtle from current position to target
    asgeir.pendown()

    #Gets index for target
    x = (i * multiplier) % points

    #Draws line between points
    asgeir.goto(posX[x],posY[x])


window.exitonclick()
