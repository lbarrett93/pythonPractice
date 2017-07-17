import sys

player1 = raw_input("Please enter a name for Player One: ")
player2 = raw_input("Please enter a name for Player Two: ")

#Game Loop
#Loop through the game until somebody wins
choices = ['rock','paper', 'scissors']

incomplete = True
#def exitLeft():
#    sys.exit(0)
def rps():
    global incomplete
    if incomplete == False:
        sys.exit(0)
    while incomplete:
        p1choice = raw_input("Player One: Make your move: \n")
        while p1choice not in choices:
            print "Invalid move. "
            p1choice = raw_input("Enter a valid choice, please, "+player1+": \n")

        p2choice = raw_input("Player Two: Make your move: \n")
        while p2choice not in choices:
            print "Invalid move. "
            p2choice = raw_input("Enter a valid choice, please, "+player2+": \n")

    #Determine the winner!

        if p1choice == p2choice:
            print "Draw!"
            #incomplete = False
        elif p1choice == 'rock' and p2choice == 'paper':
            print "Player Two wins!"
            #incomplete = False
        elif p1choice == 'rock' and p2choice == 'scissors':
            print "Player One wins!"
            #incomplete = False
        elif p1choice == 'paper' and p2choice == 'rock':
            print "Player One Wins!"
            #incomplete = False
        elif p1choice == 'paper' and p2choice == 'scissors':
            print "Player Two Wins!"
            #incomplete = False
        elif p1choice == 'scissors' and p2choice == 'rock':
            print "Player Two Wins!"
            #incomplete = False
        elif p1choice == 'paper' and p2choice == 'rock':
            print "Player One Wins!"
            #incomplete = False
        else:
            print "The game has ended impossibly!"

#Check to see if the player wants to play again
        tryAgain = raw_input("Do you want to play again? Enter Y or N: ")
        yesorno = ["y","n","yes","Yes","no","No","Y","N"]
        while tryAgain not in yesorno:
            tryAgain = raw_input("Please enter Y or N: ")
        if tryAgain == "y" or tryAgain == "Y" or tryAgain == "Yes" or tryAgain == "yes":
            print "Resetting game....\n"
            print "Loading............Complete!\n"
            rps()
        else:
            print "\nGame Over.\n"
            incomplete = False
            #sys.exit(0)
if incomplete == True:
    rps()
else:
    sys.exit(0)
