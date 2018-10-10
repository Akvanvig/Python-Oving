"""
	Title:	assignment-7.py
	Date:	21.10.2017
	Author:	Anders Kvanvig
"""
import math

class Circle(object):                       #New class Circle
    """ An advanced circle analytic toolkit """

    #Flyweight design pattern suppresses
    #the instance dictionary
    __slots__ = ['diameter']
    version = '0.7'                        #class variable

    def __init__(self,radius):
        self.radius = radius                #Instance variable (Places value in dictionary)

    def area(self):
        #Perform quadrature on a shape of uniform radius
        p = self.__perimeter()
        r = p / math.pi / 2.0
        return math.pi * self.radius ** 2.0

    def perimeter(self):
        return 2.0 * math.pi * self.radius

    __perimeter = perimeter

    @classmethod                            #Alternative Constructor
    def from_bbd(cls, bbd):
        """ Construct a circle form a bounding box diagonal """
        radius = bbd / 2.0 /math.sqrt(2.0)
        return cls(radius)

    @staticmethod                           #Attach functions to classes
    def angle_to_grade(angle):
        """ Converts angle in degree to percentage grade """
        return math.tan(math.radians(angle)) * 100.0

    @property                               #Converts dotted access to method calls
    def radius(self):
        """ Radius of a circle """
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0



class Tire(Circle):                         #New class Tire
    """ Tires are circles with corrected perimeter """

    def perimeter(self):
        return Circle.perimeter(self) * 1.25

    __perimeter = perimeter



def circleTest():
    print('Circuitous version', Circle.version)
    c = Circle(10)
    print('A circle of radius', c.radius)
    print('has an area of', c.area())
    print()

def academia():
    import random

    random.seed(83665478)
    print('Using Circuituos(tm) version', Circle.version)
    n = 10
    circles = [Circle(random.random()) for i in range(n) ] #xrange does not seem to be a thing in python 3
    print('The average area of', n, 'random circles')
    avg = sum([c.area() for c in circles]) / n
    print(('is {}').format(str(avg)))
    print()

def rubberSheet():
    cuts = [0.1, 0.7, 0.8]
    circles = [Circle(r) for r in cuts]
    for c in circles:
        print(('A circlet with a radius of {}').format(c.radius))
        print(('has a perimeter of {:3f}').format(c.perimeter()))
        print(('and a cold area of {:3f}').format(c.area()))
        c.radius *= 1.1
        print(('and a warm area of {:3f}').format(c.area()))
        print()

def tireChain():
    t = Tire.from_bbd(45)
    print(('A tire of radius {:3f}').format(t.radius))
    print(('has an inner area of {:3f}').format(t.area()))
    print(('and an odometer corrected perimeter of {:3f}').format(t.perimeter()))
    print()

def graphics():
    bbd = 25.1
    c = Circle.from_bbd(bbd)
    print('A circle with a bbd of {}'.format(str(bbd)))
    print('has a radius of {:3f}'.format(c.radius))
    print('and an area of {:3f}'.format(c.area()))
    print()

def angleToGrade():
    angle = 5.0
    print('A {:.3} angle is equivalent to a {:.3} % grade'.format(angle, Circle.angle_to_grade(angle)))
    print()



circleTest()
academia()
rubberSheet()
tireChain()
graphics()
angleToGrade()
