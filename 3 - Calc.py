'''
This program randomly generates 2 numbers and prompts the user for the sum of those numbers.

Imports the random module.
Generates 2 numbers between 1 and 9.
Stores the answer of the sum of the 2 numbers.
Prompts the user to enter the answer.
Checks if the user response is equal to the answer.
If the answer is incorrect the user is prompted again until the answer is correct.
When the answer is correct the user receives a message.

'''

import random

x = random.randint(1,10)
y = random.randint(1,10)

# The result of x + y
answer = x+y

# Stores the user response
response = input("What is " + str(x) + " + " + str(y)+":")

# If the user response is not equal to the answer, try again
while int(response) != answer:
    #response = int(input("Enter a guess: "))
    print("Yor answer is incorrect")
    response = input("What is " + str(x) + " + " + str(y)+":")
else:
    print("Yeah!!!")