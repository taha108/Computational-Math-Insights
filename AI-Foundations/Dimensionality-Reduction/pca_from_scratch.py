import numpy as np
import matplotlib.pyplot as plt
import os

def run_pca_analysis():
    print("--- 📉 Principal Component Analysis (PCA): Dimensionality Reduction ---")

    # 1. Generate correlated 2D data (a tilted cigar shape)
    np.random.seed(42)
    x = np.random.normal(0, 1, 100)
    y = 0.8 * x + np.random.normal(0, 0.5, 100)
    X = np.array([x, y]).T

    # 2. Step 1: Mean Centering (Standardization logic)
    X_centered = X - np.mean(X, axis=0)

    # 3. Step 2: Compute Covariance Matrix (Linear Algebra logic)
    # Matrix C = (X^T * X) / (n-1)
    cov_matrix = np.cov(X_centered.T)

    # 4. Step 3: Eigen-Decomposition (The Sunday "Banger" logic)
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

    # Sort eigenvectors by eigenvalues in descending order
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    # 5. Step 4: Projection onto the Principal Component
    # We take the first eigenvector (the most important direction)
    pc1 = eigenvectors[:, 0]
    X_projected = X_centered @ pc1.reshape(-1, 1) @ pc1.reshape(1, -1)

    # 6. Visualization
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 8), facecolor='#121212')
    
    plt.scatter(X_centered[:, 0], X_centered[:, 1], color='white', alpha=0.3, label='Original Data')
    plt.scatter(X_projected[:, 0], X_projected[:, 1], color='cyan', alpha=0.9, label='Projected Data (PC1)')
    
    # Draw the Eigenvector direction
    plt.quiver(0, 0, pc1[0]*2, pc1[1]*2, color='#FFD700', scale=1, 
               scale_units='xy', label='Principal Component (Vecteur Propre)')

    plt.title("PCA: Reducing 2D Data to its Main Axis", fontsize=15)
    plt.legend()
    plt.axis('equal')
    plt.grid(alpha=0.1)

    # Save to portfolio
    script_dir = os.path.dirname(__file__)
    plt.savefig(os.path.join(script_dir, 'pca_plot.png'), facecolor='#121212')
    print("PCA Visualization saved.")
    plt.show()

if __name__ == "__main__":
    run_pca_analysis()