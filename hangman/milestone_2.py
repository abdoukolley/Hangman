import random

# Created a list of words to be used in the game
word_list = ['apple', 'banana', 'orange', 'pear','pineapple']
print(word_list)

# Picks a random word from the word_list
word = random.choice(word_list)
print(word)


guess = input("Guess a letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
    