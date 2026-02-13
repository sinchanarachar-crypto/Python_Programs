import random

target= random.randint(1,50)

while True:
    userchoice=input("Guess the Number or Quit(Q): ")
    if userchoice=="Q":
        break
    userchoice=int(userchoice)
    if target==userchoice:
        print("Correct! Well Done!")
        break
    elif target<userchoice:
        print("Your guess is bigger than expected.Guess again....")
    else:
        print("Your guess is smaller than expected.Guess again....")

print("-----Game Over-----")
