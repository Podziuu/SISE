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
    
    def backward(self, grad, isLast = False):
        # print(grad, "GRAD")
        if(isLast):
            self.grad = grad * self.output * (1 - self.output)
        else:
            self.grad = self.weights * grad
        print(self.grad)
        return self.grad
    
    # def backward(self, grad, last_layer = False):
    #     print(grad, "GRAD")
    #     if(last_layer):
    #         self.grad = grad * self.output * (1 - self.output)
    #     else:
    #         self.grad = self.weights * grad;
    #     return self.grad

    def backward2last(self, target):
        factor1 = target - self.output
        factor2 = self.output * (1 - self.output)
        for i in range(len(self.weights)):
            self.grad = factor1 * factor2
            self.weights[i] += 0.1 * self.grad * self.inputs[i]

    def backward2(self, next_neurons, index):
        factor1 = 0
        for neuron in next_neurons:
            factor1 += neuron.grad * neuron.weights[index]
        factor2 = self.output * (1 - self.output)
        self.grad = factor1 * factor2
        for i in range(len(self.weights)):
            self.weights[i] += 0.1 * self.grad * self.inputs[i]

    def update(self, weights, bias):
        self.weights = weights
        self.bias = bias