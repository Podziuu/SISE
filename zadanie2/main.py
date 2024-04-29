from ucimlrepo import fetch_ucirepo 
import numpy as np
from neuron import Neuron
from layer import Layer
from network import Network
import random
  
iris = fetch_ucirepo(id=53) 
  
X = iris.data.features 
y = iris.data.targets 

x_array = X.to_numpy()

num_layers = int(input("Podaj liczbe warstw ukrytych: "))
num_neurons = [4]
for i in range(num_layers):
    num_neurons.append(int(input("Podaj liczbe neuronow w " + str(i + 1)  + " warstwie ukrytej: ")))

num_neurons.append(3)
isBias = int(input("Czy chcesz dodac bias?: "))

network = Network(num_layers + 2, num_neurons, isBias)

num_epochs = int(input("Podaj liczbę epok: "))
learning_rate = float(input("Podaj współczynnik uczenia: "))

true_labels = y.to_numpy()
target_values = []
for genre in true_labels:
    if genre == "Iris-setosa":
        target_values.append([1, 0, 0])
    elif genre == "Iris-versicolor":
        target_values.append([0, 1, 0])
    elif genre == "Iris-virginica":
        target_values.append([0, 0, 1])

target_values = np.array(target_values)

for epoch in range(num_epochs):
     for i in range(len(x_array)):
         x = x_array[i]
         expected = target_values[i]
         output = network.forward(x)
         network.backward(expected)

correct = 0
for i in range(100):
    index = random.randint(0, 149)
    x = x_array[index]
    output = network.forward(x)
    expected = target_values[index]
    if np.argmax(output) == np.argmax(expected):
        correct += 1
    else:
        print(index)
        print(output)
        print(expected)

print("Accuracy: " + str(correct / 100))