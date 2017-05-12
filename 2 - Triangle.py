'''
This program calculates the hypotenuse of a right triangle when given the other 2 sides that are less than 20.

Imports the math module.
Prompts the user to enter a value for side a and side b.
Checks if the user input is less than 20
If the sides are greater than 20 the user is prompted again until the input is valid.
When the input is valid the calculations are performed and printed to the screen.

'''

import math

#a^2 + b^2 = c^2

# Prompts the user for input
a = int(input("Enter a value not greater than 20 for side a: "))
b = int(input("Enter a value not greater than 20 for side b: "))

# Inputs are limited to values less than 20
while a > 20 and b > 20:
    print("Invalid Entry. Enter new numbers not greater than 20.")
    a = int(input("Enter a value not greater than 20 for side a: "))
    b = int(input("Enter a value not greater than 20 for side b: "))
else:
    # if a <= 20 and b <=20:
    c2 = a ** 2 + b ** 2
    c = math.sqrt(c2)
    print("a^2 =", a ** 2)
    print("b^2 =", b ** 2)
    print("c^2 =", c2)
    print("The hypotenuse =", round(c, 4))