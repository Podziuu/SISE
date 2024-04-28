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
        total = np.dot(self.weights, inputs) + self.bias
        self.output = 1/(1 + np.exp(-total))
        return self.output
    
    def backward(self, grad):
        self.grad = grad * self.output * (1 - self.output)
        return self.grad

    def update(self, weights, bias):
        self.weights = weights
        self.bias = bias