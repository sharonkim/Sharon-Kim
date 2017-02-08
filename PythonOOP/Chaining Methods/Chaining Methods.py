class Bike(object):

    def __init__(self, miles = 0):
        self.price = 200
        self.max_speed = '25mph'
        self.miles = miles

    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles

    def ride(self):
        print 'Riding'
        self.miles += 10

    def reverse(self):
        print 'Reversing'
        if self.miles - 5 < 0:
            print 'No reversing allowed'
        else:
            print 'Reversing'
            self.miles -= 5

bike1 = Bike(200, '25mph')
bike2 = Bike(400, '45mph')
bike3 = Bike(300, '35mph')

bike1.ride().ride().reverse().displayInfo()
bike2.ride().ride().ride().reverse().displayInfo()
bike3.ride().ride().ride().reverse().displayInfo()

return self
