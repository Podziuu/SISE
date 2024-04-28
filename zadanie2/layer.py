import numpy as np
from neuron import Neuron

class Layer:

    def __init__(self, num_neurons, num_neurons_in_prev, isBias):
        self.neurons = np.array([Neuron(num_neurons_in_prev ,isBias) for i in range(num_neurons)])
        
    def forward(self, inputs):
        self.output = np.array([neuron.forward(inputs) for neuron in self.neurons])
        return self.output

    def backward(self, grad):
        self.grads = np.array([neuron.backward(grad) for neuron in self.neurons])
        return self.grads