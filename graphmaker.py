import matplotlib.pyplot as plt
import numpy as np

def plot_function_and_roots(f, roots, method_names, x_range):
    plt.figure(figsize=(12, 8))
    x = np.linspace(x_range[0], x_range[1], 1000)
    y = [f(xi) for xi in x]
    plt.plot(x, y, label='f(x)')
    plt.axhline(y=0, color='k', linestyle='--')
    
    colors = ['r', 'g', 'b', 'c', 'm']
    for root, method, color in zip(roots, method_names, colors):
        plt.scatter(root, f(root), color=color, s=100, label=f'{method}: x = {root:.6f}')
    
    plt.title('Function and Roots found by Different Methods')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.savefig('function_and_roots.png')
    plt.close()

def plot_convergence(iterations_list, method_names):
    plt.figure(figsize=(12, 8))
    
    for iterations, method, color in zip(iterations_list, method_names, ['r', 'g', 'b', 'c', 'm']):
        x = [i for i, _, _ in iterations]
        y = [abs(fx) for _, _, fx in iterations]
        plt.semilogy(x, y, color=color, label=method, marker='o')
    
    plt.title('Convergence of Different Methods')
    plt.xlabel('Iteration')
    plt.ylabel('|f(x)| (log scale)')
    plt.legend()
    plt.grid(True)
    plt.savefig('convergence.png')
    plt.close()

