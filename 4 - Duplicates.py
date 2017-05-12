'''
This program stores 30 randomly generated numbers between 1 and 99 and displays all numbers stored and the set of unique numbers 

Imports the random module.
Stores a random value from 1 - 99 into the list and repeats this process 30 times.
Then prints the list to display all values stored in the list in the order they were entered.
Sorts the list for readability.
Finally, it uses the set function to print only the non-duplicate values.
'''
import random


# Stores random numbers in the list and repeats 30 times
mylist = [(random.randint(1, 100)) for k in range(30)]

# Prints the original list
print(mylist)

# Sorts and reprints the list
print(sorted(mylist))

# Prints the unique values from the list
print(set(mylist))