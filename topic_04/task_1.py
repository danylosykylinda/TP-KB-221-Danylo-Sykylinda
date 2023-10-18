def plus(x, y):
    return float(x) + float(y)

def minus(x, y):
    return float(x) - float(y)
    

def multiply(x, y):
    return float(x) * float(y)

def divide(x, y):
    try:
        return float(x) / float(y)
    except ZeroDivisionError:
        print("ERROR!!! You are trying to divide a number by zero, please enter it again")

def getNumber(prompt):
    while True: 
        number = input(prompt)
        if number == 'Q' or number == 'q':
            return number
        else:
            try:
                return float(number)
            except ValueError:
                print("You entered something wrong! Please, try again!")


while True:
    a = getNumber("Enter the first number or 'q' to quit: \n") 
    if a == 'Q' or a == 'q':
        print("You have left the program")
        break
    b = getNumber("Enter the second number or 'q' to quit: \n")
    if b == 'Q' or b == 'q':
        print("You have left the program")
        break   
    op = input("Choose an operation (+, -, *, /) or 'q' to quit: \n")
    if op == 'Q' or op == 'q':
        print("You have left the program")
        break
    if op == '+':
        print(f"Answer: {plus(a, b)}")
    elif op == '-':
        print(f"Answer: {minus(a, b)}")
    elif op == '*':
        print(f"Answer: {multiply(a, b)}")
    elif op == '/':
        print(f"Answer: {divide(a, b)}")
    else:
        print("You entered something wrong! No operation can be done.")
    