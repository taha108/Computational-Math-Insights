import numpy as np
import matplotlib.pyplot as plt

def visualize_eigen_geometry():
    # 1. Define a symmetric matrix A
    # This matrix stretches the space along specific directions
    A = np.array([[2, 1], 
                  [1, 2]])

    # 2. Compute eigenvalues and eigenvectors
    # 'evals' contains the scaling factors (λ)
    # 'evecs' contains the directions (v) as columns
    evals, evecs = np.linalg.eig(A)

    print(f"Matrix A:\n{A}")
    print(f"Eigenvalues: {evals}")
    print(f"Eigenvectors Matrix:\n{evecs}")

    # 3. Create a set of unit vectors (a circle) to see the transformation
    theta = np.linspace(0, 2*np.pi, 100)
    circle = np.array([np.cos(theta), np.sin(theta)])
    
    # Transform the entire circle by matrix A
    transformed_circle = A @ circle

    # 4. Plotting setup
    plt.figure(figsize=(10, 10), facecolor='#121212')
    ax = plt.gca()
    ax.set_facecolor('#121212')

    # Plot original unit circle (Input space)
    plt.plot(circle[0, :], circle[1, :], color='white', alpha=0.3, label='Original Unit Circle')

    # Plot transformed ellipse (Output space)
    plt.plot(transformed_circle[0, :], transformed_circle[1, :], color='cyan', lw=2, label='Transformed Space (Ellipse)')

    # 5. Highlight Eigenvectors (The invariant directions)
    colors = ['#FFD700', '#FF5733'] # Gold and Coral
    for i in range(len(evals)):
        # The eigenvector
        v = evecs[:, i]
        # The transformed eigenvector (λ * v)
        v_scaled = evals[i] * v
        
        # Plot the direction of the eigenvector
        plt.quiver(0, 0, v_scaled[0], v_scaled[1], angles='xy', scale_units='xy', scale=1, color=colors[i], 
                   label=f'Eigenvector {i+1} (λ={evals[i]:.1f})')

    # 6. Scientific Formatting
    limit = np.max(np.abs(transformed_circle)) + 0.5
    plt.xlim(-limit, limit)
    plt.ylim(-limit, limit)
    plt.axhline(0, color='white', alpha=0.2)
    plt.axvline(0, color='white', alpha=0.2)
    plt.legend(facecolor='#121212', labelcolor='white')
    plt.title(f"Linear Transformation & Eigen-Subspaces\n$Av = \\lambda v$", color='white', fontsize=14)
    plt.grid(alpha=0.1)

    # Save and Show
    plt.savefig('./Linear-Algebra/eigen_geometry.png', facecolor='#121212')
    print("Visualization saved as: Linear-Algebra/eigen_geometry.png")
    plt.show()

if __name__ == "__main__":
    visualize_eigen_geometry()