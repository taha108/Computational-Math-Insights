import numpy as np
import matplotlib.pyplot as plt

def barnsley_fern(n_points=50000):
    # Initial point
    x, y = [0], [0]

    # Matrices and translation vectors for the 4 transformations
    # Format: [[a, b], [c, d]] and [e, f] for f(x,y) = [a b; c d]*[x; y] + [e; f]
    transformations = [
        {'matrix': [[0, 0], [0, 0.16]], 'offset': [0, 0], 'p': 0.01},           # Stem
        {'matrix': [[0.85, 0.04], [-0.04, 0.85]], 'offset': [0, 1.6], 'p': 0.85}, # Leaflets
        {'matrix': [[0.2, -0.26], [0.23, 0.22]], 'offset': [0, 1.6], 'p': 0.07},  # Side leaflets (left)
        {'matrix': [[-0.15, 0.28], [0.26, 0.24]], 'offset': [0, 0.44], 'p': 0.07} # Side leaflets (right)
    ]

    for _ in range(n_points):
        # Choose a transformation based on probabilities 'p'
        r = np.random.random()
        cumulative_p = 0
        for trans in transformations:
            cumulative_p += trans['p']
            if r <= cumulative_p:
                # Apply Linear Algebra: matrix multiplication + translation
                new_pt = np.dot(trans['matrix'], [x[-1], y[-1]]) + trans['offset']
                x.append(new_pt[0])
                y.append(new_pt[1])
                break

    return x, y

# --- Visualization ---
plt.figure(figsize=(8, 10), facecolor='black')
ax = plt.gca()
ax.set_facecolor('black')

x_data, y_data = barnsley_fern()
plt.scatter(x_data, y_data, s=0.1, color='#32CD32', alpha=0.6) # Lime Green

plt.axis('off')
plt.title("Barnsley Fern: Chaos & Linear Algebra in Nature", color='white', fontsize=15)

plt.savefig('./Chaos_Theory/barnsley_fern.png', facecolor='black', bbox_inches='tight')
print("The fractal plant has grown in Chaos_Theory folder!")
plt.show()