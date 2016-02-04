#Labsheet 2
#Question 5
hoursStr=input("How many hours?")
inpHours=int(hoursStr)
minutesStr=input("How many minutes?")
minutes=int(minutesStr)
currHours=inpHours
midi="in the morning."
periodHour=''
#-------------------------------------------------------------
#this bit checks if the user enters hours and minutes that are valid
if (minutes<0) or (minutes>59):
    print('The time you entered is invalid. Please try again!')
elif (inpHours<0) or (inpHours>23):
    print('The time you entered is invalid. Please try again!')
#-------------------------------------------------------------
else:
#three main variables that will form our final string:
    #  midi - tells us if it is morning or afternoon
    #  periodHour - tells us what period in an hour we are in(half past, quarter to etc)
    #  currHours - tells us at what hour we have to approximate the input
 
    if inpHours==12:
        midi="in the afternoon."
        currHours=inpHours
    elif inpHours>12:
        currHours=inpHours-12
        midi="in the afternoon."
    if (minutes>=53) and (minutes<=59):
        if (inpHours==12) or (inpHours==0):
            currHours=1
        else:
            currHours=currHours+1
            if inpHours==11:
                midi='in the afternoon.'
            elif inpHours==23:
                midi='in the morning.'
    elif (minutes>=38) and (minutes<=52):
        periodHour='quarter to '
        if (inpHours==12) or (inpHours==0):
            currHours=1
           
        else:
            currHours=currHours+1
           
    elif (minutes>=8) and (minutes<=22):
        periodHour='quarter past '
    elif (minutes>=23) and (minutes<=37):
        periodHour='half past '
#This bit transforms the integer currHours into the word representing the number
#It also prints the message
    numToWords=['twelve ', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine ', 'ten ', 'eleven ', 'twelve']
    timeOfDay='The time is about ' + periodHour + numToWords[currHours] + midi
    print(timeOfDay)
