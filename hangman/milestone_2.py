import random

# Created a list of words to be used in the game
word_list = ['apple', 'banana', 'orange', 'pear','pineapple']

# Picks a random word from the word_list
word = random.choice(word_list)

# Guess a letter
guess = input("Guess a letter: ")

# Checking if the guess is a letter and only one letter
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
    