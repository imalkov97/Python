#1) a) Create a function which accepts a number between 1 and 12 and returns
#      the name of the month in text. Use tuples in the implementation.

m = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")

numInput = input("Enter your number (1-12)")
num = int(numInput)

if num>12:
         print("Incorrect number entered")
elif num<=0:
         print("Incorrect number entered")
else:
         if num==1:
             print(m[0])
         elif num==2:
             print(m[1])
         elif num==3:
             print(m[2])
         elif num==4:
             print(m[3])
         elif num==5:
             print(m[4])
         elif num==6:
             print(m[5])
         elif num==7:
             print(m[6])
         elif num==8:
             print(m[7])
         elif num==9:
             print(m[8])
         elif num==10:
             print(m[9])
         elif num==11:
             print(m[10])
         elif num==12:
             print(m[11])
        
    
