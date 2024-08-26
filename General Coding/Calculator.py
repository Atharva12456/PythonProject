nice=False
ooga= False
def divide(n1,n2):
    j = n1/n2
    q = j
    return j
def multiply(n1,n2):
    j = n1*n2
    q = j
    return j
def add(n1,n2):
    j = n1+n2
    q = j
    return j
def subtract(n1,n2):
    j = n1-n2
    q=j
    return j
while nice == False:
    number1=int(input("Whats the first number?:"))
    number2=int(input("What is the second number?:"))
    print("+\n-\n*\n/\n")
    ops= input("What operation would you like to use from the above?:")
    if ops == "/":
        l = divide(n1=number1, n2=number2)
        print(f"{number1}/{number2}={l}")
    if ops == "-":
        l = subtract(n1=number1, n2=number2)
        print(f"{number1}-{number2}={l}")
    if ops == "+":
        l = add(n1=number1, n2=number2)
        print(f"{number1}+{number2}={l}")
    if ops == "*":
        l = multiply(n1=number1, n2=number2)
        print(f"{number1}*{number2}={l}")
    keep = input(f"Do you want to keep calculating with {l}, start a new calculation, or stop calculating? (K/N/S):")
    if keep.lower() == "n":
        nice = False
        ooga=False
    elif keep.lower() == "k":
        nice = True
        ooga = True
    else:
        ooga = False
        nice = True
        print("Have a good day!")
while ooga == True:
    number2 = int(input("What is the second number?:"))
    print("+\n-\n*\n/\n")
    ops = input("What operation would you like to use from the above?:")
    if ops == "/":
        x = divide(n1=l, n2=number2)
        print(f"{l}/{number2}={x}")
        l=x
    if ops == "-":
        x = subtract(n1=l, n2=number2)
        print(f"{l}-{number2}={x}")
        l=x
    if ops == "+":
        x = add(n1=l, n2=number2)
        print(f"{l}+{number2}={x}")
        l=x
    if ops == "*":
        x = multiply(n1=l, n2=number2)
        print(f"{l}*{number2}={x}")
        l = x
    keep = input(f"Do you want to keep calculating with {l}, start a new calculation, or stop calculating? (K/N/S):")
    if keep.lower() == "n":
        nice = False
        ooga=False
    elif keep.lower() == "k":
        nice = True
        ooga = True
    else:
        ooga=False
        nice=True
        print("Have a good day!")
while nice == False:
    number1=int(input("Whats the first number?:"))
    number2=int(input("What is the second number?:"))
    print("+\n-\n*\n/\n")
    ops= input("What operation would you like to use from the above?:")
    if ops == "/":
        l = divide(n1=number1, n2=number2)
        print(f"{number1}/{number2}={l}")
    if ops == "-":
        l = subtract(n1=number1, n2=number2)
        print(f"{number1}-{number2}={l}")
    if ops == "+":
        l = add(n1=number1, n2=number2)
        print(f"{number1}+{number2}={l}")
    if ops == "*":
        l = multiply(n1=number1, n2=number2)
        print(f"{number1}*{number2}={l}")
    keep = input(f"Do you want to keep calculating with {l}, start a new calculation, or stop calculating? (K/N/S):")
    if keep.lower() == "n":
        nice = False
    elif keep.lower() == "k":
        nice = True
        ooga = True
    else:
        ooga = False
        nice = True
        print("Have a good day!")
while ooga == True:
    number2 = int(input("What is the second number?:"))
    print("+\n-\n*\n/\n")
    ops = input("What operation would you like to use from the above?:")
    if ops == "/":
        x = divide(n1=l, n2=number2)
        print(f"{l}/{number2}={x}")
        l=x
    if ops == "-":
        x = subtract(n1=l, n2=number2)
        print(f"{l}-{number2}={x}")
        l=x
    if ops == "+":
        x = add(n1=l, n2=number2)
        print(f"{l}+{number2}={x}")
        l=x
    if ops == "*":
        x = multiply(n1=l, n2=number2)
        print(f"{l}*{number2}={x}")
        l = x
    keep = input(f"Do you want to keep calculating with {l}, start a new calculation, or stop calculating? (K/N/S):")
    if keep.lower() == "n":
        nice = False
        ooga=False
    elif keep.lower() == "k":
        nice = True
        ooga = True
    else:
        ooga=False
        nice=True
        print("Have a good day!")
