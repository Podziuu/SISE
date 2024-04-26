from layer import Layer
import numpy as np

class Network:
    def __init__(self, num_layers, num_neurons_in_layers, isBias):
        self.layers = [Layer(num_neurons_in_layers[0], 4, isBias)]  # Initialize with the first layer
        self.layers.extend([Layer(num_neurons_in_layers[i], num_neurons_in_layers[i - 1], isBias) for i in range(1, num_layers)])
        # self.layers = np.array(Layer(num_neurons_in_layers[0], 4, isBias))
        # np.append(self.layers, [Layer(num_neurons_in_layers[i + 1], num_neurons_in_layers[i], isBias) for i in range(num_layers)])
        # self.layers = [Layer(num_neurons_in_layers[0], 4, isBias)]
        # for i in range(num_layers):
        #     self.layers.append(Layer(num_neurons_in_layers[i + 1], num_neurons_in_layers[i], isBias))

    def forward(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x

    def backward(self, grad):
        for layer in reversed(self.layers):
            grad = layer.backward(grad)
        return grad

    def update(self, lr):
        for layer in self.layers:
            layer.update(lr)