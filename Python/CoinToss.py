import random
random_num = random.random()
# the random function will return a floating point number,
# that is 0.0 <= random_num < 1.0

def coinToss():
    heads = 0
    tails = 0
    for toss in range(1, 5001):
        if random.random() < 0.5:
            face = 'tails'
            tails += 1
        else:
            face = 'heads'
            heads += 1

        print 'Attempt #{}: Throwing a coin... It's a {}!...Got {} head(s) so far and {} tail(s) so far'.format(toss, face, heads, tails)
    print 'Ending the program, thank you!'

# test function
coinToss()
