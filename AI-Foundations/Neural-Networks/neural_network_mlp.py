import numpy as np
import matplotlib.pyplot as plt
import os

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, lr=0.1):
        # 1. Weight Initialization (Randomized to break symmetry)
        self.W1 = np.random.randn(input_size, hidden_size)
        self.W2 = np.random.randn(hidden_size, output_size)
        self.lr = lr

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def _sigmoid_derivative(self, a):
        # f'(x) = f(x) * (1 - f(x))
        return a * (1 - a)

    def forward(self, X):
        # 2. Forward Propagation
        self.z1 = np.dot(X, self.W1)
        self.a1 = self._sigmoid(self.z1) # Output of hidden layer
        self.z2 = np.dot(self.a1, self.W2)
        self.a2 = self._sigmoid(self.z2) # Final prediction
        return self.a2

    def backward(self, X, y, output):
        # 3. Backpropagation (The Chain Rule in action)
        error = y - output
        d_output = error * self._sigmoid_derivative(output)

        error_hidden = d_output.dot(self.W2.T)
        d_hidden = error_hidden * self._sigmoid_derivative(self.a1)

        # 4. Weight Updates (Gradient Descent)
        self.W2 += self.a1.T.dot(d_output) * self.lr
        self.W1 += X.T.dot(d_hidden) * self.lr

    def train(self, X, y, epochs=10000):
        history = []
        for _ in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output)
            history.append(np.mean(np.square(y - output))) # Store Mean Squared Error
        return history

# --- Test Lab: Solving the XOR Problem ---
if __name__ == "__main__":
    X = np.array([[0,0], [0,1], [1,0], [1,1]])
    y = np.array([[0], [1], [1], [0]]) # XOR logic

    nn = NeuralNetwork(2, 4, 1, lr=0.5)
    loss_history = nn.train(X, y, epochs=20000)

    print("--- 🤖 Neural Network Predictions for XOR ---")
    predictions = nn.forward(X)
    for i in range(len(X)):
        print(f"Input: {X[i]} | Prediction: {predictions[i][0]:.4f} | Target: {y[i][0]}")

    # Visualization of Learning Curve
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 5), facecolor='#121212')
    plt.plot(loss_history, color='cyan')
    plt.title("Backpropagation: Convergence of the Loss Function", fontsize=15)
    plt.xlabel("Epochs")
    plt.ylabel("Mean Squared Error (MSE)")
    
    script_dir = os.path.dirname(__file__)
    plt.savefig(os.path.join(script_dir, 'training_loss.png'), facecolor='#121212')
    plt.show()