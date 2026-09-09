import numpy as np
import matplotlib.pyplot as plt
import os

def gram_schmidt(V):
    """
    Applies the Gram-Schmidt process to columns of matrix V.
    Returns:
        Q: Orthonormal matrix (columns are orthogonal unit vectors).
        R: Upper triangular matrix such that V = Q @ R.
    """
    n_rows, n_cols = V.shape
    Q = np.zeros((n_rows, n_cols))
    R = np.zeros((n_cols, n_cols))

    for j in range(n_cols):
        v = V[:, j].astype(float)
        # Subtract projections onto previous orthogonal vectors
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], V[:, j])
            v = v - R[i, j] * Q[:, i]

        # Compute norm and normalize
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]

    return Q, R

def run_orthogonalization_demo():
    print("--- 📐 Linear Algebra: Gram-Schmidt & QR Factorization ---")

    # 1. Non-orthogonal original basis in R^2 (skewed vectors)
    v1 = np.array([3.0, 1.0])
    v2 = np.array([2.0, 2.0])
    V = np.column_stack((v1, v2))

    print(f"Original Basis Matrix V:\n{V}")

    # 2. Compute QR via Gram-Schmidt from scratch
    Q, R = gram_schmidt(V)

    print(f"\nOrthogonal Matrix Q:\n{Q}")
    print(f"\nUpper Triangular Matrix R:\n{R}")
    
    # Verify reconstruction: V == Q @ R
    reconstruction_error = np.linalg.norm(V - Q @ R)
    print(f"\nReconstruction Error ||V - QR||: {reconstruction_error:.2e}")
    
    # Verify orthogonality: Q.T @ Q == Identity
    ortho_check = np.dot(Q[:, 0], Q[:, 1])
    print(f"Dot product <q1, q2> (should be 0): {ortho_check:.2e}")

    # 3. High-Contrast Scientific Visualization
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(8, 8), facecolor='#121212')
    ax.set_facecolor('#121212')

    # Plot original basis vectors (Red / Orange)
    ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, 
              color='#FF5733', width=0.012, label='Original v1 [3, 1]')
    ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, 
              color='#FF8D1A', width=0.012, label='Original v2 [2, 2]')

    # Plot orthonormal basis vectors (Cyan / Green)
    q1 = Q[:, 0]
    q2 = Q[:, 1]
    ax.quiver(0, 0, q1[0], q1[1], angles='xy', scale_units='xy', scale=1, 
              color='cyan', width=0.015, label='Orthonormal q1 (Unit)')
    ax.quiver(0, 0, q2[0], q2[1], angles='xy', scale_units='xy', scale=1, 
              color='#32CD32', width=0.015, label='Orthonormal q2 (Unit)')

    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 4)
    ax.axhline(0, color='white', alpha=0.2, lw=0.8)
    ax.axvline(0, color='white', alpha=0.2, lw=0.8)
    ax.grid(True, alpha=0.1, linestyle='--')
    ax.set_aspect('equal', adjustable='box')
    ax.legend(facecolor='#1e1e1e', edgecolor='white', loc='upper left')
    
    # Note le 'r' devant la chaîne pour éviter le warning LaTeX
    ax.set_title(r"Gram-Schmidt Orthogonalization in $\mathbb{R}^2$", fontsize=14, color='white', pad=20)

    # 4. Save
    script_dir = os.path.dirname(__file__)
    output_path = os.path.join(script_dir, 'gram_schmidt_plot.png')
    plt.savefig(output_path, facecolor='#121212', bbox_inches='tight')
    print(f"\n[SUCCESS] Clean plot saved to: {output_path}")
    plt.show()

if __name__ == "__main__":
    run_orthogonalization_demo()