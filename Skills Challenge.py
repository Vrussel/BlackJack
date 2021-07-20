# main.py
import random

p1hd = [random.randint(1, 11), random.randint(1, 11)]
dhd = [random.randint(1, 11), random.randint(1, 11)]
t = True
p = True
"""
give instructions

there are turns(hit, stand)[dealer and you]
if you get 21 1st(auto win)
dealer hits until 17 or above, 17 below hits
ace == 12:
   if ace:
   rng 1 or 11
"""

# welcome mat
print("Welcome to blackjack. You will be dealt 2 card to start. Your goal is to hit or stand to get up to 21.")
sg = input("Press b to begin the game: ")

if sg == "b":
    print("This is your hand")
    print(p1hd)

# infinity loop play until you want to stop or until win/lose
while t:
    while p:
        if sum(p1hd) == 21:
            print("You won, you have exactly 21")
            p = False
            t = False
            break
        hs = input("Enter h for hit and s for stand: ")

        if hs == "h":

            p1hd.append(random.randint(1, 11))
            print(p1hd)
            if sum(p1hd) == 21:
                print("you win, you got exactly 21")

                p = False
                t = False
                break
            if sum(p1hd) > 21:
                print("")
                print("you busted: you went over 21 ")
                print("you lost")
                print(p1hd)
                p = False
                t = False




        elif hs == "s":
            print("your turn is over and this was your final hand")
            print(p1hd)
            p = False


        else:
            p = False
            t = False

    if t == True:

        # dealer's hand
        while True:

            if sum(dhd) < 17:
                dhd.append(random.randint(1, 11))
                if sum(dhd) > 21:
                    print("you win, the dealer busted")
                    print(dhd)
                    t = False
                    break
                elif sum(dhd) >= 17:

                    print("Dealer has finalized their hand")
                    print(dhd)
                    break
            if sum(dhd) >= 17:
                print("The dealer has finalized their hand")
                print(dhd)
                break

        # score calculation
        d = 21 - sum(dhd)
        p = 21 - sum(p1hd)
        if d < 0:
            break

        elif d > p:
            print("You were closer to 21, you won")
            t = False
        elif d == p:
            print("It's a tie")
            t = False
        else:
            print("Dealer was closer to 21, you lose :(")
            t = False







