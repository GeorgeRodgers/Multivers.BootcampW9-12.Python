import nltk # natural language tool kit installed and imported to get e dictionary of words
# nltk.download('words') # ths only has to be run once to get all words
import random # Used to select a random word

from nltk.corpus import words # imports the list of words

length = int(input('How long would you like the word to be?\n')) # difficulty mode

lives = 2 + length//2 + length%2 # lives are dynamic based on length

print('\nYou have', lives, 'attempts to guess the word') # tells you how many lives you have

# Filter out only n-letter words
nLetterWords = [word for word in words.words() if len(word) == length]

comp = random.choice(nLetterWords).upper() # Selects a random word and converts to upper case
# print(comp) # used for debugging

win = False # global win boolean variable

# Sets color of text
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m' # called to return to standard terminal text color

while win == False: # loop runs whilst win is false
    user = input('\nWhat is your guess?\n').upper()
    if len(user) != length: # if user input is wrong length prompts them to try again
        print(f'Please enter a {length}-letter word')
    elif lives == 1: 
        for i in user:
            if i in comp:
                if comp.index(i) != user.index(i):
                    print(YELLOW + '[' + i + ']' + RESET, end='')
                else:       
                    print(GREEN + '[' + i + ']' + RESET, end='')
            else:
                print(RED + '[' + i + ']' + RESET, end='')
        print('')
        print(f'\nThe word was {comp}.')
        print(RED + '\nGAME OVER\n' + RESET)
        break
    elif user == comp:
        win = True
        for i in comp:
            print(GREEN + '[' + i + ']' + RESET, end='')
        print('')
        break
    else:
        lives-=1
        for i in user:
            if i in comp:
                if comp.index(i) != user.index(i):
                    print(YELLOW + '[' + i + ']' + RESET, end='')
                else:       
                    print(GREEN + '[' + i + ']' + RESET, end='')
            else:
                print(RED + '[' + i + ']' + RESET, end='')

if win == True:
    print(GREEN + '\nYOU GUESSED CORRECT WITH', lives-1, 'ATTEMPTS LEFT!\n' + RESET)