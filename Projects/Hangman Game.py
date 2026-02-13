#Hangman game
#Classic game of hangman .The computer picks up a random word and player should guess it's one letter at a time.
#If player can't guess the word in time, Stick man gets hangged

#imports
import random

#constants
Hangman=(
    """ 
    ------
    |   |
    |
    |
    |
    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |   |
    |   0
    |
    |
    |
    |
    |
    |
    ----------
    """,
    """ 
    ------
    |   |
    |   0
    | /-+-
    |
    |
    |
    |
    |
    """,
    """
     ------
    |   |
    |   0
    | /-+-\
    |
    |
    |
    |
    |
    """,
    """
     ------
    |   |
    |   0
    | /-+-\
    |   |
    |
    |
    |
    |
    """,
        """
     ------
    |   |
    |   0
    | /-+-\
    |   |
    | 
    |
    |
    |
    """,
    """
     ------
    |   |
    |   0
    | /-+-\
    |   |
    |  |
    |  |
    |
    |
    """,
        """
     ------
    |   |
    |   0
    | /-+-\
    |   |
    |  | |
    |  | |
    |
    |
    """
)

Max_Wrong=len(Hangman)-1  #maximum mistakes that is possible is 1 less than Length of Hangman

WORDS=("AMAZE","HURDLES","STRUGGLE","SUCCESS","FOOD","FRIENDS","PARENTS","CAREER","TIMELINE","HISTORY","POLITICS","LANGUAGE")
word=random.choice(WORDS) #random word generation
so_far="-"*len(word) #one dash for each letter in word to be guessed
wrong=0 #inital wrong guess,later we will increment it
used=[] #letters already guessed

#Creating Main Loop

print("WELCOME!!.This is a HANGMAN Game....\n\t\tGOOD LUCK!!")
while wrong < Max_Wrong and so_far != word:
    print(Hangman[wrong])
    print("\nYou've used the following letters:\n",used)
    print("\nSo far, the word is:\n",so_far)

#Getting Plyer's guesses
    guess=input("\n\nEnter your Guess: ")
    guess=guess.upper()

    while guess in used:
         print("You have already guessed the letter,",guess)
         guess=input("Enter your guess: ")
         guess=guess.upper()
    used.append(guess)

#Checking the guess

    if guess in word:
        print("\nYes!",guess,"is in the word!!!")

        #create a new so_far to include guess
        new=""

        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far=new
    else:
         print("\nSorry,",guess,"isn't in the word.")
         wrong+=1

#Ending the game

if wrong==Max_Wrong:
    print(Hangman[wrong])
    print("You have been HANGED!!")
else:
    print("\nYou guessed it!!")

print("The word was ", word)
input("\n\nPress 'ENTER' Key to Exit....")