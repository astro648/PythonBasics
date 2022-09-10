print("Input grade:")
grade = int(input()) # this makes the input an integer
if grade == 4:
    print("A")
elif grade == 3:
    print("B")
elif grade == 2:
    print("C")
elif grade == 1:
    print("D")
elif grade == 0:
    print("F")
else:
    print("Grade invalid, type in 4, 3, 2, 1, or 0")