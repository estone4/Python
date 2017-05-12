'''
This program calculates the area and perimeter of a square or rectangle when given a length and a width.

Builds a class to perform the calculations to determine the area and perimeter of a square or rectangle 
and rounds the return to 4 decimal places.
Prompts the user to enter a length and a width.
Prints the result with the value of the return from the class cast as a string.
'''

class Rectangle():
    '''
    Defines a method for the area and perimeter of a rectangle
    If length and width are not entered, the class uses static values of 0,0 for the top left corner and 5,5 for the bottom right corner.
    '''
    def __init__(self,l=0,w=0,tl=(0,0),br=(5,5)):
        self.length = l
        self.width = w
        self.x1, self.y1 = tl
        self.x2,self.y2 = br
        self.x = abs(int(self.x1) - int(self.x2))
        self.y = abs(int(self.y1) - int(self.y2))

    def rectangle_area(self):
        if self.length != 0 and self.width != 0:
            return self.length*self.width
        else:
            return self.x * self.y

    def rectangle_perimeter(self):
        if self.length != 0 and self.width != 0:
            return ((self.length*2)+(self.width*2))
        else:
            return (self.x * 2) + (self.y * 2)

newRectangle = Rectangle(int(input("Enter a length:")),int(input("Enter a width:")))
print("The area is " + str(newRectangle.rectangle_area()))
print("The perimeter is " + str(newRectangle.rectangle_perimeter()))