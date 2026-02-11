import numpy as np
import numpy.random as random
rng = np.random.default_rng()

number = rng.integers(0,101)

x = True

while x:
    guess = int(input('Guess a Number between 0 and 100: '))
    if(guess - number > 30):
        print('too high')
    elif(0 < guess - number < 30):
        print('lower')
    elif(number - guess > 30):
        print('too low')
    elif(30 > number - guess > 0):
        print('higher')
    else:
        print('you guessed the correct number!!')
        x = False
