import pandas as pd
import numpy as np

def calculate_errors(true_value, approximations):
    abs_errors = [abs(true_value - approx) for approx in approximations]
    rel_errors = [abs_error / abs(true_value) for abs_error in abs_errors]
    return abs_errors, rel_errors

def create_comparison_table(methods, roots, iterations_counts, true_root):
    abs_errors, rel_errors = calculate_errors(true_root, roots)
    
    data = {
        'Method': methods,
        'Root': roots,
        'Iterations': iterations_counts,
        'Absolute Error': abs_errors,
        'Relative Error': rel_errors
    }
    
    df = pd.DataFrame(data)
    df = df.sort_values('Absolute Error')
    return df

def print_detailed_analysis(df):
    print(df.to_string(index=False))
    print("\nDetailed Analysis:")
    best_method = df.iloc[0]['Method']
    worst_method = df.iloc[-1]['Method']
    print(f"Best performing method: {best_method}")
    print(f"Worst performing method: {worst_method}")
    print(f"Average number of iterations: {df['Iterations'].mean():.2f}")
    print(f"Range of absolute errors: {df['Absolute Error'].min():.2e} to {df['Absolute Error'].max():.2e}")

