def draw_stars(list):
    for num in list:
        if type(num) is int:
            print '*' * num
        elif:
            type(num) is str:
            attempts = len(num)
            print num[0].lower() * attempts

# test function
x = [4, 'Tom', 1, 'Michael', 5, 7, 'Jimmy Smith']
print 'The example list is: {}'.format(x)
draw_stars(x)
