import operations, functions

while True:
    a = operations.getNumber("Enter the first number or 'q' to quit: \n") 
    if a == 'Q' or a == 'q':
        operations.log(a)
        print("You have left the program")
        break
    b = operations.getNumber("Enter the second number or 'q' to quit: \n")
    if b == 'Q' or b == 'q':
        operations.log(b)
        print("You have left the program")
        break   
    op = operations.getOperations("Choose an operation (+, -, *, /) or 'q' to quit: \n")
    if op == 'Q' or op == 'q':
        operations.log(op)
        print("You have left the program")
        break
    if op == '+':
        operations.log(a, b, op, functions.plus(a, b))
        print(f"Answer: {functions.plus(a, b)}")
    elif op == '-':
        operations.log(a, b, op, functions.minus(a, b))
        print(f"Answer: {functions.minus(a, b)}")
    elif op == '*':
        operations.log(a, b, op, functions.multiply(a, b))
        print(f"Answer: {functions.multiply(a, b)}")
    elif op == '/':
        operations.log(a, b, op, functions.divide(a, b))
        print(f"Answer: {functions.divide(a, b)}")
        