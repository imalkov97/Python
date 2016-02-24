print("Welcome to Ivan Malkov's Naughts and Crosses!")

gamemode=input(
'''
This is the main menu!
Enter one of the following numbers in order to select your option

1. Tutorial
2. Singleplayer 
3. Multiplayer

:  '''
              )


def menu_tut():
    print("You have selected to view the tutorial!")
    tutorial()

def menu_sp():
    print("You have selected to play singeplayer!")
    team_select_sp()
    play_turn()
def menu_mp():
    print("You have selected to play multiplayer!")
    team_select_mp()

#Function used to present the menu tutorial
def tutorial():
    print(
            '''
____________________________________________________


This is your game grid.


    1   2   3
    
a  |   |   |   |
    --- --- ---
b  |   |   |   |
    --- --- ---
c  |   |   |   |

____________________________________________________
'''
            )

#Function used in SinglePlayer team selection 
def team_select_sp():
    teamchoice=input(
    '''
    Please select your team:

    1.  Naugths  O
    2.  Crosses  X
    
    (Type 1 or 2)

    :'''

    )
    if (teamchoice)=="1":
        (teamchoice)="O"
        print("You will play as Crosses! ( X )")
    elif (teamchoice)=="2":
        (teamchoice)="X"
        print("You will play as Naughts! ( O )")        
    else:
        print("You only have 2 options... 1 and 2")

#Asks whether you will go 1st or 2nd
def play_turn():
    turn=input(
'''Would you like to go first?

 1. Yes
 2. No
 
(Type 1 or 2)

'''

 )
    if turn=="1":
        print("Alright, you will start the game")
    elif turn=="2":
        print("Alright, the computer will go first")
    else:
        print("Incorrect entry. Please select '1' or '2'.")




#Function used in Multiplayer team selection 
def team_select_mp():
    
    player1_choice=input(
    '''
    Player 1, please select your team!
    (Player 2 will be assigned to the opposite team):

    1.  Naugths  O
    2.  Crosses  X                                                                                                                         
    
    (Type 1 or 2)
    : '''
    )
        
    if (player1_choice)=="1":
        (player1_choice)="O"
    elif (player1_choice)=="2":
        (player1_choice)="X"       
    else:
        print("You only have 2 options... 1 and 2")

    player2_choice="unknown"
    if player1_choice=="O":
        player2_choice="X"
    if player1_choice=="X":
        player2_choice="O"
    
    print("Player 1 will play as",(player1_choice),"")
    print("Player 2 will play as",(player2_choice),"")


if gamemode=="1":
    menu_tut()
elif gamemode=="2":
    menu_sp()
elif gamemode=="3":
    menu_mp()
else:
    print("You can only enter '1', '2', or '3' ")
 



