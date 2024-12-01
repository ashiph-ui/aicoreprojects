# *<u>Hangman Project</u>*

## Table of Contents
1. [Description](#description)
2. [Skills I have learnt](#skills-i-have-learnt)
3. [Python files: ](#python-files)

    - 3.1 - [milestone2.py](#milestone2py)
    - 3.2 - [milestone3.py](#milestone3py)
    - 3.3 - [milestone4.py](#milestone4py)
    - 3.4 - [milestone4.py](#milestone4py)

4. [Installation Instructions]()
5. [Usage Instructions](#usage-instructions)


### 1. Description
The aim of this project is to create an interactive Hangman game. The final product uses 'Object oriented programming' (OOP) to simulate an interactive hangman game experience.

This version of the game will makes the user the 'guesser'. It is up to the user to guess the hidden word!

### 2. Skills I have Learnt:
- List comprehensions
- If-statements, for-loops and while loops
- Modularising code into functions
- Object Oriented Programming (OOP)

## 3. Python files:

### 3.1 <u>milestone2.py</u> 
A very basic program that randomly selects a word from a list of words. This list contains 5 fruit names.

Also, the program will ask an input of a single alphabetical letter as a guess. The program checks whether the guess is valid or not.

### 3.2 <u>milestone3.py</u>
Extension to milestone2.

This file shows progression by addition of a new feature that checks whether the guess letter is in the word or not.

In this file the functions are made to modularise the code for better readability.

### 3.3 <u>milestone4.py</u>
This milestone converts functions into methods with classes. A new class is made called 'Hangman', once initialised , all game methods are executed from the Hangman class.

This milestone additionally tracks player guesses and punishes incorrect guesses.

### 3.4 <u>milestone5.py</u>
The final product. This is the finished product of the hangman game.

This extends the class from milestone 4 by encoding extra logic within methods. Additionally, a function is defined outside of the class which uses the class methods to play the game seamlessly.

## 4. Installation instructions
No external packages were installed. This project was made using miniconda base environment and python 3.12.

## 5. Usage instructions
Type and enter "python3 milestone5.py" in terminal when in the directory.