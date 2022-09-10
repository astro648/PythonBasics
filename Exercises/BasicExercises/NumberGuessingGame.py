import random as r

def randnumgame():
    randnum = r.randint(0, 10)
    print("--")
    print("Random number generated from 0 to 10, input answer:")
    solution = int(input())
    if solution != randnum:
        print("Wrong number")
        randnumgame()
    else:
        print("Correct number")
        randnumgame()

randnumgame()
