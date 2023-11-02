import datetime

class Operations:
    def getNumber(self, prompt):
        while True:
            number = input(prompt)
            if number == 'Q' or number == 'q':
                return number
            else:
                try:
                    return float(number)
                except ValueError:
                    print("You entered something wrong! Please try again!")
                    self.log("err_num")

    def getOperations(self, prompt):
        while True:
            op = input(prompt)
            if op == 'Q' or op == 'q' or op == '+' or op == '-' or op == '*' or op == '/':
                return op
            else:
                print("Error!!! You entered something wrong! No operation can be done.")
                self.log("err_op")

    def log(self, a=None, b=None, op=None, result=None):
        time = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        if a == "err_num":
            logging = f"\n{time}  User entered letters or other characters except numbers!"
            with open('calc.log', 'a') as logs:
                logs.write(logging)

        elif a == "err_op":
            logging = f"\n{time}  User entered some characters that are different from operation characters!"
            with open('calc.log', 'a') as logs:
                logs.write(logging)

        elif a == "q" or a == "Q":
            logging = f"\n{time}  User left the program!"
            with open('calc.log', 'a') as logs:
                logs.write(logging)

        else:
            logging = f"\n{time}  User entered value of a = {a} and value of b = {b}, and operation '{op}' on them, and got the result {result}"
            with open('calc.log', 'a') as logs:
                logs.write(logging)
