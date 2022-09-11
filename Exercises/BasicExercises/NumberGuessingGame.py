import random as r


def RandNumGame(myInput):
    solution = r.randint(0, 10)
    print("--")
    print("Random number generated from 0 to 10, input answer:")

    if myInput != solution:
        print("Wrong number")
        RandNumGame()
    else:
        print("Correct number")
        RandNumGame()


myInput = str(input())  # making it a parameter
RandNumGame(myInput)
