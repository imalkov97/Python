#4



def numToDay(n):
    Mtup =(" ","Mon","Tue","Wed","Thu","Fri","Sat","Sun")
    if n>7:
        raise ValueError("There are only 7 days!")
    if type(n) is not int:
        raise TypeError("You did not enter a number!")
    else:
        return(Mtup[n])

print(numToDay(6))
