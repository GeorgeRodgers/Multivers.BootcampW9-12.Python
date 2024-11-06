# Import the random pakage
import random

# Because ther will be two players we will repeat the dice roll so we can creat a function
# def statement used the define a function
# This function simulates two dice rolling, their combined value is added and the fucntion returns this value
def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total

# We can also define the main function
def main():
    player1 = input("Enter player 1's name:\n")
    player2 = input("Enter player 2's name:\n")

# Dice rolls are simluated for both players
    roll1 = roll_dice()
    roll2 = roll_dice()

# The rolls are printed for both player
    print(player1, 'rolled', roll1)
    print(player2, 'rolled', roll2)

# Rules of the game are defined and a sentence is printed
    if (roll1 > roll2):
        print(player1, 'wins!')
    elif (roll1 < roll2):
        print(player2, 'wins!')
    else:
        print("It's a draw")

# The main function is run
main()