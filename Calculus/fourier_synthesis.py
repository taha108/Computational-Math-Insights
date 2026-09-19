import numpy as np
import matplotlib.pyplot as plt
import os

def fourier_square_wave(x, n_harmonics):
    """
    Computes the Fourier series approximation of a square wave with n harmonics.
    Formula: (4 / pi) * sum_{k=0}^{N-1} sin((2k+1)x) / (2k+1)
    """
    f_approx = np.zeros_like(x)
    for k in range(n_harmonics):
        n = 2 * k + 1  # Odd harmonics: 1, 3, 5, 7, ...
        f_approx += (1.0 / n) * np.sin(n * x)
    return (4.0 / np.pi) * f_approx

def run_fourier_demo():
    print("--- 🎶 Harmonic Analysis: Fourier Series Synthesis ---")

    # 1. Domain: Two periods [-2pi, 2pi]
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

    # 2. Exact Square Wave (Target Ground Truth)
    # Using sign of sin(x) to create a pure discontinuous square wave
    square_exact = np.sign(np.sin(x))

    # 3. Fourier Approximations with increasing number of harmonics
    harmonics_list = [1, 3, 7, 25]
    colors = ['#FF5733', '#FF8D1A', 'cyan', '#32CD32']

    # 4. Scientific High-Contrast Plotting
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, 7), facecolor='#121212')
    ax.set_facecolor('#121212')

    # Plot ground truth square wave
    ax.plot(x, square_exact, color='white', alpha=0.3, lw=2, label='Target Square Wave', linestyle=':')

    # Plot approximations
    for n_h, col in zip(harmonics_list, colors):
        approx = fourier_square_wave(x, n_h)
        ax.plot(x, approx, label=f'{n_h} Harmonic(s)', color=col, lw=1.8)

    # 5. Styling & Details
    ax.set_xlim(-2 * np.pi, 2 * np.pi)
    ax.set_ylim(-1.6, 1.6)
    ax.axhline(0, color='white', alpha=0.2, lw=0.8)
    ax.axvline(0, color='white', alpha=0.2, lw=0.8)
    ax.grid(True, alpha=0.1, linestyle='--')
    ax.legend(facecolor='#1e1e1e', edgecolor='white', loc='upper right')

    ax.set_title(r"Fourier Series Decomposition: Square Wave Synthesis & Gibbs Effect", 
                 fontsize=14, color='white', pad=20)
    ax.set_xlabel(r"Angle $x$ (radians)", color='white')
    ax.set_ylabel(r"$f(x)$", color='white')

    # 6. Save Plot to Calculus folder
    script_dir = os.path.dirname(__file__)
    output_path = os.path.join(script_dir, 'fourier_synthesis.png')
    plt.savefig(output_path, facecolor='#121212', bbox_inches='tight')
    print(f"\n[SUCCESS] Fourier synthesis plot saved to: {output_path}")
    plt.show()

if __name__ == "__main__":
    run_fourier_demo()