passwordTuple = ("123456", "123456789", "qwerty", "password", "admin")


def passwordInput():
    pwdinput = input("Password: ")
    for x in passwordTuple:
        if x < 4:
            if pwdinput == passwordTuple(x):
                print("Correct")
            else:
                x = x + 1
        else:
            print("Incorrect, try again")
            passwordInput()
