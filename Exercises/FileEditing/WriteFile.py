lines = ['Lorem ipsum dolor sit amet', 'Python']  # This is a list of things to write
with open('write.txt', 'a') as f:  # If you write in a previous file, the data that is in it will be overwritten
    # However, we are in 'a' mode, which 'appends' more data to the end.
    for l in lines:  # cycles through list
        f.writelines(l + '\n')  # \n makes newline
f.close()
