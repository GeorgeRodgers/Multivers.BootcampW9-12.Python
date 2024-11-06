import nltk
# nltk.download('words') # ths only has to be run once to get all words
import random

from nltk.corpus import words

length = int(input('How long would you like the word to be?\n'))

lives = 2 + length//2 + length%2
print('You have ', lives, ' attempts to guess the word')

# Filter out only n-letter words
nLetterWords = [word for word in words.words() if len(word) == length]

comp = random.choice(nLetterWords)

# Sets color of text
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
RESET = '\033[0m' # called to return to standard terminal text color

print(BRIGHT_RED + '[' + comp + ']' + RESET, end='')
print(BRIGHT_GREEN + '[' + comp + ']' + RESET)

if lives == 0:
    print('The word was ', )

while lives != 0:
    user = input('What is your guess?\n')
    if len(user) < length:
        print('Your guess too short')
    elif len(user) > length:
        print('Your guess too long')
    else:
        break