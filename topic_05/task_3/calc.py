import operations, functions

while True:
    a = operations.getNumber("Enter the first number or 'q' to quit: \n") 
    if a == 'Q' or a == 'q':
        print("You have left the program")
        break
    b = operations.getNumber("Enter the second number or 'q' to quit: \n")
    if b == 'Q' or b == 'q':
        print("You have left the program")
        break   
    op = operations.getOperations("Choose an operation (+, -, *, /) or 'q' to quit: \n")
    if op == 'Q' or op == 'q':
        print("You have left the program")
        break
    if op == '+':
        print(f"Answer: {functions.plus(a, b)}")
    elif op == '-':
        print(f"Answer: {functions.minus(a, b)}")
    elif op == '*':
        print(f"Answer: {functions.multiply(a, b)}")
    elif op == '/':
        print(f"Answer: {functions.divide(a, b)}")
        