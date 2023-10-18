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
