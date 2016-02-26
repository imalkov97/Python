#Labsheet 5

f = open ("words.txt","r")

words_list = []

for line in f:
    text = str(line)[0:-1]
    words_list.append(text)
    
    print(words_list)
