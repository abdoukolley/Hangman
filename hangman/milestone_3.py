import random

# Created a list of words to be used in the game
word_list = ['apple', 'banana', 'orange', 'pear','pineapple']

# Picks a random word from the word_list
word = random.choice(word_list)


while True: 
    # Guess a letter
    guess = input("Guess a letter: ")
    
    # Checking if the guess is a letter and only one letter
    if len(guess) == 1 and guess.isalpha():
        # Checking if the guess is in the word
        if guess in word:
            print(f"Good guess!{guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word.Try again.")
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        

