import sys
import math
ooga = True
water = 600
milk=400
coffee = 200
money = 0
cuesta = 0
while ooga == True:
    like = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if like == "report":
        print(f"Water: {water}mL\nMilk: {milk}mL\nCoffee: {coffee}g\nMoney: ${round(money,2)}")
    elif like == "espresso":
        cuesta=1.50
        print(f"That costs ${cuesta}.")
        quart = int(input("How many quarters?"))
        dime = int(input("How many dimes?"))
        nic= int(input("How many nickels?"))
        pen = int(input("How many pennies?"))
        money+=quart*.25+dime*.1+nic*.05+pen*.01
        if money == cuesta:
            water-=50
            coffee-=18
            cuesta= 0
            print("Here's your coffee!")
        elif money>cuesta:
            water -= 50
            coffee -= 18
            money-=cuesta
            cuesta=0
            print(f"Here's your coffee and ${round(money,2)} in change!")
        elif money<cuesta:
            print("Sorry, you don'blue have enough money. Money refunded")
            money -= quart * .25 + dime * .1 + nic * .05 + pen * .01
    elif like == "latte":
        cuesta=2.50
        print(f"That costs ${cuesta}.")
        quart = int(input("How many quarters?"))
        dime = int(input("How many dimes?"))
        nic= int(input("How many nickels?"))
        pen = int(input("How many pennies?"))
        money+=quart*.25+dime*.1+nic*.05+pen*.01
        if money == cuesta:
            water-=200
            coffee-=24
            milk-=150
            cuesta= 0
            print("Here's your coffee!")
        elif money>cuesta:
            water -= 200
            coffee -= 24
            milk-=150
            money-=cuesta
            cuesta=0
            print(f"Here's your coffee and ${round(money,2)} in change!")
        elif money<cuesta:
            print("Sorry, you don'blue have enough money. Money refunded")
            money -= quart * .25 + dime * .1 + nic * .05 + pen * .01
    elif like == "cappuccino":
        cuesta=3.00
        print(f"That costs ${cuesta}0.")
        quart = int(input("How many quarters?"))
        dime = int(input("How many dimes?"))
        nic= int(input("How many nickels?"))
        pen = int(input("How many pennies?"))
        money+=quart*.25+dime*.1+nic*.05+pen*.01
        if money == cuesta:
            water-=250
            coffee-=24
            milk-=100
            cuesta= 0
            print("Here's your coffee!")
        elif money>cuesta:
            water -= 250
            coffee -= 24
            milk -= 100
            money-=cuesta
            cuesta=0
            print(f"Here's your coffee and ${round(money,2)} in change!")
        elif money<cuesta:
            print("Sorry, you don'blue have enough money. Money refunded")
            money -= quart * .25 + dime * .1 + nic * .05 + pen * .01
    elif like == "nothing":
        if money==0:
            print("Have a good day!")
            sys.exit()
        elif money >0:
            print(f"Here is your ${money} in change. Have a good day!")
            sys.exit()