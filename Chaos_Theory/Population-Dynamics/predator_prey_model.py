import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import os

# 1. Define the system of differential equations
def lotka_volterra(z, t, alpha, beta, delta, gamma):
    x, y = z
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]

def run_simulation():
    print("--- 🐺 Population Dynamics: Lotka-Volterra Model ---")

    # 2. Parameters (Biology/Economy context)
    alpha = 1.1  # Prey growth rate
    beta = 0.4   # Predation rate
    delta = 0.1  # Predator growth rate
    gamma = 0.4  # Predator death rate

    # 3. Initial conditions (10 preys, 5 predators) and time grid
    z0 = [10, 5]
    t = np.linspace(0, 100, 1000)

    # 4. Numerical Integration
    sol = odeint(lotka_volterra, z0, t, args=(alpha, beta, delta, gamma))
    prey, pred = sol[:, 0], sol[:, 1]

    # 5. Visualization (Dual-view)
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), facecolor='#121212')

    # View 1: Evolution over time
    ax1.plot(t, prey, label='Preys', color='cyan', lw=2)
    ax1.plot(t, pred, label='Predators', color='#FF5733', lw=2)
    ax1.set_title("Evolution Over Time")
    ax1.legend()
    ax1.grid(alpha=0.1)

    # View 2: Phase Portrait (The "Signature" of the system)
    ax2.plot(prey, pred, color='white', lw=1.5)
    ax2.set_title("Phase Portrait (Prey vs Predators)")
    ax2.set_xlabel("Prey Population")
    ax2.set_ylabel("Predator Population")
    ax2.grid(alpha=0.1)

    # 6. Save for GitHub
    script_dir = os.path.dirname(__file__)
    plt.savefig(os.path.join(script_dir, 'lotka_volterra_plot.png'), facecolor='#121212')
    print("[SUCCESS] Simulation complete. Population dynamics captured.")
    plt.show()

if __name__ == "__main__":
    run_simulation()