while nice == False:
    number1=int(input("Whats the first number?:"))
    number2=int(input("What is the second number?:"))
    print("+\n-\n*\n/\n")
    ops= input("What operation would you like to use from the above?:")
    if ops == "/":
        l = divide(n1=number1, n2=number2)
        print(f"{number1}/{number2}={l}")
    if ops == "-":
        l = subtract(n1=number1, n2=number2)
        print(f"{number1}-{number2}={l}")
    if ops == "+":
        l = add(n1=number1, n2=number2)
        print(f"{number1}+{number2}={l}")
    if ops == "*":
        l = multiply(n1=number1, n2=number2)
        print(f"{number1}*{number2}={l}")
    keep = input(f"Do you want to keep calculating with {l}, start a new calculation, or stop calculating? (K/N/S):")
    if keep.lower() == "n":
        nice = False
    elif keep.lower() == "k":
        nice = True
        ooga = True
    else:
        ooga = False
        nice = True
        print("Have a good day!")
while ooga == True:
    number2 = int(input("What is the second number?:"))
    print("+\n-\n*\n/\n")
    ops = input("What operation would you like to use from the above?:")
    if ops == "/":
        x = divide(n1=l, n2=number2)
        print(f"{l}/{number2}={x}")
        l=x
    if ops == "-":
        x = subtract(n1=l, n2=number2)
        print(f"{l}-{number2}={x}")
        l=x
    if ops == "+":
        x = add(n1=l, n2=number2)
        print(f"{l}+{number2}={x}")
        l=x
    if ops == "*":
        x = multiply(n1=l, n2=number2)
        print(f"{l}*{number2}={x}")
        l = x
    keep = input(f"Do you want to keep calculating with {l}, start a new calculation, or stop calculating? (K/N/S):")
    if keep.lower() == "n":
        nice = False
        ooga=False
    elif keep.lower() == "k":
        nice = True
        ooga = True
    else:
        ooga=False
        nice=True
        print("Have a good day!")
while nice == False:
    number1=int(input("Whats the first number?:"))
    number2=int(input("What is the second number?:"))
    print("+\n-\n*\n/\n")
    ops= input("What operation would you like to use from the above?:")
    if ops == "/":
        l = divide(n1=number1, n2=number2)
        print(f"{number1}/{number2}={l}")
    if ops == "-":
        l = subtract(n1=number1, n2=number2)
        print(f"{number1}-{number2}={l}")
    if ops == "+":
        l = add(n1=number1, n2=number2)
        print(f"{number1}+{number2}={l}")
    if ops == "*":
        l = multiply(n1=number1, n2=number2)
        print(f"{number1}*{number2}={l}")
    keep = input(f"Do you want to keep calculating with {l}, start a new calculation, or stop calculating? (K/N/S):")
    if keep.lower() == "n":
        nice = False
    elif keep.lower() == "k":
        nice = True
        ooga = True
    else:
        ooga = False
        nice = True
        print("Have a good day!")
while ooga == True:
    number2 = int(input("What is the second number?:"))
    print("+\n-\n*\n/\n")
    ops = input("What operation would you like to use from the above?:")
    if ops == "/":
        x = divide(n1=l, n2=number2)
        print(f"{l}/{number2}={x}")
        l=x
    if ops == "-":
        x = subtract(n1=l, n2=number2)
        print(f"{l}-{number2}={x}")
        l=x
    if ops == "+":
        x = add(n1=l, n2=number2)
        print(f"{l}+{number2}={x}")
        l=x
    if ops == "*":
        x = multiply(n1=l, n2=number2)
        print(f"{l}*{number2}={x}")
        l = x
    keep = input(f"Do you want to keep calculating with {l}, start a new calculation, or stop calculating? (K/N/S):")
    if keep.lower() == "n":
        nice = False
        ooga=False
    elif keep.lower() == "k":
        nice = True
        ooga = True
    else:
        ooga=False
        nice=True
        print("Have a good day!")
while nice == False:
    number1=int(input("Whats the first number?:"))
    number2=int(input("What is the second number?:"))
    print("+\n-\n*\n/\n")
    ops= input("What operation would you like to use from the above?:")
    if ops == "/":
        l = divide(n1=number1, n2=number2)
        print(f"{number1}/{number2}={l}")
    if ops == "-":
        l = subtract(n1=number1, n2=number2)
        print(f"{number1}-{number2}={l}")
    if ops == "+":
        l = add(n1=number1, n2=number2)
        print(f"{number1}+{number2}={l}")
    if ops == "*":
        l = multiply(n1=number1, n2=number2)
        print(f"{number1}*{number2}={l}")
    keep = input(f"Do you want to keep calculating with {l}, start a new calculation, or stop calculating? (K/N/S):")
    if keep.lower() == "n":
        nice = False
    elif keep.lower() == "k":
        nice = True
        ooga = True
    else:
        ooga = False
        nice = True
        print("Have a good day!")
