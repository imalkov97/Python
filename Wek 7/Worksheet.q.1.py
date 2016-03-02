#Q1

#(a) What are the differences between the functions sys.stdout.write and print?

print('''
We can see that 'sys.stdout.write' does not break the line while 'print' does.
''')

import sys
sys.stdout.write("Hello")
print("Hello")



#(b)

print('''
We can see that the input function has an extra step which uses the keyboard input and creates a string.
'sys.stdout.read()' does not have this extra step, it simply uses all the keyboard input (including spaces)
until the user inputs the special character.
''')

i = input("Hello there, enter your text : ")
print("i =",i,)

r = sys.stdin.read()
print("r =",r,)

