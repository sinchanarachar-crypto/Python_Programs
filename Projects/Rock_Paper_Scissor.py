#Rock Paper Scissor
import random

print("\tROCK-PAPER-SCISSOR GAME\n==============================\n\tYOU V/S BOT\n==============================\nLet's see who scores points fast....\nAll th Best...")

print("""###################################################""")
print("""\tIMPORTANT INSTRUCTION""")
print("""###################################################""")
print("""You have to choose one among choices provided. \nPlease enter respective option number (No need to type the whole option of your choice).""")
print("Enter options as instructed :- \n1 for ROCK\n2 for PAPER\n3 for SCISSOR")
print("Let's Begin the Game....\n(Press Enter key to proceed)")
input()

x=int(input("Enter the Challenging Score.\n(NOTE: The score should be above 2)\n" ))

RPS = ("ROCK","PAPER","SCISSOR")
OUTPUT = random.choice(RPS)

BOT = 0
YOU = 0

while BOT <= x and YOU <= x:
    print("\nEnter your choice")
    print("1.ROCK\n2.PAPER\n3.SCISSOR\n")
    ch = int(input())

    if OUTPUT == "ROCK":
        if ch == 1:
            print("You played ROCK; Bot played ROCK")
        elif ch == 2:
            print("You played PAPER; Bot played ROCK")
            YOU += 1
        elif ch==3:
            print("You played SCISSOR; Bot played ROCK")
            BOT += 1
        else:
            print("Please enter valid choice")

    if OUTPUT == "PAPER":
        if ch == 1:
            print("You played ROCK; Bot played PAPER")
            BOT += 1
        elif ch == 2:
            print("You played PAPER; Bot played PAPER")
        elif ch==3:
            print("You played SCISSOR; Bot played PAPER")
            YOU += 1
        else:
            print("Please enter valid choice")

    if OUTPUT == "SCISSOR":
        if ch == 1:
            print("You played ROCK; Bot played SCISSOR")
            YOU += 1
        elif ch == 2:
            print("You played PAPER; Bot played SCISSOR")
            BOT += 1
        elif ch==3:
            print("You played SCISSOR; Bot played SCISSOR")
        else:
            print("Please enter valid choice")

    print("\n\nYOU : ",YOU,"\nBOT : ",BOT)

print("--------------------------------")
print("\tRESULTS ARE HERE \n(Press enter to view...)")
print("--------------------------------")
if BOT == x:
    print("\n\tBOT Won!!!\n\nBetter Luck Next Time :(\n\nHave a Nice Day")
else:
    print("\n\tYOU Won!!!\n\nMaintain The Streak ;)\n\nHave a Nice Day")