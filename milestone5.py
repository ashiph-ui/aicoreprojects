# Hangman Game
import random

class Hangman():
    """Hangman Class: A class for the hangman game

    In this version, the user inputs a word list from which the program
    will randomly select a word from. The player must guess what the word
    is without losing all of their given lives.

        Handles the logic of the Hangman game with various methods:
        this includes randomly selecting a word from a word list,
        tracking guesses, the number of lives and checking guesses.

        Args:
            word_list (list): a list of words in string format
            num_lives (int, optional): The number of lives. Defaults to 5.
        """
    def __init__(self, word_list, num_lives = 5):
        # Class parameters:
        self.word_list = word_list
        self.num_lives = num_lives
        
        # Other attributes:
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        
        self.num_letters = len(set([i for i in self.word]))
        self.list_of_guesses = []
        print(f"Welcome to the Hangman game.\n\n{self.word_guessed}")
        
    def check_guess(self, guess):
        """ Checks whether the inputted guess is correct or incorrect.
        The player is punished with -1 loss of lives if the guess is incorrect.
        If the player is correct, the letter will be revealed.

        Args:
            guess (str): one letter alphabetical guess
        """
        guess = guess.lower()
    
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")   
            for index, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[index] = letter
            print(self.word_guessed)
            print("\n")
            self.num_letters -= 1
                    
        else:
            print(f"Sorry, {guess} is not in the word. Try again")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")
            
    def ask_for_input(self):
        """ A method that asks the user for their guess. This method
        will check the validity of the guess making sure all guesses are
        alphabetical, single letter that has not already been used.
        """
        
        guess = input("Guess a letter: ").lower()
      
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
            
                       
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
            
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
           

def play_game(word_list, num_lives=5):
    """ This function will use the Hangman class to 
    start the hangman game.

    Args:
        word_list (list): list of words to guess from
        num_lives (int, optional): number of lives. Defaults to 5.

    Returns:
        _type_: Return a boolean value to ensure the game stops 
                at the conclusion
    """

    game = Hangman(word_list, num_lives)

    while True:
        if getattr(game, "num_lives") == 0:
            print("You lost!")
            return False

        elif getattr( game, "num_letters") > 0:
            game.ask_for_input()

        elif num_lives != 0 and getattr( game, "num_letters") == 0:
            print("Congratulations. You won the game!")
            return False


word_list = ["apple", "banana", "orange", "grapes","strawberry"]
play_game(word_list)

        