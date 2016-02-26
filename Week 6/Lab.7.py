#Q7 An anagram of a word is another formed from the same letters. For example, parse and spare are
# anagrams. Create a dictionary where the keys are tuples of letters and the values anagrams they create.
# In Scrabble a player receives a bonus if they play all 7 of their tiles at once, creating an 8 letter word
# (combining with one tile on the board). Which group of 8 letters can create the most words?

f = open ("words.txt","r")

words_list = []

#for line in f:
#    text = str(line)[0:-1]
#    words_list.append(text)




for line in f:
    text = str(line)[0:-1]

    tupT = (text)

    
    scrDict = {}
    scrDict [tupT] = (text)[::-1]

    if scrDict

    
    print(scrDict)





