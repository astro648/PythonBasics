import random as r


def randnumgame(myInput):
    solution = r.randint(0, 10)
    print("--")
    print("Random number generated from 0 to 10, input answer:")

    if myInput != solution:
        print("Wrong number")
        randnumgame()
    else:
        print("Correct number")
        randnumgame()


myInput = int(input())  # making it a parameter
randnumgame(myInput)
