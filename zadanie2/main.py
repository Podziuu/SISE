from ucimlrepo import fetch_ucirepo 
import numpy as np
from network import Network
import random
import pickle

def saveNetwork(network):
    with open("network.pkl", "wb") as f:
        pickle.dump(network, f)

def loadNetwork():
    with open("network.pkl", "rb") as f:
        return pickle.load(f)
  
iris = fetch_ucirepo(id=53) 
  
X = iris.data.features 
y = iris.data.targets 

x_array = X.to_numpy()
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

combined_data = np.concatenate((x_array, target_values), axis=1)

isNetworkCreated = False
while True:
    if isNetworkCreated:
        print("1. Uczenie sieci")
        print("2. Testowanie sieci")
        print("3. Zapisanie sieci")
        print("4. Wyjscie")
        option = int(input("Wybierz opcje: "))
    else:
        print("Co chcesz zrobic?")
        print("1. Stworzenie nowej sieci")
        print("2. Wczytanie sieci")
        print("4. Wyjscie")
        option = int(input("Wybierz opcje: "))
        
    if option == 1 and isNetworkCreated:
        learn = input("Czy chcesz losowac dane? (t/n):")
        if learn == "t":
            combined_data = np.random.permutation(combined_data)
        for epoch in range(num_epochs):
            for i in range(len(combined_data)):
                x = combined_data[i][:4]
                expected = combined_data[i][-3:]
                output = network.forward(x)
                network.backward(expected)
                network.update(learning_rate)
        print("Nauka sieci zakonczona")
    if option == 2 and isNetworkCreated:
        correct = 0
        for i in range(150):
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
        print("Accuracy: " + str(correct / 150))
    if option == 3 and isNetworkCreated:
        print("Zapisanie sieci")
        saveNetwork(network)
        print("Siec zapisana do pliku network.pkl")
    
    if option == 1 and not isNetworkCreated:
        print("Tworzenie nowej sieci")
        num_layers = int(input("Podaj liczbe warstw ukrytych: "))
        num_neurons = [4]
        for i in range(num_layers):
            num_neurons.append(int(input("Podaj liczbe neuronow w " + str(i + 1)  + " warstwie ukrytej: ")))

        num_neurons.append(3)
        isBias = int(input("Czy chcesz dodac bias?: "))

        num_epochs = int(input("Podaj liczbę epok: "))
        learning_rate = float(input("Podaj współczynnik uczenia: "))

        network = Network(num_layers + 2, num_neurons, isBias)
        
        print("Siec stworzona, co teraz chcesz robic?")
        isNetworkCreated = True
    if option == 2 and not isNetworkCreated:
        print("Wczytanie sieci")
        network = loadNetwork()
        print("Siec wczytana, co teraz chcesz robic?")
        isNetworkCreated = True
    if option == 4:
        break