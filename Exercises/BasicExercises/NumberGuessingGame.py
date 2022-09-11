import random as r


def RandNumGame():
    randnum = r.randint(0, 10)
    print("--")
    print("Random number generated from 0 to 10, input answer:")
    solution = int(input())
    if solution != randnum:
        print("Wrong number")
        RandNumGame()
    else:
        print("Correct number")
        RandNumGame()


RandNumGame()
