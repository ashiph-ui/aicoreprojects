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
    
    guess = guess.lower()
    
    if guess in word:
                print(f"Good guess! {guess} is in the word.")   
    else:
        print(f"Sorry, {guess} is not in the word. Try again")
    
    
def ask_for_input():
    """This will run the hangman game by asking for
    an input. Input a single alphabetical
    """
    guess = input("Guess a letter: ").lower()
      
    if guess.isalpha and len(guess) == 1:
        print("Valid guess")
        
        check_guess(guess)
    else:
        print("Invalid letter. Please, enter a single alphabetical character: ")
    
        
while True:
    ask_for_input()
    
    
    
    
