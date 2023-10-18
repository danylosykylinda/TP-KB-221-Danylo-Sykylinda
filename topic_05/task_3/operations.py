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

def getOperations(prompt):
    while True: 
        op = input(prompt)
        if op == 'Q' or op == 'q' or op == '+' or op == '-' or op == '*' or op == '/':
            return op
        else:
            print("You entered something wrong! No operation can be done.")
