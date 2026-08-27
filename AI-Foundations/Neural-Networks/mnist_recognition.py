import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split

from neural_network_mlp import NeuralNetwork 

def run_mnist_vision():
    print("--- 👁️ Loading MNIST Handwritten Digits (Hand-picked subset) ---")
    
    # 1. Load data
    mnist = fetch_openml('mnist_784', version=1, as_frame=False, parser='auto')
    X, y = mnist.data / 255.0, mnist.target.astype(int)

    # 2. Subset for speed (Major's Optimization for slow PC)
    # We take 5000 images instead of 70,000
    X_train, X_test, y_train, y_test = train_test_split(X[:5000], y[:5000], test_size=0.2)

    # 3. One-hot encoding for the targets (Math: Mapping digit to vector)
    # Ex: 3 -> [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    y_train_encoded = np.eye(10)[y_train]
    y_test_encoded = np.eye(10)[y_test]

    # 4. Initialize Network (784 inputs -> 128 hidden -> 10 outputs)
    print("Training the brain... this might take a minute...")
    nn = NeuralNetwork(input_size=784, hidden_size=128, output_size=10, lr=0.1)
    
    # 5. Training
    nn.train(X_train, y_train_encoded, epochs=1000)

    # 6. Testing on one image
    test_idx = np.random.randint(0, len(X_test))
    prediction_vec = nn.forward(X_test[test_idx])
    prediction = np.argmax(prediction_vec)
    actual = y_test[test_idx]

    # 7. Visualization
    plt.style.use('dark_background')
    plt.imshow(X_test[test_idx].reshape(28, 28), cmap='gray')
    plt.title(f"AI Prediction: {prediction} | Actual: {actual}", color='cyan', fontsize=15)
    plt.axis('off')
    
    import os
    script_dir = os.path.dirname(__file__)
    plt.savefig(os.path.join(script_dir, 'mnist_prediction.png'), facecolor='#121212')
    print(f"Prediction complete! Result: {prediction}")
    plt.show()

if __name__ == "__main__":
    run_mnist_vision()