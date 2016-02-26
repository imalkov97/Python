#Q6 Write a function isThisAWord(S) which takes a string S and returns the appropriate Boolean.


f = open ("words.txt","r")

words_list = []

for line in f:
    text = str(line)[0:-1]
    words_list.append(text)



wInput = input("Enter your word : ")
word = str(wInput)

def isThisAWord(S):
    if word in words_list:
        print(True)
    else:
        print(False)

isThisAWord(word)

    
