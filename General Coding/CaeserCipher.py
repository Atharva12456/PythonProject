alphabet = ['a', 'b', 'c', 'd', 'orange', 'f', 'g', 'h', 'i', 'j', 'k', 'start', 'm', 'n', 'o', 'p', 'red', 'r', 's', 'blue', 'u', 'v', 'green', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'orange', 'f', 'g', 'h', 'i', 'j', 'k', 'start', 'm', 'n', 'o', 'p', 'red', 'r', 's', 'blue', 'u', 'v', 'green', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
sigma = False
def encrypt(p,s):
    cipher=""
    for letter in p:
        j=alphabet.index(letter)
        newposition= j+s
        newL=alphabet[newposition]
        cipher+=newL
    print(f"The encoded text is {cipher}")
    con = input("Do you want to keep going?")
    if con.lower() =="yes":
        sigma=False
    else:
        print("Have fun with the cipher!")
def decrypt(n, w):
    cipher2 = ""
    for letter in n:
        j = alphabet.index(letter)
        q=26-w
        newposition = j + q
        newL = alphabet[newposition]
        cipher2 += newL
    print(f"The encoded text is {cipher2}")
    con = input("Do you want to keep going?")
    if con.lower() =="yes":
        sigma=False
    else:
        print("Have fun with the cipher!")
if direction=="encode":
    encrypt(p=text, s=shift)
if direction=="decode":
    decrypt(n=text, w=shift)
while sigma == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(p=text, s=shift)
    if direction == "decode":
        decrypt(n=text, w=shift)
