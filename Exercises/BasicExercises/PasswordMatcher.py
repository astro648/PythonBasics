passwordTuple = ("123456", "123456789", "qwerty", "password", "admin")

def passwordInput():
    x = 0
    pwdinput = input("Password: ")
    for i in passwordTuple:
        if pwdinput == i:
            print("Correct")
            x = 1
    if x == 0:
        print("Try again")
        passwordInput()
passwordInput()
