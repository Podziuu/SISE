import numpy as np

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def forward(self, inputs):
        total = np.dot(self.weights, inputs) + self.bias
        return 1/(1 + np.exp(-total))

    def update(self, weights, bias):
        self.weights = weights
        self.bias = bias