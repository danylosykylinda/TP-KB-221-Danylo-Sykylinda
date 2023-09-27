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

match op:
    case "+":
        print(f"Answer: {plus(a, b)}")
    case "-":
        print(f"Answer: {minus(a, b)}")
    case "*":
        print(f"Answer: {multiply(a, b)}")
    case"/":
        print(f"Answer: {divide(a, b)}")
    case _:
        print("You have entered something wrong.")
