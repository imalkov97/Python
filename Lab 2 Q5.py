hours = input ("Please enter the number of hours") 
minutes = input ("Please enter the number of minutes") 

h=int(hours)
m=int(minutes)
t=(1)
d=(2)

#no more than 23 hours can be displayed
if (h>23):
    raise(
    "No more than 23 hours can be displayed"
    )

#no less than 0 hours can be displayed
if (h<0):
    raise(
    "No less than 0 hours can be displayed"
    )

#no more than 59 minutes can be displayed
if (m>59):
    raise(
    "No more than 59 minutes can be displayed"
    )

#no less than 0 minutes can be displayed
if (m<0):
    raise(
    "No less than 0 minutes can be displayed"
    )

#morning, afternoon, evening or night variables
if (h>=23 or h<=4):
    t=(1)
if (5<=h or h<=11):
    t=(2)
if (12<=h<=16):
    t=(3)
if (18<=h or h<=22):
    t=(4)


#around the hour
if (52<=m<=59) or (0<=m<=6):
    m=""
if (52<=m<=59) or (0<=m<=6):
    (h+1)    

#quarter past
elif (7<=m<=22):
    m="quarter past"

#half past
elif (23<=m<=37):
    m="half past"

#quarter to
elif (38<=m<=51):
    m="quarter to"
elif (38<=m<=51):
    h+1


#number of hours to words
if (h==0):
    d=("twelve")
if (h==1):
    d=("one")
if (h==2):
    d=("two")
if (h==3):
    d=("three")
if (h==4):
    d=("four")
if (h==5):
    d=("five")
if (h==6):
    d=("six")
if (h==7):
    d=("seven")
if (h==8):
    d=("eight")
if (h==9):
    d=("nine")
if (h==10):
    d=("ten")
if (h==11):
    d=("eleven")
if (h==12):
    d=("twelve")
if (h==13):
    d=("one")
if (h==14):
    d=("two")
if (h==15):
    d=("three")
if (h==16):
    d=("four")
if (h==17):
    d=("five")
if (h==18):
    d=("six")
if (h==19):
    d=("seven")
if (h==20):
    d=("eight")
if (h==21):
    d=("nine")
if (h==22):
    d=("ten")
if (h==23):
    d=("eleven")

    

#morning, afternoon, evening or night allocation

if (t==1):
    t="morning"
elif (t==2):
    t="afternoon"
elif (t==3):
    t="evening"
elif (t==4):
    t="night"





print("The current time is about",m,d,"in the",t)






























