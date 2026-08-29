import numpy as np
import matplotlib.pyplot as plt
import os

# We use your NeuralNetwork logic from Module 20/21
class Autoencoder:
    def __init__(self, input_dim, encoding_dim):
        # Encoder weights: Input -> Small layer
        self.W_enc = np.random.randn(input_dim, encoding_dim) * 0.1
        # Decoder weights: Small layer -> Output
        self.W_dec = np.random.randn(encoding_dim, input_dim) * 0.1
        self.lr = 0.01

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def train(self, X, epochs=1000):
        print(f"Distilling information into {self.W_enc.shape[1]} dimensions...")
        for epoch in range(epochs):
            # 1. Forward Pass
            latent = self._sigmoid(X @ self.W_enc)
            output = self._sigmoid(latent @ self.W_dec)
            
            # 2. Compute Error (Reconstruction Loss)
            error = X - output
            
            # 3. Backpropagation (Simplified)
            d_output = error * (output * (1 - output))
            d_latent = (d_output @ self.W_dec.T) * (latent * (1 - latent))
            
            # 4. Updates
            self.W_dec += (latent.T @ d_output) * self.lr
            self.W_enc += (X.T @ d_latent) * self.lr

        return output

# --- Execution ---
if __name__ == "__main__":
    # Create dummy data: 10 patterns of 8 bits
    # Example: identity matrix (The hardest thing to compress!)
    X = np.eye(8) 
    
    # Compress 8 bits into only 3 bits (The bottleneck)
    ae = Autoencoder(input_dim=8, encoding_dim=3)
    reconstructed = ae.train(X, epochs=5000)

    print("\n--- 🤖 Autoencoder Results (8 bits to 3 bits) ---")
    print("Original (Row 1):", X[0])
    print("Reconstructed:   ", np.round(reconstructed[0], 2))

    # Visualization
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.imshow(X, cmap='binary')
    ax1.set_title("Original Data (8D)")
    ax2.imshow(reconstructed, cmap='viridis')
    ax2.set_title("Reconstructed from 3D Bottleneck")
    
    script_dir = os.path.dirname(__file__)
    plt.savefig(os.path.join(script_dir, 'autoencoder_reconstruction.png'))
    plt.show()