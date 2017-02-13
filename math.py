class Math(object):

    def __init__(self):
        self PI = 3.14

    def round(self, number):
        if number % 1 >= 0.5:
            number = int(number) + 1;
        else:
            number = int(number)
