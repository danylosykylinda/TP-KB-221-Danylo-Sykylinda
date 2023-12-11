import re

def RPNGenerator(expression):
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []

    if not re.match(r'^[\d()+\-*/^ ]+$', expression):
        return "You entered something wrong! Please, try enter again."
    else:
        expression = re.findall(r'\d+|[()+\-*/^]', expression)

        for char in expression:
            if char.isalnum():
                output.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while len(stack) != 0 and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            elif char in operators:
                while len(stack) != 0 and operators.get(stack[-1], 0) >= operators[char]:
                    output.append(stack.pop())
                stack.append(char)
            

        while len(stack) != 0:
            output.append(stack.pop())

        return " ".join(output)

def RPNCalculator(rpn_exp):
    stack = []
    
    if not re.match(r'^[\d()+\-*/^ ]+$', rpn_exp):
        return "You entered something wrong! Please, try enter again."
    else:
        rpn_exp = re.findall(r'\d+|[()+\-*/^]', rpn_exp)

    for char in rpn_exp:
        if char.isalnum():
            stack.append(char)
        else:
            num2 = float(stack.pop())
            num1 = float(stack.pop())
            if char == '^':
                stack.append(num1 ** num2)
            elif char == '*':
                stack.append(num1 * num2)
            elif char == '/':
                stack.append(num1 / num2)
            elif char == '+':
                stack.append(num1 + num2)
            elif char == '-':
                stack.append(num1 - num2)


    return stack[0]


if __name__ == '__main__':   
    rpn_gen = RPNGenerator(input("Enter an expression to convert a regular mathematical notation to a reverse Polish notation(RPN) (with spaces): "))
    print(rpn_gen)
    rpn_calc = RPNCalculator(input("Enter the expression to convert the reverse Polish notation(RPN) to a regular mathematical notation (with spaces): "))
    print(rpn_calc)
