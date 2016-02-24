width=input("Enter the width of your tree (Odd numbers only!)")
length=input("Enter the length of the tree trunk")

w=int(width)
l=int(length)

t=("*") #The character used to display the tree
r=(1) #The start of the tree (top)
n=(1) #The number of rows of the tree trunk
e=(3) #The number of "*" character columns in the tree trunk


while (r*t)<(w*t):
    print (r*t)
    r = r + 2


while n<l:      
    print (e*t)
    n = n + 1 
