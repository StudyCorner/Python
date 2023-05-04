def factorial(n):
    if n==1:
        return 1
    else:
        return (n*factorial(n-1))



import math
pi = math.pi

def circleArea(radius):
    area = pi*radius*radius
    print("Area of Circle ",area)
