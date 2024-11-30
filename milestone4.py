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
        
    def test(self):
        print(self.word)
        print(self.word_guessed)
        print(self.num_letters)
        print(self.num_letters)

word_list = ["apple", "banana", "orange", "grapes","strawberry"]
test = Hangman(word_list)

test.test()

        
        