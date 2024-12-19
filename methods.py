import math

def bisection(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Function values at a and b must have opposite signs")
    
    iterations = []
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        iterations.append((i+1, c, fc))
        
        if abs(fc) < tol:
            return c, iterations
        
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    
    raise ValueError("Method did not converge")

def secant(f, x0, x1, tol=1e-6, max_iter=100):
    iterations = []
    for i in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        iterations.append((i+1, x2, f(x2)))
        
        if abs(x2 - x1) < tol:
            return x2, iterations
        
        x0, x1 = x1, x2
    
    raise ValueError("Method did not converge")

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    iterations = []
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        
        if dfx == 0:
            raise ValueError("Derivative is zero. Method fails.")
        
        x1 = x0 - fx / dfx
        iterations.append((i+1, x1, f(x1)))
        
        if abs(x1 - x0) < tol:
            return x1, iterations
        
        x0 = x1
    
    raise ValueError("Method did not converge")

def false_position(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Function values at a and b must have opposite signs")
    
    iterations = []
    for i in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        fc = f(c)
        iterations.append((i+1, c, fc))
        
        if abs(fc) < tol:
            return c, iterations
        
        if fc * f(a) < 0:
            b = c
        else:
            a = c
    
    raise ValueError("Method did not converge")

def muller(f, x0, x1, x2, tol=1e-6, max_iter=100):
    iterations = []
    for i in range(max_iter):
        h1 = x1 - x0
        h2 = x2 - x1
        g1 = (f(x1) - f(x0)) / h1
        g2 = (f(x2) - f(x1)) / h2
        
        a = (g2 - g1) / (h2 + h1)
        b = a * h2 + g2
        c = f(x2)
        
        discriminant = math.sqrt(b**2 - 4*a*c)
        if abs(b - discriminant) < abs(b + discriminant):
            denominator = b + discriminant
        else:
            denominator = b - discriminant
        
        dx = -2*c / denominator
        x3 = x2 + dx
        
        iterations.append((i+1, x3, f(x3)))
        
        if abs(dx) < tol:
            return x3, iterations
        
        x0, x1, x2 = x1, x2, x3
    
    raise ValueError("Method did not converge")

