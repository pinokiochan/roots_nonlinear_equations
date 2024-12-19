import math

def f(x):
    return x**3 - x

def bisection_method(func, a, b, tol=1e-7, max_iterations=7):
    if func(a) * func(b) >= 0:
        raise ValueError("Invalid interval")

    for i in range(1, max_iterations + 1):
        c = (a + b) / 2
        fc = func(c)
        print(f"{i:<6} {a:<10.6f} {b:<10.6f} {c:<10.6f} {fc:<10.6f}")
        if abs(fc) < tol:
            return c
        if func(a) * fc < 0:
            b = c
        else:
            a = c
    return c

a, b = -2, 0
print(f"\nApproximate root: {bisection_method(f, a, b):.7f}")
