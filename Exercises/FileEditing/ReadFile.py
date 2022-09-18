f = open("lipsumpar.txt")
# line = f.readline()
for line in f:
    print(line.strip())

f.close()
