import math
import re

def digitin(parameter):
    print("Enter {}: ".format(parameter))
    x = input()
    while not re.match(r'[+-]?\d$', x):
        print("Please enter a valid parameter!")
        x = input()
    return float(x)


print("This script solves quadratic equations, please follow instructions below")
a = digitin("a")
b = digitin("b")
c = digitin("c")
print("Your equation is y = {}x^2 + {}x + {}".format(a, b, c))
delta = b*b - 4 * a * c
if delta > 0:
    x1 = (-1 * b - math.sqrt(delta))/(2 * a)
    x2 = (-1 * b + math.sqrt(delta))/(2 * a)
    print("The roots of equation are:\nx1 = {}\nx2 = {}".format(x1, x2))
elif delta == 0:
    x = (-1 * b)/(2 * a)
    print("The roots of equation are:\nx1 = {}\nx2 = {}".format(x, -1 * x))
else:
    print("There are no roots")
