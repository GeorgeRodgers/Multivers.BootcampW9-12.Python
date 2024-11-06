# For a game of rock paper scissors we need computer and user choice
# We also want the computer to randomly select their choce so that the game works
# To do this we need to import the 'random' package from Pythons in built libary

import random

# Here we are using the 'random.choice()' method to select a radon item from the list
# There more rando, methods listed in the documentaion for this package

comp = random.choice(['rock', 'paper', 'scissors'])

user = input('Would you like rock, paper or scissors?\n')

# We woudld also like to know what the computer choose but we need to do this after the user has made ther choice

print('The computer choose ' + comp + '.')

# To compare the computer and user choices we need to use conditionl logic
# As with JavaScript the `==` operator is used for comparison
# As python is strongly typed there is no need to use a strict comparison

# Comparison opporators in python are similar to JavaScript, except 'else if' is shortened to 'elif
# Blocks are also written differently
# Because Python is a "whitespace langauge" a condition is closed with colon, ':', and the block statement are indented on the next line
# The block must be indented by at least one space and all statements in the block must have the same indentation

if comp == user:
    print('Tie')
elif user == 'rock' and comp == 'scissors':
    print('You win!')
elif user == 'paper' and comp == 'rock':
    print('You win!')
elif user == 'scissors' and comp == 'paper':
    print('You win!')
else:
    print('You lose')