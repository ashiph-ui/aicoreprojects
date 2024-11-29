while True:
    guess = input("Guess a letter")
    if guess.isalpha and len(guess) == 1:
        print("Valid guess")
        continue
    else:
        guess = input("Invalid letter. Please, enter a single alphabetical character.")
    