'''
Challenge: Create a function that will examine the range of numbers from 1 to
100. If a number is divisible by 3, print “fizz”, if a number is divisible by
5, print “buzz”, if a number is divisible by 3 and 5, print “fizzbuzz”

Authors: Brandon, Sharon, Fabian
Tutor: Jonathan
Date: 01/10/2016
'''
# Original function built by the team
def challenge2():
    # Looping through the requested range
    for i in range(1,101):
        # Print number to evaluate
        print i,
        # Comparing if both conditions are met at the same time
        if i % 3 == 0 and i % 5 == 0:
            print "fizzbuzz"
        # Otherwise check if divisible by 5
        elif i % 5 == 0:
            print "buzz"

        # Or if divisible by 3
        elif i % 3 == 0:
            print "fizz"


# Additional function with only 2 evaluations. No sure if performs worse,
# better or like the previous one
def challenge2_1():
    # Looping through the requested range
    for i in range(1,101):
        # Resetting fizz and buzz values
        fizz = ""
        buzz = ""
        # If divisible by 5 set the buzz value
        if i % 5 == 0:
            buzz = "buzz"
        # If divisible by 3 set the fizz value
        if i % 3 == 0:
            fizz = "fizz"
        # Print the number evaluated and fizz and buzz values at this point
        print "{} {}{}".format(i,fizz,buzz)


# Testing the functions
# challenge2()
challenge2_1()
