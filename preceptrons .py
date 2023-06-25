from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

class Perceptron:
    def __init__(self, learning_rate=0.0001, n_iterations=100):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features + 1)  # initialize weights and bias to zeros
        self.errors = []  # calculate the misclassification during training

        for _ in range(self.n_iterations):
            error = 0
            for i in range(n_samples):
                xi = np.insert(X[i], 0, 1)
                y_pred = self.predict(xi)
                update = self.learning_rate * (y[i] - y_pred)
                self.weights += update * xi
                error += int(update != 0.0)
            self.errors.append(error)

    def predict(self, X):
        z = np.dot(X, self.weights[1:]) + self.weights[0]  # Use weights[1:] for features, weights[0] for bias
        return np.where(z >= 0.0, 1, 0)  # Update to return 1 and 0 instead of 1 and -1

perceptron = Perceptron(learning_rate=0.1, n_iterations=100)
perceptron.fit(X_train, y_train)
y_pred = perceptron.predict(X_test)
accuracy = np.mean(y_pred == y_test)
print('Accuracy:', accuracy)
