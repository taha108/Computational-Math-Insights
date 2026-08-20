import numpy as np
import matplotlib.pyplot as plt

# 1. The Function to minimize (A bowl shape)
def f(x): return x**2 + 5*np.sin(x)

# 2. The Derivative (Gradient) - Calculus foundations
def grad(x): return 2*x + 5*np.cos(x)

# 3. Gradient Descent Algorithm
def gradient_descent(start_x, learning_rate, epochs):
    x = start_x
    history = [x]
    
    for _ in range(epochs):
        # The core move: x_new = x_old - step * gradient
        x = x - learning_rate * grad(x)
        history.append(x)
    return np.array(history)

# 4. Execution
history = gradient_descent(start_x=8, learning_rate=0.1, epochs=20)

# 5. Visualization
x_axis = np.linspace(-10, 10, 500)
plt.figure(figsize=(10, 6), facecolor='#121212')
ax = plt.gca()
ax.set_facecolor('#121212')

plt.plot(x_axis, f(x_axis), color='white', alpha=0.5, label="Loss Surface")
plt.plot(history, f(history), 'ro-', label="AI Learning Path")

plt.title("Point 16: Gradient Descent from Scratch", color='white')
plt.legend()
plt.savefig('./AI-Foundations/gradient_descent.png', facecolor='#121212')
plt.show()