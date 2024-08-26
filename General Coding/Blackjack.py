import random
import sys
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10]
money=500
p=True
num_cards=51
while p==True:
    po=0
    lr=0
    o=0
    fgh=0
    asd=0
    Ycards=[]
    Ccards=[]
    d=456
    if money<=0:
        print("You lost all your money.")
        sys.exit()
    play = input(f"Would you like to play a game of blackjack? Current amount of money: ${money} (Y/N):")
    if play.lower() == "y":
        e=True
        bet = int(input("How much would you like to bet?"))
    elif play.lower() == "n":
        print(f"You made ${money-500}. Have a good day!")
        sys.exit()
    for q in range(1):
        hj= cards[random.randint(0,num_cards)]
        d=cards[random.randint(0,num_cards)]
        cards.remove(hj)
        cards.remove(d)
        Ccards.append(hj)
        Ccards.append("X")
        num_cards-=2
    for j in range(0,2):
        op=cards[random.randint(0,num_cards)]
        cards.remove(op)
        Ycards.append(op)
        num_cards -= 1
    for l in Ycards:
        o+=l
    print(f"Your cards: {Ycards}")
    print(f"Computer's cards: {Ccards}")
    e=True
    while e== True:
        n= input("Would you like to stay or hit? (S/H):")
        if n.lower()=="s":
            Ccards[1]=d
            for up in Ccards:
                asd+=int(up)
                po+=int(up)
            for down in Ycards:
                fgh+=int(down)
                lr+=int(down)
            if fgh > 21:
                for ooga in Ycards:
                    if ooga==11:
                        fgh-=11
                        lr-=11
            if asd > 21:
                for ooga in Ccards:
                    if ooga==11:
                        asd-=11
                        po-=11
            fgh=21-fgh
            asd=21-asd
            if po>21:
                money+=bet
                print(f"Your cards totalled to {lr} and the computer's card's totalled to {po}. YOU WIN and made ${bet}.")
                e=False
            elif fgh>=0 and fgh<asd:
                money+=bet
                print(f"Your cards totalled to {lr} and the computer's card's totalled to {po}. YOU WIN and made ${bet}.")
                e=False
            elif fgh == asd:
                print("You and the computer got the same score. YOU DRAWED and made no money")
            else:
                money-=bet
                print(f"Your cards totalled to {lr} and the computer's card's totalled to {po}. YOU LOSE and lost ${bet}.")
                e = False
        elif n.lower()=="h":
             Ycards.append(cards[random.randint(0,num_cards)])
             print(Ycards)
             num_cards -= 1
        else:
            print("That's not an action")