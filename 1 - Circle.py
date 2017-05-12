'''
This program calculates the area, circumference, and diameter of a circle when given a radius.

Imports the math module.
Builds a class to perform the calculations of determining the
area, circumference, and diameter of a circle and rounds the return to 4 decimal places.
Prompts the user to enter a radius.
Prints the result with the value of the return from the class cast as a string.
'''

import math

class Circle():
    '''
    Defines a method for the area, circumference, and diameter of a circle.
    '''
    def __init__(self,r):
        self.radius = r

    def cir_area(self):
        return round(math.pi*(self.radius**2),4)

    def cir_circ(self):
        return round(((2*math.pi)*self.radius),4)

    def cir_diameter(self):
        return round((2*self.radius),4)

# Creates a new instance of the Circle class and prompts the user for input
newCircle = Circle(int(input("Enter a radius:")))

# Prints the area, circumference, and diameter of a circle
print("The area of the circle is " + str(newCircle.cir_area()))
print("The circumference of the circle is " + str(newCircle.cir_circ()))
print("The diameter of the circle is " + str(newCircle.cir_diameter()))