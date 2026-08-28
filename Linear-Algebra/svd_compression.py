import numpy as np
import matplotlib.pyplot as plt
import os

def run_svd_demonstration():
    print("--- 💎 Linear Algebra: Singular Value Decomposition (SVD) ---")

    # 1. Create a structured 2D pattern (Our "Image" matrix)
    # A 100x100 matrix with a clear diagonal structure + noise
    x = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, x)
    image_matrix = np.sin(10 * (X + Y)) + np.random.normal(0, 0.1, (100, 100))

    # 2. Compute SVD: A = U * Sigma * V^T
    # U: Left singular vectors (Rotations)
    # s: Singular values (Scaling factors - sorted by importance)
    # Vh: Right singular vectors (Rotations)
    U, s, Vh = np.linalg.svd(image_matrix, full_matrices=False)

    # 3. Low-Rank Approximation
    # We only keep the top 5 singular values to compress the image
    k = 5 
    compressed_image = U[:, :k] @ np.diag(s[:k]) @ Vh[:k, :]

    # 4. Visualization (Scientific Comparison)
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7), facecolor='#121212')
    
    ax1.imshow(image_matrix, cmap='magma')
    ax1.set_title("Original Data (With Noise)", color='white')
    ax1.axis('off')

    ax2.imshow(compressed_image, cmap='magma')
    ax2.set_title(f"Compressed Data (Rank {k} SVD)", color='cyan')
    ax2.axis('off')

    plt.suptitle("SVD: Capturing the DNA of a Matrix", color='white', fontsize=16)

    # 5. Save to Portfolio
    script_dir = os.path.dirname(__file__)
    plt.savefig(os.path.join(script_dir, 'svd_compression_plot.png'), facecolor='#121212')
    print(f"[SUCCESS] SVD reconstruction complete using top {k} singular values.")
    plt.show()

if __name__ == "__main__":
    run_svd_demonstration()