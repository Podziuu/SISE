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
    
    def backward(self, grad, isLast = False):
        # print(grad, "GRAD")
        if(isLast):
            self.grad = grad * self.output * (1 - self.output)
        else:
            self.grad = self.weights * grad;
        print(self.grad)
        return self.grad
    
    # def backward(self, grad, last_layer = False):
    #     print(grad, "GRAD")
    #     if(last_layer):
    #         self.grad = grad * self.output * (1 - self.output)
    #     else:
    #         self.grad = self.weights * grad;
    #     return self.grad

    def update(self, weights, bias):
        self.weights = weights
        self.bias = bias