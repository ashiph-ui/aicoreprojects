# Hangman Game
import random

class Hangman():
    def __init__(self, word_list, num_lives = 5):
        # Class parameters:
        self.word_list = word_list
        self.num_lives = num_lives
        
        # Other attributes:
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        
        self.num_letters = len(set([i for i in self.word]))
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        guess = guess.lower()
    
        if guess in self.word:
                    print(f"Good guess! {guess} is in the word.")   
        else:
            print(f"Sorry, {guess} is not in the word. Try again")
            
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()
      
            if not guess.isalpha and len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            
            elif guess in self.word_guessed:
                print("You already tried that letter!")
            
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                    
            
    def check_attributes(self):
        print(self.word)
        print(self.word_guessed)
        print(self.num_letters)
        print(self.num_letters)

word_list = ["apple", "banana", "orange", "grapes","strawberry"]
test = Hangman(word_list)

test.ask_for_input()

        
        