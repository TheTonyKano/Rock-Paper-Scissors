from random import randint    
#Creates a list of playable options
options = ["Rock", "Paper", "Scissors", "Spock"]
def mainMenu():
    computer = options[randint(0,3)]
    player = False
    while player == False:
        player = input("Rock, Paper, Scissors, Spock? ")
        if player == computer:
            print("Tie!")
        elif player == options[0]:
            if computer == options [1] or computer == options[3]:
                print("You Lose!", computer, "beats", player)
                RetryMenu()
            else:
                print("You Win!", player, "beats", computer)
                RetryMenu()
        elif player == options[1]:
            if computer == options [2] or computer == options[3]:
                print("You Lose!", computer, "beats", player)
                RetryMenu()
            else:
                print("You Win!", player, "beats", computer)
                RetryMenu()
        elif player == options[2]:
            if computer == options [0] or computer == options[3]:
                print("You Lose!", computer, "beats", player)
                RetryMenu()
            else:
                print("You Win!", player, "beats", computer)
                RetryMenu()
        elif player == options[3]:
            print("You Win!", player, "beats", computer)
            RetryMenu()
        else:
            print("That's not a valid play. Check your spelling!")
            mainMenu()
        

def RetryMenu():
    RetryOptions = ["Yes", "No"]
    tryagain = input("Do you wish to play again? ")
    if tryagain == RetryOptions[0]:
        mainMenu()
    else:
        quit
#Start of Script
mainMenu()