def choice():
    option=input('''
    Would you like to proceed?
    Choose your option by entering the number.
    
    1  Yes
    2  No
    
    '''
          )
    
    if option == "1":
        print("You will proceed")
    elif option == "2":
        print("You will not proceed")
    else:
        print("Incorrect option")
# Is there any way to pause this? Require the user to press enter in order to contiune?        
        choice()


choice()
        
        
