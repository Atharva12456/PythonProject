print("Welcome to Treasure Island. Your mission is to find the treasure.")
LR = input("You find yourself at a crossroad going left and right. Which way would you like to go? (L/R)")
if LR.upper() == "L":
    SW = input("You find yourself at a lake, with your only options being to swim in the lake or to wait and hope something happens. What do you do? (S/W)")
    if SW.upper() == "W":
        WD = input("Three doors appear before you. They are red, yello, and blue. Which door would you like to open? (R/B/Y)")
        if WD.upper() == "Y":
            print("You open the door and find yourself in a room filled to the brim with treasure. YOU WIN!")
        elif WD.upper()== "R":
            print("As you open the door a hand reaches out and suddenly pulls you inside. You try to fight back, but its too late and your brutally ripped apart. GAME OVER.")
        else:
            print("You open the door and are suddenly pounced upon by a hungry lion who rips you apart. GAME OVER.")
    else:
        print("You dive into the ocean, and suddenly find something grab your foot. You struggle and thrash but eventually drown, alone in the vast sea. GAME OVER.")
else:
    print("You head into the jungle and get brutally attacked by a monster. GAME OVER.")