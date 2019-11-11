import random
import time
choices =["heads", "tails"]
print("Welcome to the coin toss!")
while True:
    time.sleep (2)
    coin =input("Would you like to choose heads or tails? ")
    if coin == "heads":
        print(" You have chosen",coin)
    elif coin == "tails":
        print("You have chosen",coin)
    else:
        print("Invalid choice.")
        exit()
    time.sleep(2)
    print(" Prepare for the toss!")
    time.sleep(2)
    print("Tossing......")
    flip = random.choice(choices)
    if coin == flip:
        print("You won!")
    else:
        print("You lost!")
    time.sleep(3)
