# To test our knowledge of python we will now build a word guess game
# Import the random package

import random

words = ("apple", "brave", "cloud", "drink", "flame", "grape", "haste", "jolly", "knack", "lunar") # words stored as tuple because they will not be edited

comp = random.choice(words) # computer choose a random word from the list

print('The computer has chosen a word from the following list:\n')
for word in words:
    print(word)

print('\nYou have three chances to guess the word')



lives = 3
while lives > 0:
    print('\nYou have', lives, 'left')
    user = input('What do you think the word is?\n')

    if comp == user:
        print("That's correct!")
        break
    elif lives == 1:
        lives -= 1
        print('The word was', comp)
        print('GAME OVER')
    else:
        lives -= 1
        correctLetters = []
        for i in comp:
            for y in user:
                if i == y:
                    correctLetters.append(i)
        if correctLetters:
            print('You got the following letters correct ' + (', '.join(correctLetters)) + '\n')
        else:
            print("You didn't get any letters correct\n")


