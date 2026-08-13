import numpy as np
import matplotlib.pyplot as plt

# 1. Define the function to integrate: f(x) = x^2 (or any other)
def f(x):
    return x**2

# 2. Integration limits
a, b = 0, 2
x = np.linspace(-1, 3, 400)
x_int = np.linspace(a, b, 100) # Points for the shaded area

# 3. Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, f(x), 'r', linewidth=2, label="f(x) = x²")

# 4. Visualize the integral as the area under the curve
plt.fill_between(x_int, f(x_int), color='blue', alpha=0.3, label="Integral (Area)")

# 5. Aesthetics
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title(f"Visualizing the Definite Integral from {a} to {b}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True, linestyle='--')

# 6. Output
plt.savefig('./Calculus/integral_plot.png')
print("Plot saved: integral_plot.png")
plt.show()