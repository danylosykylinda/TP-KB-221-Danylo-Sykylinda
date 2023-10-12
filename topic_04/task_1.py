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

def find_excep():
    while True:
        try:
            a = input("Enter the first number or 'q' to quit: \n")
            if a == 'q' or a == 'Q':
                print("You have left the program")
                break
            else:
                float(a)
            b = input("Enter the second number or 'q' to quit: \n")
            if b == 'q' or b == 'Q':
                print("You have left the program")
                break
            else:
                float(b)
            op = input("Choose an operation (+, -, *, /) or 'q' to quit: \n")
            if op == 'q' or op == 'Q':
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
        except ValueError:
            print("ERROR!!! You entered something wrong, please enter it again.")
find_excep()

        
            