#2) a) Write a function which takes a string with a text file name;
#      and reverses the order in which the lines of text are written in the file.

f = open("Boring.txt","r")
for line in f:
    print(line)
f.close()
