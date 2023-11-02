import operations
import functions

calculator = functions.Calculator()
operations = operations.Operations()

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
        operations.log(a, b, op, calculator.plus(a, b))
        print(f"Answer: {calculator.plus(a, b)}")
    elif op == '-':
        operations.log(a, b, op, calculator.minus(a, b))
        print(f"Answer: {calculator.minus(a, b)}")
    elif op == '*':
        operations.log(a, b, op, calculator.multiply(a, b))
        print(f"Answer: {calculator.multiply(a, b)}")
    elif op == '/':
        operations.log(a, b, op, calculator.divide(a, b))
        print(f"Answer: {calculator.divide(a, b)}")