while ooga == True:
    number2 = int(input("What is the second number?:"))
    print("+\n-\n*\n/\n")
    ops = input("What operation would you like to use from the above?:")
    if ops == "/":
        x = divide(n1=l, n2=number2)
        print(f"{l}/{number2}={x}")
        l=x
    if ops == "-":
        x = subtract(n1=l, n2=number2)
        print(f"{l}-{number2}={x}")
        l=x
    if ops == "+":
        x = add(n1=l, n2=number2)
        print(f"{l}+{number2}={x}")
        l=x
    if ops == "*":
        x = multiply(n1=l, n2=number2)
        print(f"{l}*{number2}={x}")
        l = x
    keep = input(f"Do you want to keep calculating with {l}, start a new calculation, or stop calculating? (K/N/S):")
    if keep.lower() == "n":
        nice = False
        ooga=False
    elif keep.lower() == "k":
        nice = True
        ooga = True
    else:
        ooga=False
        nice=True
        print("Have a good day!")
while nice == False:
    number1=int(input("Whats the first number?:"))
    number2=int(input("What is the second number?:"))
    print("+\n-\n*\n/\n")
    ops= input("What operation would you like to use from the above?:")
    if ops == "/":
        l = divide(n1=number1, n2=number2)
        print(f"{number1}/{number2}={l}")
    if ops == "-":
        l = subtract(n1=number1, n2=number2)
        print(f"{number1}-{number2}={l}")
    if ops == "+":
        l = add(n1=number1, n2=number2)
        print(f"{number1}+{number2}={l}")
    if ops == "*":
        l = multiply(n1=number1, n2=number2)
        print(f"{number1}*{number2}={l}")
    keep = input(f"Do you want to keep calculating with {l}, start a new calculation, or stop calculating? (K/N/S):")
    if keep.lower() == "n":
        nice = False
    elif keep.lower() == "k":
        nice = True
        ooga = True
    else:
        ooga = False
        nice = True
        print("Have a good day!")
while ooga == True:
    number2 = int(input("What is the second number?:"))
    print("+\n-\n*\n/\n")
    ops = input("What operation would you like to use from the above?:")
    if ops == "/":
        x = divide(n1=l, n2=number2)
        print(f"{l}/{number2}={x}")
        l=x
    if ops == "-":
        x = subtract(n1=l, n2=number2)
        print(f"{l}-{number2}={x}")
        l=x
    if ops == "+":
        x = add(n1=l, n2=number2)
        print(f"{l}+{number2}={x}")
        l=x
    if ops == "*":
        x = multiply(n1=l, n2=number2)
        print(f"{l}*{number2}={x}")
        l = x
    keep = input(f"Do you want to keep calculating with {l}, start a new calculation, or stop calculating? (K/N/S):")
    if keep.lower() == "n":
        nice = False
        ooga=False
    elif keep.lower() == "k":
        nice = True
        ooga = True
    else:
        ooga=False
        nice=True
        print("Have a good day!")
while nice == False:
    number1=int(input("Whats the first number?:"))
    number2=int(input("What is the second number?:"))
    print("+\n-\n*\n/\n")
    ops= input("What operation would you like to use from the above?:")
    if ops == "/":
        l = divide(n1=number1, n2=number2)
        print(f"{number1}/{number2}={l}")
    if ops == "-":
        l = subtract(n1=number1, n2=number2)
        print(f"{number1}-{number2}={l}")
    if ops == "+":
        l = add(n1=number1, n2=number2)
        print(f"{number1}+{number2}={l}")
    if ops == "*":
        l = multiply(n1=number1, n2=number2)
        print(f"{number1}*{number2}={l}")
    keep = input(f"Do you want to keep calculating with {l}, start a new calculation, or stop calculating? (K/N/S):")
    if keep.lower() == "n":
        nice = False
    elif keep.lower() == "k":
        nice = True
        ooga = True
    else:
        ooga = False
        nice = True
        print("Have a good day!")
while ooga == True:
    number2 = int(input("What is the second number?:"))
    print("+\n-\n*\n/\n")
    ops = input("What operation would you like to use from the above?:")
    if ops == "/":
        x = divide(n1=l, n2=number2)
        print(f"{l}/{number2}={x}")
        l=x
    if ops == "-":
        x = subtract(n1=l, n2=number2)
        print(f"{l}-{number2}={x}")
        l=x
    if ops == "+":
        x = add(n1=l, n2=number2)
        print(f"{l}+{number2}={x}")
        l=x
    if ops == "*":
        x = multiply(n1=l, n2=number2)
        print(f"{l}*{number2}={x}")
        l = x
    keep = input(f"Do you want to keep calculating with {l}, start a new calculation, or stop calculating? (K/N/S):")
    if keep.lower() == "n":
        nice = False
        ooga=False
    elif keep.lower() == "k":
        nice = True
        ooga = True
    else:
        ooga=False
        nice=True
        print("Have a good day!")
