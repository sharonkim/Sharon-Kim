'''
Challenge: Build a function that takes in a dictionary. Print the key and value
of each key-value pair like so:

    Your dictionary has the following inside:
    key1 : value1
    key2 : value2
    key3 : value3
    ...

Authors: Brandon, Sharon, Fabian
Tutor: Jonathan
Date: 01/10/2016
'''

# Defining the function
def challenge3(dictionary):
    # Print informative text
    print "Your dictionary has the following inside:""
    # Looping through the dictionary elements
    for element in dictionary:
        # print the key value pairs in the needed format
        print element,":",dictionary[element]



# Testing the function
x = {
    "Name":"Fabian",
    "Age":"Mystery",
    "City":"Heredia",
    "Continent":"America",
    "LastName":"Sanchez"
}

challenge3(x)
