import numpy as np
import matplotlib.pyplot as plt

# 1. Simulation Parameters for a Stochastic Process
steps = 365                # Number of time steps
n_realizations = 5         # Number of independent paths
drift = 0.05              # Deterministic linear trend
volatility = 0.2          # Standard deviation (stochastic component)

plt.figure(figsize=(12, 7), facecolor='#121212')
ax = plt.gca()
ax.set_facecolor('#121212')

# 2. Generating Paths using Cumulative Sum of Normal Distribution
for i in range(n_realizations):
    # Generating incremental steps following N(drift, volatility^2)
    increments = np.random.normal(loc=drift, scale=volatility, size=steps)
    
    # Path is the integration of these increments over time
    path = np.cumsum(increments) 
    
    plt.plot(path, lw=1.5, alpha=0.8, label=f"Path {i+1}")

# 3. Scientific Aesthetics
plt.axhline(0, color='white', linestyle='--', alpha=0.3)
plt.title("Simulation of a Random Walk with Positive Drift", color='white', fontsize=14)
plt.xlabel("Time Steps (t)", color='white')
plt.ylabel("Process Value X(t)", color='white')
plt.legend()
plt.grid(True, alpha=0.1)
plt.tick_params(colors='white')

# 4. Output
plt.savefig('./Probability/stochastic_process.png', facecolor='#121212')
plt.show()