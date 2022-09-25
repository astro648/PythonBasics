import os.path
fileExist = os.path.exists("e.txt")
if fileExist is True:
    f = open("lipsumpar.txt")
    # line = f.readline()
    for line in f:
        print(line.strip())
    f.close()
else:
    print("File does not exist")