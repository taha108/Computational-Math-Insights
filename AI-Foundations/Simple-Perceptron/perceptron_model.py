import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, learning_rate=0.1, n_iterations=100):
        self.lr = learning_rate
        self.n_iters = n_iterations
        self.weights = None
        self.bias = None

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        # 1. Initialize weights (vector) and bias (scalar)
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        # 2. Gradient Descent (The Learning Loop)
        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                # Forward pass: Linear combination + Activation
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self._sigmoid(linear_output)

                # Backward pass: Compute gradients (Calculus in action!)
                # Update weights: W = W - lr * (y_pred - y_true) * x
                update = self.lr * (y_predicted - y[idx])
                self.weights -= update * x_i
                self.bias -= update

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self._sigmoid(linear_output)
        return [1 if i > 0.5 else 0 for i in y_predicted]

# --- Testing on a Logic Gate (AND Problem) ---
if __name__ == "__main__":
    print("--- 🤖 Training a Perceptron for AND Logic Gate ---")
    
    # Data for AND gate
    X = np.array([[0,0], [0,1], [1,0], [1,1]])
    y = np.array([0, 0, 0, 1])

    model = Perceptron(learning_rate=0.1, n_iterations=1000)
    model.fit(X, y)

    # Final Test
    test_data = np.array([[1,1], [0,1]])
    predictions = model.predict(test_data)
    
    print(f"Inputs: {test_data.tolist()}")
    print(f"Predictions: {predictions}") # Should be [1, 0]