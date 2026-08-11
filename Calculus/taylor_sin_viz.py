import numpy as np
import matplotlib.pyplot as plt

# 1. Mathematical functions (Taylor-Young expansion at x=0)
# 'f' is the original sine function (the ground truth)
def f(x): return np.sin(x)

# Taylor polynomials at different orders
def dl1(x): return x
def dl3(x): return x - (x**3)/6
def dl5(x): return x - (x**3)/6 + (x**5)/120

# 2. Data generation
# Creating 400 points between -3 and 3 to visualize local convergence
x = np.linspace(-3, 3, 400)

# 3. Plot configuration
plt.figure(figsize=(10, 6))

# Plotting the original function
plt.plot(x, f(x), label="sin(x)", color="black", linewidth=2)

# Plotting approximations with dashed lines for visual distinction
plt.plot(x, dl1(x), '--', label="1st Order (Tangent)")
plt.plot(x, dl3(x), '--', label="3rd Order")
plt.plot(x, dl5(x), '--', label="5th Order")

# 4. Plot styling and formatting
plt.ylim(-2, 2) # Zooming in to focus on the area of convergence
plt.axhline(0, color='black', linewidth=0.5) # X-axis
plt.axvline(0, color='black', linewidth=0.5) # Y-axis
plt.title("Approximation of sin(x) using Taylor Series")
plt.legend()
plt.grid(True)

# 5. Output and display
# Save the plot as a PNG file for the GitHub portfolio
plt.savefig('taylor_plot.png')
print("Plot successfully saved as: taylor_plot.png")

# Display the window
plt.show()