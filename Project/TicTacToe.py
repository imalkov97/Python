print("Welcome to Ivan Malkov's Naughts and Crosses!")

gamemode=input(
'''
Enter one of the following numbers in order to select its corresponding option

1. Tutorial
2. 1 player 
3. 2 players

: '''
              )
def singleplayer()
    teamchoice=input(
    '''
    Please select what you would like to play as.
    Type 1 for Naugths: X
    Type 2 for Crosses: O
    '''
      )
    print()
    if  (teamchoice)==("1"):
        (teamchoice)="X"
        print("You will play as Naughts! ( X )")
    elif (teamchoice)==("2"):
        (teamchoice)="O"
        print("You will play as Crosses! ( O )")        
    else:
        print("You only have 2 options... 1 and 2")
    print(
    '''
____________________________________________________

This is the game grid.


    1   2   3
    
a  |   |   |   |
    --- --- ---
b  |   |   |   |
    --- --- ---
c  |   |   |   |

____________________________________________________
'''
     )

print("Which cell would you like to fill?")
placement=input("Enter the grid coordinates:" " ")

if (placement)==("a1") or ("1a") or ("A1") or ("1A"):
    print("____________________________________________________")
    print()
    print("1   2   3")
    print("a  | "(teamchoice))
    print("--- --- ---")
    print("b  |   |   |   |")
    print("--- --- ---")
    print("c  |   |   |   |")


#def GridCalc(letter,number):
 #   if letter == "a" or "A" or "b" or "B" or "c" or "C"
  #  number == "1" or "2" or "3":
    
    

