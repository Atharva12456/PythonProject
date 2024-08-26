
print("Welcome to the secret auction program.")
oogs =False
oif={}
l=0
q = ""
while oogs==False:
    name1 = input("What is your name?:")
    bid = int(input("What's your bid?:"))
    oif[name1]=bid
    con = input("Are there any other bidders?:(Y/N)")
    if con.lower() == "y":
        oogs= False
        for _ in range(50):
            print()
    else:
        oogs = True
for j in oif:
    if l<oif[j]:
        l=oif[j]
        q=j
print(f"The winner is {q} with a bet of {l}.")