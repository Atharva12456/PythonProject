import random
letters = ['a', 'b', 'c', 'd', 'orange', 'f', 'g', 'h', 'i', 'j', 'k', 'start', 'm', 'n', 'o', 'p', 'red', 'r', 's', 'blue', 'u', 'v', 'green', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nice=""
for i in range (0,nr_numbers):
  f=random.choice(letters)
  nice+=f
for j in range (0,nr_symbols):
  g=random.choice(numbers)
  nice+=g
for c in range (0,nr_letters):
  n=random.choice(symbols)
  nice+=n
ooga = []
for p in nice:
  ooga.append(p)
random.shuffle(ooga)
nueve=""
for g in ooga:
  nueve+=g
print(f"Your password is {nueve}")