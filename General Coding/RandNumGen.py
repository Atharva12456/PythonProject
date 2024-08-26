import random
import sys
nueve = False
oof=False
ooga = False
nivce = True
grah = False
print("Welcome to the Number Guessing Game!")
while nueve == False:
    print("I'm thinking of a number netween 1 and 100")
    dif= input("Would you like to play on easy or hard mode?:")
    if dif.lower()=="hard":
      ooga = True
      nueve = True
    elif dif.lower()=="easy":
        oof=True
        nueve = True
while ooga == True:
    number = random.randint(0,100)
    attempts = 5
    nivce = False
    while nivce == False:
        if attempts == 0:
            print(f"You lost all you your attempts. The corect number was {number}.")
            again = input("Would you like to play again? (Y/N):")
            if again.lower() == "y":
                oof = False
                grah = False
                nueve = False
            elif again.lower() == "n":
                print("Have a good day!")
                sys.exit()
        guess = int(input("Make a guess:"))
        if guess > number:
            print("Too high.\nGuess again.")
            attempts-=1
        elif guess< number:
            print("Too low.\nGuess again.")
            attempts-=1
        elif guess==number:
            print(f"You got it right with {attempts} attempts remaining!")
            again = input("Would you like to play again? (Y/N):")
            if again.lower() == "y":
                ooga = False
                nivce = True
                nueve = False
            elif again.lower() == "n":
                print("Have a good day!")
                sys.exit()
while oof == True:
    number = random.randint(0,100)
    attempts = 10
    nivce = True
    while nivce == True:
        if attempts == 0:
            print(f"You lost all you your attempts. The correct number was {number}.")
            again = input("Would you like to play again? (Y/N):")
            if again.lower() == "y":
                oof = False
                grah = False
                nueve = False
            elif again.lower() == "n":
                print("Have a good day!")
                sys.exit()
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        if guess > number:
            print("Too high.\nGuess again.")
            attempts-=1
        elif guess< number:
            print("Too low.\nGuess again.")
            attempts-=1
        elif guess==number:
            print(f"You got it right with {attempts} attempts remaining!")
            again = input("Would you like to play again? (Y/N):")
            if again.lower() == "y":
                oof = False
                grah = False
                nueve = False
            elif again.lower() == "n":
                print("Have a good day!")
                sys.exit()