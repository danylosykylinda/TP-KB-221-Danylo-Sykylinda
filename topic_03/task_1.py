def plus(x, y):
    return float(x) + float(y)

def minus(x, y):
    return float(x) - float(y)

def multiply(x, y):
    return float(x) * float(y)

def divide(x, y):
    if float(y) == 0.0:
        return "Cannot be divided by zero."
    return float(x) / float(y)

while True:
    a = (input("Enter the first number: \n"))
    if a == 'q' or a == 'Q':
        print("You have left the program")
        break
    b = (input("Enter the second number: \n"))
    if b == 'q' or b == 'Q':
        print("You have left the program")
        break
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
        print("You have entered something wrong.")
