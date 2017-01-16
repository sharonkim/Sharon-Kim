'''
Challenge: Build a function that takes in a list of numbers and a value. Multiply each
number in the list by the value given and return the updated list.

Authors: Brandon, Sharon, Fabian
Tutor: Jonathan
Date: 01/10/2016
'''

# Defining the function
def challenge1(list, times):
    # Looping thorugh the list
    for index in range(0,len(list)):
        # Modifying the values of the list "n" times according to the times value
        # passed as argument
        list[index] = list[index] * times

# Testing the function
x = [1,2,3,4,5,6]
challenge1(x,5)
print x
