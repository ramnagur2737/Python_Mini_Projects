import numpy as np
import numpy.random as random
rng = np.random.default_rng()



def func():
    print("helo")
    number = rng.integers(1,4)
    print("whats your choice")
    print("1 for Rock")
    print("2 for Scissors")
    print("3 for Paper")
    m = int(input("enter you choice :) :- \n"))
    if number == m:
        print("its a tie!!!!")
    elif m == 1:
        if number ==2:
            print("the computer chose scissors")
            print("you won!! :)")
        elif number==3:
            print("the computer chose paper")
            print("you lost! :(")
    elif m == 2:
        if number ==1:
            print("the computer chose rock")
            print("you lost! :(")
        elif number==3:
            print("the computer chose paper")
            print("you won!! :)")
    elif m == 3:
        if number ==1:
            print("the computer chose rock")
            print("you won!! :)")
        elif number==2:
            print("the computer chose scissor")
            print("you lost! :(")
    x = input("do you wanna play again?")
    if x== 'Y' or x == 'y':
        print("yay")
        func()
    elif x == 'N' or x == 'n':
        print(":(")
        return

print("the computer chose paper")



x = input("hello!! wanna play rock paper scissors? (Y for yes, N for no)\n")
if x== 'Y' or x == 'y':
    print("yay")
    func()
elif x == 'N' or x == 'n':
    print(":(")
else:
    print(":(")
