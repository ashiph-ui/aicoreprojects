import random

word_list = ["apple", "banana", "orange", "grapes","strawberry"]
word = random.choice(word_list)
print(word)

def check_guess(guess):
    """Checks the guess to see if it contain only
    one letter and is alhpabetical.

    Args:
        guess (str): one letter of alphabet
    """
    if guess.isalpha and len(guess) == 1:
        print("Valid guess")
    else:
        guess = input("Invalid letter. Please, enter a single alphabetical character: ")
    
def ask_for_input():
    """This will run the hangman game by asking for
    an input. Inpt a single alphabetical
    """
    while True:
        guess = input("Guess a letter: ").lower()
        check_guess(guess)
        
        if guess in word:
                print(f"Good guess! {guess} is in the word.")   
        else:
            print(f"Sorry, {guess} is not in the word. Try again")
        
    
ask_for_input()