a = float(input("Enter the first number: \n"))
b = float(input("Enter the second number: \n"))
op = input("Choose an operation(+,-,*,/): \n")

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0.0:
        return "Cannot be divided by zero."
    return x / y

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
