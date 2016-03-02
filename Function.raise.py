def myName():
    #print("Function-Start", name)
    #global name
    name='Jim'
    print("Function-End", name)


name = 'Simon'
print("Main-Before", name)
myName()
print("Main-After", name)
