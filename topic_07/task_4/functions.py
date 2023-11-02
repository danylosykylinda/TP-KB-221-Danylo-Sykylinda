class Calculator:
    def plus(self, x, y):
        return float(x) + float(y)

    def minus(self, x, y):
        return float(x) - float(y)

    def multiply(self, x, y):
        return float(x) * float(y)

    def divide(self, x, y):
        try:
            return float(x) / float(y)
        except ZeroDivisionError:
            return "ERROR!!! You are trying to divide a number by zero, please enter it again"
