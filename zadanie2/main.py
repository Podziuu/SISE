from ucimlrepo import fetch_ucirepo 
import numpy as np
from neuron import Neuron
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets 

input = np.array([1, 2, 3, 4])
weights = np.array([0.5, -0.3, 0, 0.11])
neuron = Neuron(weights, 0)

print(neuron.forward(input))


