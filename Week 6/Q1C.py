#Q 1) c)



diceSumDict = {}
for die1 in range(1,7):
    for die2 in range(1,7):
        sum = die1+die2
        if sum in diceSumDict:
            diceSumDict[sum].append( (die1,die2) )
        else:
            diceSumDict[sum] = [ (die1,die2) ]

for key in diceSumDict:
    print(key, diceSumDict[key])
            
