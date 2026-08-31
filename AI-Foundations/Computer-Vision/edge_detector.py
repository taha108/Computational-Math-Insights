import numpy as np
import matplotlib.pyplot as plt
from skimage import data, color
from scipy.signal import convolve2d
import os

def run_edge_detection():
    print("--- 👁️ Computer Vision: Sobel Edge Detection ---")

    # 1. Load a sample image 
    img = data.camera() 

    # 2. Define Sobel Kernels (3x3 Matrices)
    # These act as discrete derivative operators
    Kx = np.array([[-1, 0, 1], 
                   [-2, 0, 2], 
                   [-1, 0, 1]])
    
    Ky = np.array([[-1, -2, -1], 
                   [ 0,  0,  0], 
                   [ 1,  2,  1]])

    # 3. Apply Convolution (The "Mathematical Scan")
    print("Scanning image with Sobel kernels...")
    Gx = convolve2d(img, Kx, mode='same')
    Gy = convolve2d(img, Ky, mode='same')

    # 4. Compute Gradient Magnitude (Hypotenuse of Gx and Gy)
    # G = sqrt(Gx^2 + Gy^2)
    G = np.hypot(Gx, Gy)
    G = G / G.max() # Normalization to [0, 1]

    # 5. Visualization
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7), facecolor='#121212')
    
    ax1.imshow(img, cmap='gray')
    ax1.set_title("Original Grayscale Image", color='white')
    ax1.axis('off')

    ax2.imshow(G, cmap='magma') 
    ax2.set_title("Detected Edges (Mathematical Gradient)", color='cyan')
    ax2.axis('off')

    # 6. Saving to portfolio
    script_dir = os.path.dirname(__file__)
    plt.savefig(os.path.join(script_dir, 'edge_detection_plot.png'), facecolor='#121212')
    print("[SUCCESS] Edge map generated and saved.")
    plt.show()

if __name__ == "__main__":
    run_edge_detection()