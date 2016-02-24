#  Save your dictionary from Q1c into a file
#  and then access it from a separate Python session.

import pickle
f = open("Dictionary.txt","rb")
dice = pickle.load(f)
f.close()

print(dice.keys())
