#Word Jumble
#Computer picks a random word and jumbles it. Player has to guess the correct answer

import random

#Sequence of words 
WORDS = ("HAPPY","BOTTLE","GEOMETRY","LAPTOP","COLLEGE","STUDENTS","LECTURER","ASSIGNMENT")

#Picking random word from WORDS
word = random.choice(WORDS)

#Creating a variable to use later to see whether guess is correct or not
correct = word

#Create jumbled version of word
jumble=""

#Setting up the Loop
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1 ):]

#Start the Game
print(
"""
          WELCOME TO WORD JUMBLE GAME!
    
    Unscramble  the Letters to make a Word...

(Press the enter key at the prompt to quit.)
"""
)
print("The Jumbled Word is: ", jumble)

#Guessing the player's guess
guess = input("\nYour Guess: ")
guess = guess.upper()
while guess != correct and guess != "":
    print("OOPSS!!, That's not Correct..")
    guess = input("Your Guess: ")

if guess == correct:
    print("That's it! You solved it!\n")

#Ending
print("Well Played Dude!!")

input("\n\nPress enter key to exit...")