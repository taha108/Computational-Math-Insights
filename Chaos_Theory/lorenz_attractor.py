import numpy as np
import matplotlib.pyplot as plt

# 1. The Lorenz System (3 coupled ODEs)
def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

# 2. Parameters
dt = 0.01
num_steps = 10000

# 3. Initialization
xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

# Starting point (The "Initial Condition")
xs[0], ys[0], zs[0] = (0., 1., 1.05)

# 4. Numerical Integration (Euler Method)
for i in range(num_steps):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)

# 5. Visualization in 3D
fig = plt.figure(figsize=(10, 7), facecolor='black')
ax = fig.add_subplot(projection='3d')
ax.set_facecolor('black')

# Plotting the trajectory with a cyan glow
ax.plot(xs, ys, zs, lw=0.5, color='cyan')

# Removing axes for a "Secret Lab" look
ax.set_axis_off()
plt.title("Lorenz Attractor: The Mathematical Butterfly", color='white')

# Save for the portfolio
plt.savefig('lorenz_butterfly.png', facecolor='black')
plt.show()