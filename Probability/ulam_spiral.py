import numpy as np
import matplotlib.pyplot as plt

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def generate_ulam(n):
    grid = np.zeros((n, n))
    # Start at the exact center
    x, y = n // 2, n // 2
    
    # Directions: Right, Up, Left, Down
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    
    current_dir = 0
    step_limit = 1
    number = 1
    
    while number <= n**2:
        # Move in the current direction twice for each step_limit size
        # (1,1 , 2,2, 3,3...)
        for _ in range(2):
            for _ in range(step_limit):
                if number <= n**2:
                    if is_prime(number):
                        grid[y, x] = 1
                    
                    # Move to next position
                    x += dx[current_dir]
                    y += dy[current_dir]
                    number += 1
            
            # Turn 90 degrees
            current_dir = (current_dir + 1) % 4
            
        step_limit += 1 # Increase steps after two turns
        
    return grid

# --- Configuration ---
size = 151 # Must be an odd number
spiral = generate_ulam(size)

# --- Visualization ---
plt.figure(figsize=(10, 10), facecolor='black')
plt.imshow(spiral, cmap='gray_r', interpolation='nearest')
plt.axis('off')
plt.title(f"The Ulam Spiral\nPrime patterns in the void", color='cyan', fontsize=15)

plt.savefig('./Probability/ulam_spiral.png', facecolor='black', bbox_inches='tight')
plt.show()