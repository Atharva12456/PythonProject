import random
choice=int(input("Lets play Rock, Paper, Scissors. Choose 0 for Rock, 1 for Scissors, and 2 for Paper"))
RPS = ["rock","scissors","paper"]
comp = random.randint(0,2)
comPchoice = RPS[comp]
userchoice = RPS[choice]
if userchoice == comPchoice:
    print("Both of us chose the same thing. DRAW.")
elif userchoice == "rock" and comPchoice == "scissors":
    print(f"The computer chose {comPchoice}. YOU WIN")
elif userchoice == "rock" and comPchoice == "paper":
    print(f"The computer chose {comPchoice}. YOU LOST")
elif userchoice == "paper" and comPchoice == "scissors":
    print(f"The computer chose {comPchoice}. YOU LOST")
elif userchoice == "paper" and comPchoice == "rock":
    print(f"The computer chose {comPchoice}. YOU WIN")
elif userchoice == "scissors" and comPchoice == "paper":
    print(f"The computer chose {comPchoice}. YOU WIN")
elif userchoice == "scissors" and comPchoice == "rock":
    print(f"The computer chose {comPchoice}. YOU LOST")