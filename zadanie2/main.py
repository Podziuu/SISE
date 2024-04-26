from ucimlrepo import fetch_ucirepo 
import numpy as np
from neuron import Neuron
from layer import Layer
from network import Network
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
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

x = network.forward(x_array[0])

print(x)

# for Layer in network.layers:
#     print(Layer.forward(x_array[0]))
    # print("warstwa")
    # for Neuron in Layer.neurons:
    #     print(Neuron.weights)
    #     print(Neuron.bias)
    