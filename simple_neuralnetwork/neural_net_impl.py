#------ Imports -----#
import numpy as np
import matplotlib.pyplot as plt

class NeuralNet:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize the neural network with random weights and biases
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights for the input layer and the hidden layer with biases
        self.w1 = np.random.randn(self.input_size, self.hidden_size)
        self.b1 = np.zeros((1, self.hidden_size))  # Bias for the hidden layer
        # Weights for the output layer
        self.w2 = np.random.randn(self.hidden_size, self.output_size)
        self.b2 = np.zeros((1, self.output_size))  # Bias for the output layer

    def forward(self, inputs):
        # Perform the forward pass through the network
        self.z1 = np.dot(inputs, self.w1) + self.b1
        self.a1 = self.sigmoid(self.z1)

        self.z2 = np.dot(self.a1, self.w2) + self.b2
        self.output = self.sigmoid(self.z2)
        return self.output

    def backpropagation(self, inputs, target, learning_rate):
        # Perform backpropagation to update weights and biases
        output = self.forward(inputs)
        error_out = output - target

        # Update weights and biases for the output layer
        delta_out = error_out * self.sigmoid_der(output)
        derivative_w2 = np.dot(self.a1.T, delta_out)
        derivative_b2 = np.sum(delta_out, axis=0, keepdims=True)
        self.w2 -= derivative_w2 * learning_rate
        self.b2 -= derivative_b2 * learning_rate

        # Update weights and biases for the hidden layer
        error_hidden = np.dot(delta_out, self.w2.T)
        delta_hidden = error_hidden * self.sigmoid_der(self.a1)
        derivative_w1 = np.dot(inputs.T, delta_hidden)
        derivative_b1 = np.sum(delta_hidden, axis=0, keepdims=True)
        self.w1 -= derivative_w1 * learning_rate
        self.b1 -= derivative_b1 * learning_rate

        # Calculate and return Mean Squared Error
        return self.mse(output, target)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_der(self, x):
        return x * (1 - x)

    def mse(self, output, target):
        return np.mean((output - target) ** 2) / 2

def main():
    # Define input data and target output for an XOR gate
    inputs = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
    target_output = np.array([[1], [0], [0], [1]])

    # Create a neural network with 3 input nodes, 3 hidden nodes, and 1 output node
    nn = NeuralNet(3, 3, 1)

    # Print initial predictions before training
    print("Initial Predictions:")
    print(nn.forward(inputs))

    # Train the neural network using backpropagation until the error is below 0.01
    errors = []
    error_threshold = 0.01
    error = 1

    while error > error_threshold:
        error = nn.backpropagation(inputs, target_output, learning_rate=1)
        errors.append(error)

    # Print final predictions after training
    print("Final Predictions:")
    print(nn.forward(inputs))

    # Plot training errors over iterations
    x_axis = range(len(errors))
    plt.plot(x_axis, errors)
    plt.xlabel('Iterations')
    plt.ylabel('Mean Squared Error')
    plt.title('Training Error Over Iterations')
    plt.show()
