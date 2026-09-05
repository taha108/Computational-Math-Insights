import numpy as np
import matplotlib.pyplot as plt
import os

def f(x):
    return x**2 - 2  # The equation we want to solve: x^2 - 2 = 0

def df(x):
    return 2*x       # The derivative f'(x)

def run_newton_method():
    print("--- 🎯 Newton-Raphson: High-Speed Convergence ---")
    
    # 1. Initialization
    x_n = 2.0  # Initial guess (start far from the result)
    history = [x_n]
    tolerance = 1e-10
    max_iter = 10

    # 2. The Iterative Loop (The "Heart" of the algorithm)
    for i in range(max_iter):
        # Formula: x_{n+1} = x_n - f(x_n) / f'(x_n)
        x_next = x_n - f(x_n) / df(x_n)
        
        print(f"Iteration {i+1}: x = {x_next:.12f}")
        history.append(x_next)
        
        # Check if we are close enough to the root
        if abs(x_next - x_n) < tolerance:
            break
        x_n = x_next

    # 3. Scientific Visualization
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 6), facecolor='#121212')
    
    # Plot the evolution of the approximation
    plt.plot(history, 'o-', color='cyan', label='Approximation of √2')
    plt.axhline(np.sqrt(2), color='red', linestyle='--', label='Exact Value')
    
    plt.title("Newton-Raphson: Quadratic Convergence Toward √2", fontsize=14)
    plt.xlabel("Iteration Step", color='white')
    plt.ylabel("Computed Value", color='white')
    plt.legend()
    plt.grid(alpha=0.1)

    # 4. Save to Portfolio
    script_dir = os.path.dirname(__file__)
    plt.savefig(os.path.join(script_dir, 'newton_convergence.png'), facecolor='#121212')
    print(f"\n[SUCCESS] Root found: {x_n:.10f}")
    plt.show()

if __name__ == "__main__":
    run_newton_method()