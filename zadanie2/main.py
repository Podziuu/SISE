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

# testx1 = x_array[48].copy()
# testx2 = x_array[49].copy()
# testx3 = x_array[98].copy()
# testx4 = x_array[99].copy()
# testx5 = x_array[148].copy()
# testx6 = x_array[149].copy()


num_layers = 1#int(input("Podaj liczbe warstw ukrytych: "))
num_neurons = [4]
for i in range(num_layers):
    num_neurons.append(4)  #(int(input("Podaj liczbe neuronow w " + str(i + 1)  + " warstwie ukrytej: ")))

num_neurons.append(3)
isBias = 0#int(input("Czy chcesz dodac bias?: "))

network = Network(num_layers + 2, num_neurons, isBias)

num_epochs = 100#int(input("Podaj liczbę epok: "))
learning_rate = 1#float(input("Podaj współczynnik uczenia: "))

true_labels = y.to_numpy()
target_values = []
for genre in true_labels:
    if genre == "Iris-setosa":
        target_values.append([1, 0, 0])
    elif genre == "Iris-versicolor":
        target_values.append([0, 1, 0])
    elif genre == "Iris-virginica":
        target_values.append([0, 0, 1])




for epoch in range(num_epochs):
     for i in range(len(x_array)):
         x = x_array[i]
         expected = target_values[i]
         output = network.forward(x)
         network.backward2(expected)


x = x_array[103]
expected = target_values[103]
output = network.forward(x)
print(str(output) + " " + str(expected))





# x = network.forward(x_array[0])

# # print(x)

# z = np.array([1, 0, 0])
# # print(z)

# network.backward2(z)

# for Layer in network.layers:
#     print("warstwa")
#     for Neuron in Layer.neurons:
#         print(Neuron.grad)
    