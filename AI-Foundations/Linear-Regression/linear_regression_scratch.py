import numpy as np
import matplotlib.pyplot as plt
import os

def solve_regression():
    print("--- 📈 Linear Regression: Ordinary Least Squares (OLS) ---")

    # 1. Experimental Data (Example: Study hours vs Exam Score)
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = np.array([2, 5, 4, 6, 9, 11, 12, 15, 14, 18])

    # 2. Mathematical Solver (Closed-form formulas)
    n = len(x)
    mean_x, mean_y = np.mean(x), np.mean(y)

    # Calculate slope (a) and intercept (b)
    # a = sum((x - mean_x) * (y - mean_y)) / sum((x - mean_x)^2)
    numerator = np.sum((x - mean_x) * (y - mean_y))
    denominator = np.sum((x - mean_x)**2)
    
    a = numerator / denominator
    b = mean_y - a * mean_x

    print(f"Computed Model: y = {a:.2f}x + {b:.2f}")

    # 3. Prediction
    y_pred = a * x + b

    # 4. Visualization (Research Quality)
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 6), facecolor='#121212')
    plt.scatter(x, y, color='#FF5733', label='Experimental Data', s=100)
    plt.plot(x, y_pred, color='cyan', lw=3, label=f'Best Fit Line (OLS)')

    plt.title("Linear Regression from Scratch", fontsize=15, pad=20)
    plt.xlabel("Input Feature (x)", fontsize=12)
    plt.ylabel("Target Value (y)", fontsize=12)
    plt.legend()
    plt.grid(alpha=0.1)

    # 5. Saving to portfolio
    script_dir = os.path.dirname(__file__)
    plt.savefig(os.path.join(script_dir, 'regression_plot.png'), facecolor='#121212')
    print("Optimization Plot saved in AI-Foundations folder.")
    plt.show()

if __name__ == "__main__":
    solve_regression()