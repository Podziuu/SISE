from layer import Layer
import numpy as np

class Network:
    def __init__(self, num_layers, num_neurons_in_layers, isBias):
        self.layers = [Layer(num_neurons_in_layers[0], 4, isBias)]
        self.layers.extend([Layer(num_neurons_in_layers[i], num_neurons_in_layers[i - 1], isBias) for i in range(1, num_layers)])



    def forward(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x
    
    def backward2(self, target):
        self.layers[-1].backward2last(target)
        
        for i in reversed(range(len(self.layers) - 1)):
            self.layers[i].backward2(self.layers[i + 1].neurons)
            

    def backward(self, grad):
        for layer in reversed(self.layers):
            isLast = layer == self.layers[-1]
            print(grad, "GRAD IN LAYER")
            grad = layer.backward(grad, isLast)
        # for layer in reversed(self.layers):
        #     isLast = layer == self.layers[-1]
        #     # print(grad, "GRAD IN LATER")
        #     grad = layer.backward(grad, isLast)
        for i in reversed(range(len(self.layers))):
            layer = self.layers[i]
            errors = list()
            if i != len(self.layers) - 1:
                for j in range(len(layer.neurons)):
                    error = 0
                    for neuron in self.layers[i + 1].neurons:
                        error += neuron.weights[j] * neuron.grad
                    errors.append(error)
            else:
                for j in range(len(layer.neurons)):
                    errors.append(layer.neurons[j].output - grad[j])
            
            for j in range(len(layer.neurons)):
                layer.neurons[j].grad = errors[j] * layer.neurons[j].output * (1 - layer.neurons[j].output)
                # layer.neurons[j].update(layer.neurons[j].weights - 0.1 * layer.neurons[j].grad, layer.neurons[j].bias - 0.1 * layer.neurons[j].grad)

        # errors = np.array()

        # for i in range(len(self.layers[-1].neurons)):
        #     errors.append(self.layers[-1].neurons[i].output - expected[i])
        #     self.layers[-1].neurons[i].grad = errors[i] * self.layers[-1].neurons[i].output * (1 - self.layers[-1].neurons[i].output)

        #error = np.sum(0.5 * (expected - self.layers[-1].output) ** 2)

        # for layer in reversed(self.layers):
        #     grad = layer.backward(grad)
        # return grad

    

    def update(self, lr):
        for layer in self.layers:
            layer.update(lr)