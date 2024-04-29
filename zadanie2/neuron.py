import numpy as np

class Neuron:
    def __init__(self, num_weights, isBias):
        self.weights = np.random.uniform(-1, 1, num_weights)
        self.grad = 0
        if isBias:
            self.bias = np.random.uniform(-1, 1)
        else:
            self.bias = 0

    def forward(self, inputs):
        self.inputs = inputs
        total = np.dot(self.weights, self.inputs) + self.bias
        self.output = 1/(1 + np.exp(-total))
        return self.output

    def backwardlast(self, target):
        factor1 = target - self.output
        factor2 = self.output * (1 - self.output)
        self.grad = factor1 * factor2

    def backward(self, next_neurons, index):
        factor1 = 0
        factor1 = np.dot([neuron.grad for neuron in next_neurons], [neuron.weights[index] for neuron in next_neurons])
        factor2 = self.output * (1 - self.output)
        self.grad = factor1 * factor2

    def update(self, lr):
        for i in range(len(self.weights)):
            self.weights[i] += lr * self.grad * self.inputs[i]
        self.bias += lr * self.grad