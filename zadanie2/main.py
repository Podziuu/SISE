from ucimlrepo import fetch_ucirepo 
import numpy as np
from network import Network
import pickle
from sklearn.metrics import confusion_matrix

def saveNetwork(network):
    with open("network.pkl", "wb") as f:
        pickle.dump(network, f)

def loadNetwork():
    with open("network.pkl", "rb") as f:
        return pickle.load(f)
    
    
print("Ktore zadanie chcesz wykonac?")
print("1. Klasyfikacja irysow")
print("2. Autoenkoder")
print("3. Wyjscie")
choice = int(input("Wybierz opcje: "))

if choice == 1: 
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
    training_data = np.concatenate((combined_data[0:15], combined_data[50:65], combined_data[100:115]), axis=0)
    test_data = np.concatenate((combined_data[15:50], combined_data[65:100], combined_data[115:150]), axis=0)
    
elif choice == 2:
    x_array = np.array([[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]])
    y_array = np.array([[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]])
    combined_data = np.concatenate((x_array, y_array), axis=1)
    training_data = combined_data
    test_data = combined_data
elif choice == 3:
    exit()

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
        print("Podaj warunek stopu")
        print("1. Ilosc epok")
        print("2. Dokladnosc")
        stopCondition = int(input( "Wybierz opcje: "))
        if stopCondition == 1:
            stop = int(input("Podaj liczbe epok: "))
        elif stopCondition == 2:
            stop = float(input("Podaj dokladnosc: "))
        shuffle = int(input("Czy chcesz losowac dane? "))
        errorEpoch = int(input("Co ile epok chcesz zapisywac blad? "))
        network.train(training_data, stopCondition, stop, shuffle, learning_rate, momentum, errorEpoch, choice)
        print("Nauka sieci zakonczona")

    if option == 2 and isNetworkCreated:
        with open("trainStats.txt", "w") as file:
            pass
        correct = choice == 1 and [0, 0, 0] or [0, 0, 0, 0]
        predicted_labels = []
        true_labels = []
        for index in range(choice == 1 and 105 or 4):
            test = test_data[index]
            output = network.forward(test[:4])
            if choice == 1:
                expected = test[-3:]
            else:
                expected = test[-4:]
            true_label = np.argmax(expected)
            predicted_label = np.argmax(output)
            true_labels.append(true_label)
            predicted_labels.append(predicted_label)
            if predicted_label == true_label:
                correct[true_label] += 1

            error = network.calculateError(expected, output)
            neuronWeights = []
            neuronOutputs = []
            for i in range(len(network.layers)):
                layerWeights = []
                layerOutputs = []
                for j in range(len(network.layers[i].neurons)):
                    layerWeights.append(network.layers[i].neurons[j].weights)
                    layerOutputs.append(network.layers[i].neurons[j].output)
                neuronWeights.append(layerWeights)
                neuronOutputs.append(layerOutputs)

            
            with open("trainStats.txt", "a") as file:
            
                file.write(f"Wzorzec numer: {index}, {test[:4]}\n")
                file.write(f"Popelniony blad dla wzorca: {error}\n")
                file.write(f"Pozadany wzorzec odpowiedzi: {expected}\n")
                for i in range(len(output)):
                    file.write(f"Blad popelniony na {i} wyjsciu: {output[i] - expected[i]}\n")
                for i in range(len(output)):
                    file.write(f"Wartosc na {i} wyjsciu: {output[i]}\n")
                file.write(f"Wartosci wag neuronow wyjsciowych\n {neuronWeights[-1]}\n")
                for i in reversed(range(len(network.layers) - 1)):
                    file.write(f"Wartosci wyjsciowe neuronow ukrytych warstwy {i}: {neuronOutputs[i]}\n")
                for i in reversed(range(len(network.layers) - 1)):
                    file.write(f"Wartosci wag neuronow ukrytych warstwy {i}:\n {neuronWeights[i]}\n")
                file.write("\n\n")
                   
        file.close()

        if choice == 1:
            print("Klasyfikacja irysow")
            accuracy = sum(correct) / (len(test_data)) * 100
            print("Iris-setosa: " + str(correct[0] / 35 * 100) + "%")
            print("Iris-versicolor: " + str(correct[1] / 35 * 100) + "%")
            print("Iris-virginica: " + str(correct[2] / 35 * 100) + "%")    
            print("Total: " + str(accuracy) + "%")
        else:
            print("Autoenkoder")
            print("Popelniony blad: ", error)
            print("Odpowiedzi: ", output)
            print("Poprawne odpowiedzi: ", expected)
        matrix = confusion_matrix(true_labels, predicted_labels)
        print("\nMacierz pomyłek:")
        print(matrix)
        precision = np.diag(matrix) / np.sum(matrix, axis=0)
        recall = np.diag(matrix) / np.sum(matrix, axis=1)
        f_measure = 2 * (precision * recall) / (precision + recall)

        print("\nPrecyzja (Precision):", precision)
        print("Czułość (Recall):", recall)
        print("Miara F (F-measure):", f_measure)
        
    if option == 3 and isNetworkCreated:
        print("Zapisanie sieci")
        saveNetwork(network)
        print("Siec zapisana do pliku network.pkl")
    
    if option == 1 and not isNetworkCreated:
        print("Tworzenie nowej sieci")
        num_layers = int(input("Podaj liczbe warstw ukrytych: "))
        num_neurons = []
        for i in range(num_layers):
            num_neurons.append(int(input("Podaj liczbe neuronow w " + str(i + 1)  + " warstwie ukrytej: ")))

        num_neurons.append(choice == 1 and 3 or 4)
        isBias = int(input("Czy chcesz dodac bias?: "))

        learning_rate = float(input("Podaj współczynnik uczenia: "))
        momentum = float(input("Podaj współczynnik momentum: "))

        network = Network(num_layers + 1, num_neurons, isBias)
        
        print("Siec stworzona, co teraz chcesz robic?")
        isNetworkCreated = True
    if option == 2 and not isNetworkCreated:
        print("Wczytanie sieci")
        network = loadNetwork()
        print("Siec wczytana, co teraz chcesz robic?")
        isNetworkCreated = True
    if option == 4:
        break
    
network.errorPlot()