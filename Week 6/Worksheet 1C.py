#1) c) Consider rolling two 6-sided dice and calculating the sum.
#      Create a dictionary whose keys are the possible sums and values
#      those combinations which add to the sum. Which sum is the most likely?

import pickle
f = open("Dictionary.txt","wb")

dice = {2:1+1,2:1+1,3:1+2,3:2+1,4:2+2,4:2+2,5:2+3,5:3+2,6:3+3,6:3+3,7:4+3,7:3+4,8:4+4,8:4+4,9:5+4,9:4+5,10:5+5,10:5+5,11:5+6,11:6+5,12:6+6,12:6+6}

print(list(dice.keys()))
print(list(dice.values()))

pickle.dump(dice,f)
f.close()

