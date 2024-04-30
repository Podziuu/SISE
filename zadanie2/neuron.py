import numpy as np

class Neuron:
    def __init__(self, num_weights, isBias):
        self.weights = np.random.uniform(-1, 1, num_weights)
        self.grad = 0
        if isBias:
            self.bias = np.random.uniform(-1, 1)
        else:
            self.bias = 0
        
        self.deltaWeights = np.zeros(num_weights)
        self.bias_momentum = 0

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

    def update(self, lr, momentum):
        for i in range(len(self.weights)):
            self.weights[i] += lr * self.grad * self.inputs[i] + momentum * self.deltaWeights[i]
        self.bias += lr * self.grad
        if momentum > 0:
            self.deltaWeights -= self.weights
            self.bias_momentum -= self.bias
        