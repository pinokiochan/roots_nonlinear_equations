from formulas import f1, f2, f3, f4, f5, f6, df1, df2, df3, df4, df5, df6
from methods import bisection, secant, newton_raphson, false_position, muller
from graphmaker import plot_function_and_roots, plot_convergence
from analysis import create_comparison_table, print_detailed_analysis

def find_interval(f, start=0.1, step=0.1, max_iterations=1000):
    a, b = start, start + step
    for _ in range(max_iterations):
        try:
            if f(a) * f(b) < 0:
                return a, b
            if f(a) * f(b) == 0:  # If either a or b is a root
                return (a, b) if f(a) == 0 else (b, a)
        except ValueError:
            pass  # Skip over domain errors
        a, b = b, b + step
    
    # If no sign change is found, return an interval containing the minimum
    a, b = start, start + step
    min_val, min_point = float('inf'), a
    for _ in range(max_iterations):
        try:
            if f(b) < min_val:
                min_val, min_point = f(b), b
        except ValueError:
            pass  # Skip over domain errors
        a, b = b, b + step
    return min_point - step, min_point + step

def analyze_function(f, df, true_root, function_name):
    print(f"\nAnalyzing function: {function_name}")
    
    try:
        # Find suitable interval for bisection and false position methods
        a, b = find_interval(f)
        x0, x1, x2 = a, (a + b) / 2, b

        # Apply methods
        methods = ['Bisection', 'Secant', 'Newton-Raphson', 'False Position', 'Muller']
        roots = []
        all_iterations = []

        root_bisection, iter_bisection = bisection(f, a, b)
        roots.append(root_bisection)
        all_iterations.append(iter_bisection)

        root_secant, iter_secant = secant(f, x0, x1)
        roots.append(root_secant)
        all_iterations.append(iter_secant)

        root_newton, iter_newton = newton_raphson(f, df, x0)
        roots.append(root_newton)
        all_iterations.append(iter_newton)

        root_false_pos, iter_false_pos = false_position(f, a, b)
        roots.append(root_false_pos)
        all_iterations.append(iter_false_pos)

        root_muller, iter_muller = muller(f, x0, x1, x2)
        roots.append(root_muller)
        all_iterations.append(iter_muller)

        # Plotting
        plot_function_and_roots(f, roots, methods, (a, b))
        plot_convergence(all_iterations, methods)

        # Analysis
        iterations_counts = [len(iterations) for iterations in all_iterations]
        comparison_table = create_comparison_table(methods, roots, iterations_counts, true_root)
        print_detailed_analysis(comparison_table)

    except ValueError as e:
        print(f"Error: {e}")

def main():
    functions = [
        (f1, df1, 2.0945514815423265, "f1(x) = x^3 - 2x - 5"),
        (f2, df2, 0.7034674, "f2(x) = e^x - x^2"),
        (f3, df3, 0.7390851332151607, "f3(x) = ln(x) - cos(x)"),
        (f4, df4, 1, "f4(x) = x^4 - 6x^3 + 12x^2 - 10x + 3"),
        (f5, df5, 1.8954942670339809, "f5(x) = sin(x) - 0.5x"),
        (f6, df6, 1.5213797068045873, "f6(x) = x^3 - x - 2")
    ]

    for f, df, true_root, function_name in functions:
        analyze_function(f, df, true_root, function_name)

if __name__ == "__main__":
    main()

