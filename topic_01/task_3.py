a = int(input("Enter the first coefficient of the quadratic equation \n"))
b = int(input("Enter the second coefficient of the quadratic equation \n"))
c = int(input("Enter the third coefficient of the quadratic equation \n"))

def D(a, b, c):
    discriminant = b**2 - 4*a*c
    return discriminant

print(f"The discriminant of the quadratic equation is {D(a, b, c)}")
