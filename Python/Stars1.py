def draw_stars(list):
    for num in list:
        print '*' * num

# test function
x = [4, 6, 1, 3, 5, 7, 25]
print 'The example list is: {}'.format(x)
draw_stars(x)
