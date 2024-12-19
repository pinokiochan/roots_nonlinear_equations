import math

def f1(x):
    return x**3 - x - 1

def f2(x):
    return x - math.cos(x)

def f3(x):
    return math.exp(-x) - x

def f4(x):
    return x**3 + x**2 + x + 7

def f5(x):
    return x**2 + 4*math.sin(x)

def f6(x):
    return math.cos(x) - x * math.exp(x)

def df1(x):
    return 3*x**2 - 1

def df2(x):
    return 1 + math.sin(x)

def df3(x):
    return -math.exp(-x) - 1

def df4(x):
    return 3*x**2 + 2*x + 1

def df5(x):
    return 2*x + 4*math.cos(x)

def df6(x):
    return -math.sin(x) - (x * math.exp(x)) - math.exp(x)