while nice == False:
    number1=int(input("Whats the first number?:"))
    number2=int(input("What is the second number?:"))
    print("+\n-\n*\n/\n")
    ops= input("What operation would you like to use from the above?:")
    if ops == "/":
        l = divide(n1=number1, n2=number2)
        print(f"{number1}/{number2}={l}")
    if ops == "-":
        l = subtract(n1=number1, n2=number2)
        print(f"{number1}-{number2}={l}")
    if ops == "+":
        l = add(n1=number1, n2=number2)
        print(f"{number1}+{number2}={l}")
    if ops == "*":
        l = multiply(n1=number1, n2=number2)
        print(f"{number1}*{number2}={l}")
    keep = input(f"Do you want to keep calculating with {l}, start a new calculation, or stop calculating? (K/N/S):")
    if keep.lower() == "n":
        nice = False
    elif keep.lower() == "k":
        nice = True
        ooga = True
    else:
        ooga = False
        nice = True
        print("Have a good day!")
while ooga == True:
    number2 = int(input("What is the second number?:"))
    print("+\n-\n*\n/\n")
    ops = input("What operation would you like to use from the above?:")
    if ops == "/":
        x = divide(n1=l, n2=number2)
        print(f"{l}/{number2}={x}")
        l=x
    if ops == "-":
        x = subtract(n1=l, n2=number2)
        print(f"{l}-{number2}={x}")
        l=x
    if ops == "+":
        x = add(n1=l, n2=number2)
        print(f"{l}+{number2}={x}")
        l=x
    if ops == "*":
        x = multiply(n1=l, n2=number2)
        print(f"{l}*{number2}={x}")
        l = x
    keep = input(f"Do you want to keep calculating with {l}, start a new calculation, or stop calculating? (K/N/S):")
    if keep.lower() == "n":
        nice = False
        ooga=False
    elif keep.lower() == "k":
        nice = True
        ooga = True
    else:
        ooga=False
        nice=True
        print("Have a good day!")
while nice == False:
    number1=int(input("Whats the first number?:"))
    number2=int(input("What is the second number?:"))
    print("+\n-\n*\n/\n")
    ops= input("What operation would you like to use from the above?:")
    if ops == "/":
        l = divide(n1=number1, n2=number2)
        print(f"{number1}/{number2}={l}")
    if ops == "-":
        l = subtract(n1=number1, n2=number2)
        print(f"{number1}-{number2}={l}")
    if ops == "+":
        l = add(n1=number1, n2=number2)
        print(f"{number1}+{number2}={l}")
    if ops == "*":
        l = multiply(n1=number1, n2=number2)
        print(f"{number1}*{number2}={l}")
    keep = input(f"Do you want to keep calculating with {l}, start a new calculation, or stop calculating? (K/N/S):")
    if keep.lower() == "n":
        nice = False
    elif keep.lower() == "k":
        nice = True
        ooga = True
    else:
        ooga = False
        nice = True
        print("Have a good day!")
while ooga == True:
    number2 = int(input("What is the second number?:"))
    print("+\n-\n*\n/\n")
    ops = input("What operation would you like to use from the above?:")
    if ops == "/":
        x = divide(n1=l, n2=number2)
        print(f"{l}/{number2}={x}")
        l=x
    if ops == "-":
        x = subtract(n1=l, n2=number2)
        print(f"{l}-{number2}={x}")
        l=x
    if ops == "+":
        x = add(n1=l, n2=number2)
        print(f"{l}+{number2}={x}")
        l=x
    if ops == "*":
        x = multiply(n1=l, n2=number2)
        print(f"{l}*{number2}={x}")
        l = x
    keep = input(f"Do you want to keep calculating with {l}, start a new calculation, or stop calculating? (K/N/S):")
    if keep.lower() == "n":
        nice = False
        ooga=False
    elif keep.lower() == "k":
        nice = True
        ooga = True
    else:
        ooga=False
        nice=True
        print("Have a good day!")
while nice == False:
    number1=int(input("Whats the first number?:"))
    number2=int(input("What is the second number?:"))
    print("+\n-\n*\n/\n")
    ops= input("What operation would you like to use from the above?:")
    if ops == "/":
        l = divide(n1=number1, n2=number2)
        print(f"{number1}/{number2}={l}")
    if ops == "-":
        l = subtract(n1=number1, n2=number2)
        print(f"{number1}-{number2}={l}")
    if ops == "+":
        l = add(n1=number1, n2=number2)
        print(f"{number1}+{number2}={l}")
    if ops == "*":
        l = multiply(n1=number1, n2=number2)
        print(f"{number1}*{number2}={l}")
    keep = input(f"Do you want to keep calculating with {l}, start a new calculation, or stop calculating? (K/N/S):")
    if keep.lower() == "n":
        nice = False
    elif keep.lower() == "k":
        nice = True
        ooga = True
    else:
        ooga = False
        nice = True
        print("Have a good day!")