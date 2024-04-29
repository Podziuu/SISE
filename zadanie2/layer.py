import numpy as np
from neuron import Neuron

class Layer:
    def __init__(self, num_neurons, num_neurons_in_prev, isBias):
        self.neurons = np.array([Neuron(num_neurons_in_prev ,isBias) for i in range(num_neurons)])
        
    def forward(self, inputs):
        self.output = np.array([neuron.forward(inputs) for neuron in self.neurons])
        return self.output

    def backwardlast(self, targets):
        for i in range(len(self.neurons)):
            self.neurons[i].backwardlast(targets[i])

    def backward(self, next_neurons):
        for i in range(len(self.neurons)):
            self.neurons[i].backward(next_neurons, i)
        
    def update(self, lr):
        for neuron in self.neurons:
            neuron.update(lr)