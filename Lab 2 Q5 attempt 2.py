hours = input ("Please enter the number of hours ") 
minutes = input ("Please enter the number of minutes ") 

h=int(hours)
m=int(minutes)

y=("timeofday")

if (h>23):  #no more than 23 hours can be displayed                                     
    raise(
    "No more than 23 hours can be displayed"
    )

if (h<0):   #no less than 0 hours can be displayed
    raise(
    "No less than 0 hours can be displayed"
    )

if (m>59):  #no more than 59 minutes can be displayed
    raise(
    "No more than 59 minutes can be displayed"
    )

if (m<0):   #no less than 0 minutes can be displayed
    raise(
    "No less than 0 minutes can be displayed"
    )

if (0<=h<=11):
    y=("am")
          
if (12<=h<=23):
    y=("pm")    



print("the time is",h,":",m,y)   #print with am/pm

t=("time")  #morning, afternoon, evening or night variables                 
d=("time display")

if (5<=h<=11):
    t=(1)
if (12<=h<=16):
    t=(2)
if (17<=h<=21):
    t=(3)
if (22<=h<=23) or (h==0) or (1<=h<=3):
    t=(4)

if (t==1):
    d="morning"
    
if (t==2):
    d="afternoon"
    
if (t==3):
    d="evening"
    
if (t==4):
    d="night"

print("the time is",h,":",m,"in the",d) #print with day time

w=("words") #number of hours to words

if (h==0):   
    w=("twelve")
if (h==1):
    w=("one")
if (h==2):
    w=("two")
if (h==3):
    w=("three")
if (h==4):
    w=("four")
if (h==5):
    w=("five")
if (h==6):
    w=("six")
if (h==7):
    w=("seven")
if (h==8):
    w=("eight")
if (h==9):
    w=("nine")
if (h==10):
    w=("ten")
if (h==11):
    w=("eleven")
if (h==12):
    w=("twelve")
if (h==13):
    w=("one")
if (h==14):
    w=("two")
if (h==15):
    w=("three")
if (h==16):
    w=("four")
if (h==17):
    w=("five")
if (h==18):
    w=("six")
if (h==19):
    w=("seven")
if (h==20):
    w=("eight")
if (h==21):
    w=("nine")
if (h==22):
    w=("ten")
if (h==23):
    w=("eleven")


#around the hour
if (52<=m<=59) or (0<=m<=6):
    m=""
    

#quarter past
elif (7<=m<=22):
    m="quarter past"

#half past
elif (23<=m<=37):
    m="half past"

#quarter to
elif (38<=m<=51):
    m="quarter to"


print("The time is about",m,w,"in the",d)

























