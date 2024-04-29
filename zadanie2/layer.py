import numpy as np
from neuron import Neuron

class Layer:

    def __init__(self, num_neurons, num_neurons_in_prev, isBias):
        self.neurons = np.array([Neuron(num_neurons_in_prev ,isBias) for i in range(num_neurons)])
        
    def forward(self, inputs):
        self.output = np.array([neuron.forward(inputs) for neuron in self.neurons])
        return self.output

    def backward(self, grad, isLast = False):
        errors = np.array([neuron.backward(grad, isLast) for neuron in self.neurons])
        # for neuron in self.neurons:
        #     errors.append(neuron.backward(grad, isLast))
        return errors
        # for i in range(len(self.neurons)):
        #     self.neurons[i].grad = errors[i]
        # self.grads = np.array([neuron.backward(grad, isLast) for neuron in self.neurons])
        # return self.grads
        # return [neuron.backward(grad, isLast) for neuron in self.neurons]

    def backward2last(self, targets):
        for i in range(len(self.neurons)):
            self.neurons[i].backward2last(targets[i])

    def backward2(self, next_neurons):
        for i in range(len(self.neurons)):
            self.neurons[i].backward2(next_neurons, i)