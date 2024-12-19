import math

def f1(x):
    return x**3 - 2*x - 5

def f2(x):
    return math.exp(x) - x**2

def f3(x):
    return math.log(x) - math.cos(x)

def f4(x):
    return x**4 - 6*x**3 + 12*x**2 - 10*x + 3

def f5(x):
    return math.sin(x) - 0.5*x

def f6(x):
    return x**3 - x - 2

def df1(x):
    return 3*x**2 - 2

def df2(x):
    return math.exp(x) - 2*x

def df3(x):
    return 1/x + math.sin(x)

def df4(x):
    return 4*x**3 - 18*x**2 + 24*x - 10

def df5(x):
    return math.cos(x) - 0.5

def df6(x):
    return 3*x**2 - 1

