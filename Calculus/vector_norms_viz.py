import numpy as np
import matplotlib.pyplot as plt
import os

def plot_unit_balls():
    print("--- 🏔️ Topology: Visualizing Unit Balls in R^2 ---")
    
    # 1. Setup the coordinate grid
    x = np.linspace(-1.5, 1.5, 400)
    y = np.linspace(-1.5, 1.5, 400)
    X, Y = np.meshgrid(x, y)

    # 2. Define the Norms
    # L1: |x| + |y|
    L1 = np.abs(X) + np.abs(Y)
    # L2: sqrt(x^2 + y^2)
    L2 = np.sqrt(X**2 + Y**2)
    # Linf: max(|x|, |y|)
    Linf = np.maximum(np.abs(X), np.abs(Y))

    # 3. Plotting with High-Contrast Dark Theme
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 10), facecolor='#121212')
    
    # We draw the "contour" where Norm = 1
    plt.contour(X, Y, L1, levels=[1], colors='#FF5733', linewidths=3) # Orange
    plt.contour(X, Y, L2, levels=[1], colors='cyan', linewidths=3)    # Blue
    plt.contour(X, Y, Linf, levels=[1], colors='#32CD32', linewidths=3) # Green

    # 4. Aesthetics and Labels
    plt.axhline(0, color='white', alpha=0.3)
    plt.axvline(0, color='white', alpha=0.3)
    plt.grid(alpha=0.1)
    plt.axis('equal')
    
    # Custom Legend
    from matplotlib.lines import Line2D
    custom_lines = [Line2D([0], [0], color='#FF5733', lw=3),
                    Line2D([0], [0], color='cyan', lw=3),
                    Line2D([0], [0], color='#32CD32', lw=3)]
    plt.legend(custom_lines, ['L1 Norm (Manhattan)', 'L2 Norm (Euclidean)', 'Linf Norm (Chebyshev)'], 
               facecolor='#1e1e1e', edgecolor='white')

    plt.title("The Geometry of Distance: Unit Balls in R^2", fontsize=15, pad=20)

    # 5. Scientific Save
    script_dir = os.path.dirname(__file__)
    plt.savefig(os.path.join(script_dir, 'norms_visualization.png'), facecolor='#121212', bbox_inches='tight')
    print("[SUCCESS] Visualization saved in Calculus folder.")
    plt.show()

if __name__ == "__main__":
    plot_unit_balls()