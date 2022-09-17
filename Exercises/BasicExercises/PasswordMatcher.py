passwordTuple = ("123456", "123456789", "qwerty", "password", "admin")
def passwordInput():
    pwdinput = input("Password: ")
    if pwdinput == passwordTuple(0) or pwdinput == passwordTuple(1) or pwdinput == passwordTuple(2) or pwdinput == passwordTuple(3) or pwdinput == passwordTuple(4):
        print("Correct")
        passwordInput()
    else:
        print("Incorrect, try again")
        passwordInput()
