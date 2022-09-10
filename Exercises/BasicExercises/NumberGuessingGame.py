import random as r
i = 0
while i < 10:
    randnum = r.randint(0, 10)
    print("Random number generated from 0 to 10, input answer:")
    solution = input()
    while solution != randnum:
        print("Wrong number, new round")
        exit
