passwordTuple = ("123456", "123456789", "qwerty", "password", "admin")

def password():
    attempts = 5
    x = 0
    while attempts != 0 and x != 1:
        pwdinput = input("Password: ")
        for i in passwordTuple:
            if pwdinput == i:
                print("Correct")
                x = 1
        if x == 0:
            print("Try again")
            attempts = attempts - 1
            print(str(attempts)+" attempts left")

password()
