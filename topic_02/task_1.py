from math import sqrt

a = float(input("Enter the first coefficient of the quadratic equation \n"))
b = float(input("Enter the second coefficient of the quadratic equation \n"))
c = float(input("Enter the third coefficient of the quadratic equation \n"))

def D(a, b, c):
    discriminant = b**2 - 4*a*c
    return discriminant

def roots(D):
    if D < 0:
        return "This equation has no solution."
    elif D == 0:
        x = -b/(2*a)
        return x
    elif D > 0:
        x1 = (-b + sqrt(D))/(2*a)
        x2 = (-b - sqrt(D))/(2*a)
        return f"{x1} and {x2}"
    else:
        return "Something went wrong!"

print(f"The roots of the equation: {roots(D(a, b, c))}")
