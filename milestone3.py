import random

word_list = ["apple", "banana", "orange", "grapes","strawberry"]
word = random.choice(word_list)
print(word)

while True:
    guess = input("Guess a letter: ")
    if guess.isalpha and len(guess) == 1:
        print("Valid guess")
        
    else:
        guess = input("Invalid letter. Please, enter a single alphabetical character: ")
        
    if guess in word:
            print(f"Good guess! {guess} is in the word.")   
    else:
        print(f"Sorry, {guess} is not in the word. Try again")  