from layer import Layer
import numpy as np
import matplotlib.pyplot as plt

class Network:
    def __init__(self, num_layers, num_neurons_in_layers, isBias):
        self.layers = [Layer(num_neurons_in_layers[0], 4, isBias)]
        self.layers.extend([Layer(num_neurons_in_layers[i], num_neurons_in_layers[i - 1], isBias) for i in range(1, num_layers)])

    def forward(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x
    
    def backward(self, target):
        self.layers[-1].backwardlast(target)
        for i in reversed(range(len(self.layers) - 1)):
            self.layers[i].backward(self.layers[i + 1].neurons)

    def update(self, lr, momentum):
        for layer in self.layers:
            layer.update(lr, momentum)
            
    def errorPlot(self):
        with open('trainError.txt', 'r') as file:
            data = file.readlines()
        epochs = []
        errors = []
        for line in data:
            epoch, error = map(float, line.strip().split())
            epochs.append(epoch)
            errors.append(error)
        plt.plot(epochs, errors, marker='', linestyle='-')
        plt.title('Error od epoki')
        plt.xlabel('Epoka')
        plt.ylabel('Error')
        plt.grid(True)
        plt.show()

    def train(self, combined_data, stopCondition, stop, shuffle, learning_rate, momentum, errorEpoch, choice):
        with open('trainError.txt', 'w') as file:
            pass
        epochsTillSave = errorEpoch + 1
        if stopCondition == 1:
            for epoch in range(stop + 1):
                error = 0
                if shuffle:
                    combined_data = np.random.permutation(combined_data)
                for i in range(len(combined_data)):
                    x = combined_data[i][:4]
                    if choice == 1:
                        expected = combined_data[i][-3:]
                    else:
                        expected = combined_data[i][-4:]
                    output = self.forward(x)
                    self.backward(expected)
                    self.update(learning_rate, momentum)
                    error += self.calculateError(expected, output)
                    
                epochsTillSave -= 1
                if epochsTillSave == 0:
                    with open('trainError.txt', 'a') as file:
                        file.write(str(epoch) + " " + str(error) + "\n")
                    epochsTillSave = errorEpoch

        elif stopCondition == 2:
            for i in range(1000):
                error = 0
                if shuffle:
                    combined_data = np.random.permutation(combined_data)
                for j in range(len(combined_data)):
                    x = combined_data[j][:4]
                    expected = combined_data[j][-4:]
                    output = self.forward(x)
                    self.backward(expected)
                    self.update(learning_rate, momentum)
                    error += self.calculateError(expected, output)

                epochsTillSave -= 1
                if epochsTillSave == 0:
                    with open('trainError.txt', 'a') as file:
                        file.write(str(i) + " " + str(error) + "\n")
                    epochsTillSave = errorEpoch

                if error < stop:
                    break

    def calculateError(self, target, output):
        error = 0
        for i in range(len(target)):
            error += (target[i] - output[i]) ** 2
        return error / 2

    def test(self, x):
        return self.forward(x)