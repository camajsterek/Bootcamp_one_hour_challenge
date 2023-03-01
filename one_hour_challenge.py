# A game where the computer generates a random number
# between 1 and 10 and the user gets three chances to guess
# what that number is.

# import the random module for the computer choice

import random

# create variables for the guesses and set the game state
ComputerAnswer = 0
PlayerGuess = 0
GameState = True

# define the player input function


def PlayerInput():
    global PlayerGuess
    # try/except to validate the players input
    try:
        # takes the player input and turns it from a string into an integer
        Choice = int(input("Enter an integer between 1 and 10: "))
        if Choice < 1 or Choice > 10:
            # if the player enters a number outside the given range, the function runs again
            print("Error, invalid option.  Try again.")
            PlayerInput()
        else:
            # if the player has entered a valid number, this sets the global variable
            PlayerGuess = Choice
    # Runs the function again in the instance of value error.
    # This happens if the player enters something that can't become an integer
    except ValueError:
        print("Error, invalid option.  Try again.")
        PlayerInput()

# define the computer input function
# I made this a function so that the game can be played more than once
# in a single instance and the computers answer can change


def ComputerInput():
    global ComputerAnswer
    # sets the computers answer to a random number between 1 & 10
    ComputerAnswer = random.randint(1, 10)

# define the comparison function to compare the user input
# versus the computers answer


def Comparison(Computer):
    # variable for iterating over three gueses
    i = 0
    # print statment to show the user what the game is about
    print("Guess the number the computer is thinking of.  You have three chances!")
    # loop for the player to guess twice.  Allows for different output on third go
    while i < 2:
        # run the player input function
        PlayerInput()
        # check if their guess is lower
        if PlayerGuess < Computer:
            print(PlayerGuess, "is too low, try again.")
            # check if their guess is higher
        elif PlayerGuess > Computer:
            print(PlayerGuess, "is too high, try again.")
            # check if their guess is right
        elif PlayerGuess == Computer:
            print("Congratulations,", PlayerGuess, "is the correct number!")
            # end the game if the player wins
            break
        # increase the iteration
        i += 1
        # else statement runs for the third attempt of the user guessing
    else:
        PlayerInput()
        if PlayerGuess == Computer:
            print("Congratulations,", PlayerGuess, "is the correct number!")
        else:
            print("You lose.  The number was", Computer)

# a function to see if the player wants to play another game or not


def Cont():
    # invoke global gamestate to allow changing it
    global GameState
    # create variable to allow for validation tests, ask user their input
    state = input("Do you want to play again? (y/n) ")
    try:
        state = state.lower()  # change to lower case to ensure comparison
        if state == "y":
            GameState = True  # if yes, play again with game state true
        elif state == "n":
            GameState = False  # if no, exit the while loop below
        else:  # sanity check
            print("Error, invalid choice.  Try again.")
            Cont()  # reruns this function
    except UnboundLocalError:  # incase the user enters something other than a string
        print("Error, invalid choice.  Try again.")
        Cont()  # reruns this function


# while loop to play the actual game
while GameState == True:
    # generate the computer's number
    ComputerInput()
    # compare the computer's number to the user's number which is generated in function
    Comparison(ComputerAnswer)
    # ask if the user wants to play again
    Cont()
    # process for exiting the loop
    if GameState == False:
        print("Game over.")

# require input to exit the script.  This stops some python interperators from closing entirely before the user has finished looking at the output
input("press enter to exit")
