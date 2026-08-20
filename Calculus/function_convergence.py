import numpy as np
import matplotlib.pyplot as plt
import os

def plot_convergence():
    x = np.linspace(0, 1, 200)
    plt.figure(figsize=(10, 6), facecolor='#121212')
    ax = plt.gca()
    ax.set_facecolor('#121212')

    # We plot fn(x) = x^n for different values of n
    # As n increases, the function "flattens" toward the x-axis
    n_values = [1, 2, 5, 10, 50, 100]
    colors = plt.cm.viridis(np.linspace(0, 1, len(n_values)))

    for n, color in zip(n_values, colors):
        y = x**n
        plt.plot(x, y, label=f'n = {n}', color=color, lw=2)

    # Aesthetics
    plt.title(f"Convergence of $f_n(x) = x^n$ on $[0, 1]$", color='white', fontsize=14)
    plt.xlabel("x", color='white')
    plt.ylabel("f_n(x)", color='white')
    plt.grid(alpha=0.1)
    plt.legend(facecolor='#121212', labelcolor='white')
    plt.tick_params(colors='white')

    # Save to the correct folder
    script_dir = os.path.dirname(__file__)
    plt.savefig(os.path.join(script_dir, 'convergence_plot.png'), facecolor='#121212')
    print("Plot saved in Calculus folder.")
    plt.show()

if __name__ == "__main__":
    plot_convergence()