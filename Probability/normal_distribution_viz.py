import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def plot_normal():
    # 1. Setup the data: A non-standard normal distribution
    mu, sigma = 5, 2  # Mean = 5, Std Dev = 2
    x = np.linspace(-5, 15, 1000)
    y = norm.pdf(x, mu, sigma)

    # 2. Centering and Reducing (Standardization)
    z_x = (x - mu) / sigma
    z_y = norm.pdf(z_x, 0, 1) # Standard Normal N(0,1)

    # 3. Visualization
    plt.figure(figsize=(12, 6), facecolor='#121212')
    ax = plt.gca()
    ax.set_facecolor('#121212')

    plt.plot(x, y, label=f'Original: N({mu}, {sigma}²)', color='orange', lw=2)
    plt.plot(x, z_y, label='Standardized: N(0, 1)', color='cyan', lw=2, linestyle='--')

    # Aesthetics
    plt.title("Standardization: The Power of Centering & Reducing", color='white', fontsize=14)
    plt.axvline(0, color='white', alpha=0.3)
    plt.grid(alpha=0.1)
    plt.legend(facecolor='#121212', labelcolor='white')
    plt.tick_params(colors='white')

    plt.savefig('./Probability/gaussian_cloche.png', facecolor='#121212')
    print("Gaussian visualization saved in Probability folder.")
    plt.show()

if __name__ == "__main__":
    plot_normal()